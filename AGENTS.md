# Cyber Cookbook — Agent Memory

The owner's red + blue team study cookbook (Linux & Windows, L0 beginner → L5 expert), with an AI
track and CVE/breach case studies. Free or self-hosted resources and labs only. Built with MkDocs
Material and published to GitHub Pages: https://premdon009.github.io/cyber-cookbook/

**The approved plan is [PLAN.md](PLAN.md). Read it before starting a phase.**

## Phase status (update this table when a phase lands)

| Phase | Scope | Status |
|---|---|---|
| P0 | Scaffold, catalog, roadmap, home lab, templates, CI | ✅ 2026-11-17 |
| P1 | `docs/00-foundations/` + `docs/10-linux/` | ⏳ next |
| P2 | `docs/20-windows/` (incl. Active Directory) | ⏳ |
| P3 | `docs/30-red-team/` | ⏳ |
| P4 | `docs/40-blue-team/` | ⏳ |
| P5 | `docs/50-purple-team/`, `60-cloud-containers/`, `70-specialties/` | ⏳ |
| P6 | `docs/80-ai/` + `docs/lab/ai-lab.md` | ⏳ |
| P7 | `docs/90-case-studies/` (+ web research for 2025–26 incidents) | ⏳ |

One phase per session. Each section's `index.md` lists the planned notes; flip "planned" to a
link as each note is written. Keep `README.md`'s progress table in sync.

## Content rules (never break)

1. Every topic note uses `docs/note-templates/recipe.md`, and every case uses
   `docs/note-templates/case-study.md`. Red view and blue view always appear together.
2. Educational and lab-scoped: explain how a technique works, its ATT&CK ID, and how to detect and
   prevent it. **No weaponised exploit code, malware samples, or guides to evading real security
   products.** Red sections link to `docs/ethics-and-legal.md`.
3. Free resources only. A freemium resource is tagged `freemium` and listed only if its free tier
   is enough to learn from. Every external link goes through `resources.yml` (add the entry, then
   run `gen_catalog.py`), apart from one-off citations inside a note.
4. Case studies: confirm facts from 2+ primary sources (vendor advisory, NVD, CISA, the researcher's
   write-up). Don't invent CVE numbers, dates or CVSS scores; if one can't be confirmed, say so.

## Commands

```bash
unset VIRTUAL_ENV; export NO_MKDOCS_2_WARNING=1   # outer venvs confuse uv; silence MkDocs EOL banner
uv sync
uv run mkdocs serve                               # preview at http://127.0.0.1:8000
uv run python scripts/gen_catalog.py              # after editing resources.yml
uv run python scripts/check_links.py              # 0 FAIL required; WARN = bot-blocked, check by hand
uv run python scripts/fetch_resources.py --dry-run
```

**Done means** all four of these pass: `uv run mkdocs build --strict`, `gen_catalog.py --check`,
`check_links.py` (0 fail), `uv lock --check`. Then commit (conventional commits, e.g.
`feat(linux): ...`) and push to `main`; the Pages workflow deploys. Check that the run is green
with `gh run list`.

## Gotchas

- MkDocs always excludes any `docs/templates/` folder, which is why the templates live in
  `docs/note-templates/`.
- `.gitignore` must use `/resources/` (anchored to the root). A bare `resources/` also ignores the
  generated `docs/resources/` catalog, and CI fails.
- `mkdocs.yml` sets `validation.omitted_files: warn`, so under `--strict` a page in `docs/` must be
  reachable from a `.nav.yml` (folders listed in `docs/.nav.yml` include their pages automatically).
  Keep planning files like `PLAN.md` at the repo root, not in `docs/`.
- Material for MkDocs reaches end of life on 2027-05-05. Its successor, Zensical, reads `mkdocs.yml`;
  a migration is a future task, not urgent.
