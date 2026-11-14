# Website article source

The Mac mini writing source is `/Users/ben/WEBSITE/www`, inside the WEBSITE Obsidian Sync vault. MOS is a separate iCloud vault and is not a publishing source. The website checkout is separate from the vault.

Write article changes to the vault as well as the website checkout. Sync only the public `cn` and `en` directories. The sync script defaults to `$HOME/WEBSITE/www`; `OBSIDIAN_PUBLISH_DIR` can override it. Do not reintroduce `rsync --delete`.

## Restored articles

- `002409.md`: Yoke Technology, July 1, 2026.
- `06656.md`: Sigenergy, September 1, 2026.
- `600887.md`: Yili, November 1, 2026. Old `yili` URLs remain aliases.
- `AAOI.md`: November 7, 2026 Fengli Investment report, `/cn/stocks/aaoi/`. Chinese page contains the full 50-item report; English page links to it and is not a full translation. Replaces unrelated Carvana text in the old English AAOI page.
- `300433.md`: withdrawn by the owner. Remove from the vault as well as Git. Do not restore it during synchronization.

`data/required_stocks.json` and the homepage's validation partial prevent a successful Hugo deployment if a required article disappears, a stock identity changes, or the withdrawn Lens article reappears. Intentional future removals must also update the manifest; this is a publication invariant, not a recommendation to restore deleted content automatically.

Tests: `python3 -m unittest discover -s tests -v`. Set `HUGO_BIN` if Hugo is not on PATH. Build with `hugo --gc --minify --cleanDestinationDir --printPathWarnings`.

## Machine status

The eight source files were written and verified in the Mac mini vault on November 8, 2026; overwritten source content was backed up outside the Git checkout. This does not prove that Obsidian Sync has finished on either MBP. No automatic publisher was installed on the Mac mini as part of this article repair, and the remote MBP job has not been inspected or disabled. Complete the single-publisher handover before claiming that machine migration is finished.
