# Stocks recovery, 2026-11-08

## Evidence and root cause

- `1366d38` independently introduced `content/cn/stocks/300433.md` (Lens Technology), dated 2026-07-01. Its current content is preserved byte-for-byte.
- `961f75c` (2026-11-05) deleted both Yili articles and the original Chinese Yoke article at `content/en/stocks/YokeTechnology.md`, including its October follow-up section.
- Subsequent commits restored Yoke under stock code 002409 in both languages and published Sigenergy under 06656.
- `64631f2` (2026-11-07) deleted both languages of 002409 and 06656, while reintroducing 300433. Its Cloudflare Pages check completed successfully. Live `/cn/stocks/` showed Lens and lacked the deleted articles.
- The repository's Obsidian sync used `rsync -a --delete`: files published directly to GitHub but absent from the local vault are deleted. The commit diffs match this failure mode. The external machine/vault that produced these commits is not accessible in this checkout.
- Hugo lists `.Pages` / `.Site.RegularPages` and links each page's `.RelPermalink`. Dates order entries; they do not identify or replace them. No custom date-to-company mapping exists.

## Recovery

- Restore 002409 and 06656 in both languages from `0b7cc42`.
- Restore Yili in both languages from `3551ebe`, including the corrected English link.
- Restore the Chinese Yoke follow-up section from `3551ebe` (originally added by `9c28ed2`). Keep the English translation from `3adbc47`.
- Keep distinct routes `/cn/stocks/002409/` and `/cn/stocks/300433/`, both legitimately dated 2026-07-01. Add the old `/stocks/yoketechnology/` alias to the English 002409 page.
- Remove `--delete` from synchronization. Missing vault files are no longer implicit deletion requests. Intentional deletions should be reviewed and made explicitly in Git.
- Add an optional `OBSIDIAN_PUBLISH_DIR` override and a regression test covering remote-only article preservation, normal updates, new files, and excluded files in both languages.

## Operational follow-up

The machine running automatic Obsidian publishing must pull this commit before its next synchronization. This checkout cannot update a different machine's script or vault. Old copies of the script still contain the destructive flag. Do not force-push an outdated checkout over the recovery.

## Other monthly articles

Yili (November) and Sigenergy (September) suffered the same deletions and are restored. Earlier deleted Chinese Gemini, Nvidia and Palantir files in `b156f83` were moves to Books, not missing articles, and are left unchanged.

AAOI (May) and INTL (June) contain pre-existing Carvana discussion copied into their bodies. This is a separate content-quality issue, not a route collision; no verified replacement research was found in their file histories. Their content is left unchanged in this recovery rather than inventing research.

## Checks

Run `python3 -m unittest discover -s tests -v`, `bash -n scripts/*.sh`, and `hugo --gc --minify --printPathWarnings`. Inspect Hugo's page inventory, built pages and Stocks/home listings for unique URLs, expected titles and dates. Verify Cloudflare's check for the pushed commit and fetch the live article and listing URLs directly; search-engine caches alone are not deployment evidence.
