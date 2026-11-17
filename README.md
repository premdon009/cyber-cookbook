# Cyber Cookbook

Red + blue team study cookbook for **Linux and Windows**, from beginner to expert, with an
**AI** track (how models work, using them, connecting tools via MCP, restricting access,
AI security) and **case studies** of famous CVEs and breaches.

Everything uses **free** reading material and **free or self-hosted labs**.

📖 **Read it as a site:** https://premdon009.github.io/cyber-cookbook/

## Quick start

```bash
uv sync                                        # install MkDocs Material
uv run mkdocs serve                            # http://127.0.0.1:8000
uv run python scripts/fetch_resources.py       # optional: offline clones into resources/
```

## Layout

| Path | What |
|---|---|
| `docs/` | The notes (MkDocs site), split into sections `00-foundations` … `90-case-studies` |
| `docs/lab/` | Home-lab build guide (hypervisor, SIEM, Docker CVE targets, GOAD AD lab) |
| `docs/note-templates/` | Recipe, case-study, lab write-up and tool-card templates |
| `resources.yml` | Single source for every external resource and lab |
| `scripts/gen_catalog.py` | Renders `docs/resources/*.md` from `resources.yml` |
| `scripts/fetch_resources.py` | Shallow-clones `clone: true` repos for offline reading |
| `scripts/check_links.py` | Finds dead links (CI runs it weekly) |

## Progress

| Phase | Scope | Status |
|---|---|---|
| P0 | Scaffold, resource catalog, roadmap, home lab, templates, CI | ✅ |
| P1 | Foundations + Linux | ⏳ |
| P2 | Windows + Active Directory | ⏳ |
| P3 | Red team | ⏳ |
| P4 | Blue team | ⏳ |
| P5 | Purple team, cloud & containers, specialties | ⏳ |
| P6 | AI track + AI lab | ⏳ |
| P7 | Case studies (famous CVEs & hacks, incl. 2025–26) | ⏳ |

## Ethics

Offensive content is for **your own lab** or systems you have **written permission** to test.
See [docs/ethics-and-legal.md](docs/ethics-and-legal.md).

## Licence

Notes: [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). Scripts: MIT.
Linked resources keep their own licences.
