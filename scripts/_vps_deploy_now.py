#!/usr/bin/env python3
"""Direct VPS upload for Google Ads audit pages (mirrors vps-deploy.yml scope)."""
import os
import sys
from pathlib import Path

import paramiko

HOST = "72.62.34.234"
ROOT = Path(__file__).resolve().parents[1]

# Relative paths / dirs to upload (file or directory ending with /)
DEPLOY_PATHS = [
    "index.html",
    "es/",
    "pl/smartwatch/",
    "gr/smartwatch/",
    "pl/casa-fuego/",
    "cz/casa-fuego/",
    "sk/casa-fuego/",
    "cz/terms-conditions.html",
    "assets/js/consent-default.js",
    "assets/js/main.js",
    "assets/js/tracking.js",
    "assets/css/components.css",
]

REFUND_GEOS = [
    "bg", "cz", "de", "ee", "en", "es", "fr", "gr", "hr", "hu",
    "it", "lt", "lv", "pl", "pt", "ro", "si", "sk",
]

password = os.environ.get("VPS_PASS", "")
users = ["root", "admin", "ubuntu", "otger", "trendtopia"]

client = None
for user in users:
    c = paramiko.SSHClient()
    c.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        c.connect(HOST, username=user, password=password, timeout=15, allow_agent=False, look_for_keys=False)
        client = c
        print(f"connected as {user}")
        break
    except paramiko.AuthenticationException:
        pass
    except Exception as ex:
        print(f"connect error {user}: {ex}")
    finally:
        if client is not c:
            c.close()

if not client:
    print("NO_SSH — set VPS_PASS or use GitHub Actions deploy")
    sys.exit(1)


def find_bases():
    _, stdout, stderr = client.exec_command(
        "for b in /var/www/trendtopia-store.com /var/www/adclickmobile.com /var/www/html /root/trendtopia-store.com; do "
        '[ -d "$b" ] && echo "$b"; done'
    )
    lines = [l.strip() for l in (stdout.read() + stderr.read()).decode().splitlines() if l.strip().startswith("/")]
    return lines or ["/var/www/html"]


def ensure_dir(sftp, remote_dir: str) -> None:
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


def upload_file(sftp, local: Path, remote: str) -> None:
    ensure_dir(sftp, os.path.dirname(remote))
    with sftp.file(remote, "wb") as f:
        f.write(local.read_bytes())
    print(f"uploaded {remote} ({local.stat().st_size} bytes)")


sftp = client.open_sftp()
bases = find_bases()
print("bases:", bases)

files_to_upload: list[tuple[Path, str]] = []
for rel in DEPLOY_PATHS:
    local = ROOT / rel.replace("/", os.sep).rstrip(os.sep)
    if rel.endswith("/"):
        if not local.is_dir():
            print(f"skip missing dir {rel}")
            continue
        for fp in local.rglob("*"):
            if fp.is_file():
                rrel = fp.relative_to(ROOT).as_posix()
                files_to_upload.append((fp, rrel))
    elif local.is_file():
        files_to_upload.append((local, rel.replace("\\", "/")))
    else:
        print(f"skip missing {rel}")

for geo in REFUND_GEOS:
    fp = ROOT / geo / "refund-policy.html"
    if fp.is_file():
        files_to_upload.append((fp, f"{geo}/refund-policy.html"))

for base in bases:
    for local, rrel in files_to_upload:
        remote = f"{base}/{rrel}"
        try:
            upload_file(sftp, local, remote)
        except Exception as ex:
            print(f"fail {remote}: {ex}")

sftp.close()
client.close()
print(f"DONE — {len(files_to_upload)} files × {len(bases)} bases")
