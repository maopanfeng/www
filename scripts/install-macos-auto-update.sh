#!/usr/bin/env bash
set -euo pipefail

site_dir="$(cd "$(dirname "$0")/.." && pwd)"
plist="$HOME/Library/LaunchAgents/com.maopanfeng.website-publish.plist"

mkdir -p "$HOME/Library/LaunchAgents"

cat > "$plist" <<PLIST
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN"
  "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
  <key>Label</key>
  <string>com.maopanfeng.website-publish</string>
  <key>ProgramArguments</key>
  <array>
    <string>${site_dir}/scripts/publish.sh</string>
  </array>
  <key>StartInterval</key>
  <integer>300</integer>
  <key>StandardOutPath</key>
  <string>${site_dir}/.publish.log</string>
  <key>StandardErrorPath</key>
  <string>${site_dir}/.publish.err.log</string>
</dict>
</plist>
PLIST

launchctl unload "$plist" >/dev/null 2>&1 || true
launchctl load "$plist"

echo "Auto update installed. It checks for website changes every 5 minutes."
