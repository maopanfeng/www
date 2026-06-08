#!/usr/bin/env bash
set -euo pipefail

source_dir="/Users/ben/Obsidian/WWW"
site_dir="$(cd "$(dirname "$0")/.." && pwd)"

if [ ! -d "$source_dir" ]; then
  echo "Obsidian publish folder not found: $source_dir"
  exit 1
fi

for folder in cn en; do
  if [ -d "$source_dir/$folder" ]; then
    mkdir -p "$site_dir/content/$folder"
    rsync -a --delete \
      --exclude ".DS_Store" \
      --exclude ".obsidian" \
      --exclude ".git" \
      "$source_dir/$folder/" "$site_dir/content/$folder/"
  fi
done

echo "Synced public Obsidian notes from $source_dir to $site_dir."
