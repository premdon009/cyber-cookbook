# How to use this cookbook

## Study loop

1. **Read the recipe**: understand the *what & why* and the *how it works* first.
2. **Run the commands** on both platforms in your [home lab](lab/index.md). Never run them on your daily machine.
3. **Do the red view**: abuse the technique against a lab target.
4. **Do the blue view**: find what it left behind (logs, events, files, network traffic), then write or
   tune a detection.
5. **Answer the self-check questions** without looking.
6. **Write your own lab write-up** with the [lab write-up template](note-templates/lab-writeup.md),
   and keep it in your private notes or in `docs/` here.

## Note conventions

- **Levels:** `L0`…`L5`, matching the [roadmap](roadmap.md).
- **ATT&CK IDs:** written like `T1003.001`, and linked to attack.mitre.org.
- **Cost tags:** 🟢 free · 🟡 freemium · 🔵 self-hosted.
- **Platform tabs:** commands appear in `Linux` / `Windows` tabs.

## Working on the repo

```bash
uv sync                                          # installs mkdocs-material etc.
uv run mkdocs serve                              # live preview
uv run python scripts/gen_catalog.py             # after editing resources.yml
uv run python scripts/check_links.py             # find dead links
uv run python scripts/fetch_resources.py --only sigma hacktricks   # offline clones
uv run mkdocs build --strict                     # what CI runs
```

**Adding a resource:** add an entry to `resources.yml` (the schema is in the file header), run
`gen_catalog.py`, and commit both files. CI fails if the catalog pages are out of date.

**Adding a note:** copy a template from `docs/note-templates/` into the right section folder. Folders
pick up new pages automatically.
