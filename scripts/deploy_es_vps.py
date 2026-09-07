#!/usr/bin/env python3
"""Upload only ES locale + shared compliance assets to VPS web roots."""
from __future__ import annotations

import os
import sys
from pathlib import Path

import paramiko

HOST = "72.62.34.234"
ROOT = Path(__file__).resolve().parents[1]

SHARED = [
    "assets/js/consent-default.js",
    "assets/js/main.js",
    "assets/js/tracking.js",
    "assets/css/components.css",
]

USERS = ["root", "admin", "ubuntu", "otger", "trendtopia"]


def es_files() -> list[str]:
    files = [p.relative_to(ROOT).as_posix() for p in ROOT.glob("es/**/*.html")]
    return sorted(files)


def collect_files() -> list[str]:
    out = es_files()
    for rel in SHARED:
        if (ROOT / rel).is_file():
            out.append(rel)
    return out


def find_bases(client: paramiko.SSHClient) -> list[str]:
    _, stdout, stderr = client.exec_command(
        "for b in /var/www/trendtopia-store.com /var/www/adclickmobile.com "
        "/var/www/html /root/trendtopia-store.com; do "
        '[ -d "$b/es" ] && echo "$b"; done'
    )
    bases = [l.strip() for l in (stdout.read() + stderr.read()).decode().splitlines() if l.strip()]
    return bases or ["/var/www/trendtopia-store.com"]


def ensure_remote_dir(sftp: paramiko.SFTPClient, remote_dir: str) -> None:
    path = ""
    for part in remote_dir.replace("\\", "/").split("/"):
        if not part:
            continue
        path += "/" + part
        try:
            sftp.stat(path)
        except FileNotFoundError:
            try:
                sftp.mkdir(path)
            except OSError:
                pass


def main() -> int:
    password = os.environ.get("VPS_PASS", "")
    if not password:
        print("Set VPS_PASS environment variable.", file=sys.stderr)
        return 1

    files = collect_files()
    print(f"Deploying {len(files)} files (ES + shared assets)")

    client: paramiko.SSHClient | None = None
    for user in USERS:
        c = paramiko.SSHClient()
        c.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            c.connect(HOST, username=user, password=password, timeout=20, allow_agent=False, look_for_keys=False)
            client = c
            print(f"Connected as {user}")
            break
        except paramiko.AuthenticationException:
            c.close()
        except Exception as exc:
            print(f"connect error ({user}): {exc}")
            c.close()

    if not client:
        print("SSH authentication failed", file=sys.stderr)
        return 1

    bases = find_bases(client)
    print("Web roots:", ", ".join(bases))

    sftp = client.open_sftp()
    uploaded = 0
    for rel in files:
        local = ROOT / rel.replace("/", os.sep)
        data = local.read_bytes()
        for base in bases:
            remote = f"{base}/{rel}"
            ensure_remote_dir(sftp, os.path.dirname(remote))
            with sftp.file(remote, "wb") as fh:
                fh.write(data)
            uploaded += 1
            print(f"  {remote} ({len(data)} B)")

    sftp.close()
    client.close()
    print(f"DONE — {uploaded} uploads across {len(bases)} root(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
