# Cyber Cookbook

A study cookbook for becoming a well-rounded security practitioner, covering **red team**
(offence) and **blue team** (defence) on **Linux and Windows**, from zero to expert, plus an
**AI** track and **case studies** of famous CVEs and breaches.

Everything here uses **free** reading material and **free or self-hosted labs**. Freemium
platforms are tagged 🟡 and are only listed when the free tier is enough to learn from.

!!! warning "Lab only"
    Everything offensive in this cookbook is meant for **your own lab** or systems you have
    **written permission** to test. Read [Ethics & legal](ethics-and-legal.md) first.

## How it is organised

| Section | What you learn |
|---|---|
| [Roadmap](roadmap.md) | Levels L0 → L5 with notes, labs and a capstone per level |
| [Home lab](lab/index.md) | Build an isolated lab: attacker VM, AD domain, SIEM |
| [Foundations](00-foundations/index.md) | Networking, OS concepts, scripting, crypto, web basics |
| [Linux](10-linux/index.md) | Admin → hardening → privesc → forensics |
| [Windows & AD](20-windows/index.md) | Internals, PowerShell, event logs, Active Directory attack and defence |
| [Red team](30-red-team/index.md) | Methodology, recon, web, AD attack paths, exploitation, reporting |
| [Blue team](40-blue-team/index.md) | SOC, SIEM, detection engineering, hunting, IR, DFIR, malware analysis |
| [Purple team](50-purple-team/index.md) | Emulate → detect → improve loops with ATT&CK |
| [Cloud & containers](60-cloud-containers/index.md) | AWS/Azure/GCP IAM, Docker, Kubernetes |
| [Specialties](70-specialties/index.md) | Reverse engineering, binary exploitation, crypto, mobile, OSINT |
| [AI](80-ai/index.md) | How models work, using them, connecting tools (MCP), restricting access, AI security |
| [Case studies](90-case-studies/index.md) | Heartbleed → Log4Shell → xz-utils and beyond: how they worked, how to catch them |
| [Resources](resources/index.md) | The full catalog of free resources and labs |

## The recipe format

Every topic note is a **recipe**: what & why → how it works → Linux / Windows commands →
**red view** (abuse + ATT&CK ID) → **blue view** (artifacts, detection, prevention) → lab
exercise → self-check → go deeper. See the [recipe template](note-templates/recipe.md).

## Offline reading

```bash
uv sync
uv run python scripts/fetch_resources.py      # shallow-clones cheat sheets & lists into resources/
uv run mkdocs serve                           # browse this site locally at http://127.0.0.1:8000
```
