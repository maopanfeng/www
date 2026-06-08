#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")/.."

./scripts/sync-from-obsidian.sh

if ! git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
  echo "This folder is not a Git repository yet."
  exit 1
fi

if [ -n "$(git status --porcelain)" ]; then
  git add -A
  git commit -m "Update website from Obsidian"
else
  echo "No website changes to publish."
fi

if git remote get-url origin >/dev/null 2>&1; then
  git push origin HEAD
else
  echo "No Git remote named origin is configured yet."
  echo "Add your GitHub repository with:"
  echo "  git remote add origin <your-github-repo-url>"
fi
