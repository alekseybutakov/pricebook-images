#!/usr/bin/env bash
# Качает картинки из manifest_T23.tsv (колонки: имя_файла<TAB>URL) в текущую папку.
set -u
[ -f manifest_T23.tsv ] || { echo "нет manifest_T23.tsv"; exit 1; }
ok=0; skip=0; fail=0
while IFS=$'\t' read -r name url; do
  [ -z "${name:-}" ] && continue
  case "$name" in \#*) continue;; esac
  if [ -s "$name" ]; then skip=$((skip+1)); continue; fi
  if curl -fsSL --max-time 60 -A "Mozilla/5.0" -o "$name.part" "$url"; then
    mv "$name.part" "$name"; ok=$((ok+1)); echo "OK   $name"
  else
    rm -f "$name.part"; fail=$((fail+1)); echo "FAIL $name  <- $url"
  fi
done < manifest_T23.tsv
echo "---- скачано $ok, пропущено (уже есть) $skip, не скачалось $fail"
