#!/usr/bin/env bash
# Verify pre-rendered home HTML (no JS). Usage: ./scripts/verify_home_ssr.sh [base_url]
set -euo pipefail
BASE="${1:-}"
check_file() {
  local file="$1"
  local lang="$2"
  local needle="$3"
  grep -q "lang=\"${lang}\"" "$file" || { echo "FAIL lang $file"; exit 1; }
  grep -q "$needle" "$file" || { echo "FAIL content $file ($needle)"; exit 1; }
  grep -q 'option value="es"' "$file" || { echo "FAIL select options $file"; exit 1; }
  echo "OK $file"
}
if [ -n "$BASE" ]; then
  for loc in en es pl; do
    html=$(curl -fsSL -H "Accept-Language: ${loc}" "$BASE/")
    echo "$html" | grep -q "data-ssr-locale=\"${loc}\"" || echo "WARN: / may not route locale $loc yet (nginx maps?)"
  done
else
  ROOT="$(cd "$(dirname "$0")/.." && pwd)"
  check_file "$ROOT/home/index.en.html" "en" "Choose your country"
  check_file "$ROOT/home/index.es.html" "es" "49,00 €"
  check_file "$ROOT/home/index.pl.html" "pl" "199,00 zł"
  check_file "$ROOT/home/index.gr.html" "el" "69,00 €"
fi
