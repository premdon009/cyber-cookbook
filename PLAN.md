# Plan: `cyber-cookbook`, a red + blue team study repo (Linux & Windows, beginner to expert)

## Context
The owner wants a personal, public study repo for becoming a well-rounded security practitioner,
covering both offence (red team) and defence (blue team) on Linux and Windows, from the basics up
to expert level. It should collect the best **free** reading material and **free or self-hosted
labs** (nothing paywalled; freemium items are tagged as such), and hold the owner's own cookbook-style
notes. Decisions already made:
- Location: `~/cyber-cookbook` (it does not exist yet), as a new git repo pushed to **public**
  GitHub `premdon009/cyber-cookbook` (gh is already logged in), with the site on **GitHub Pages**.
- Format: **MkDocs Material**. The files stay plain Markdown, so they also read fine on GitHub.
- External repos: **curated links + a clone script** into a git-ignored `resources/` folder.
- Depth: **full notes for every topic**, written in phases over several sessions.

This is unrelated to telecom-sentinel. Nothing in that repo is touched.

## Repo layout
```
cyber-cookbook/
├── pyproject.toml, uv.lock     # mkdocs-material, mkdocs-awesome-nav, pyyaml (uv-managed)
├── mkdocs.yml                  # Material theme, search, dark mode, admonitions, tabs, code copy
├── resources.yml               # SINGLE SOURCE for every external resource (see below)
├── scripts/
│   ├── fetch_resources.py      # clones clone:true repos (shallow) into resources/<category>/
│   ├── gen_catalog.py          # resources.yml -> docs/resources/*.md tables
│   └── check_links.py          # HEAD/GET every URL, report dead/redirected (stdlib only)
├── .github/workflows/
│   ├── pages.yml               # build --strict + deploy to Pages on push to main
│   └── links.yml               # weekly link check, opens an issue on rot
├── resources/                  # .gitignored offline clones
└── docs/
    ├── index.md, roadmap.md, how-to-use.md, ethics-and-legal.md
    ├── lab/                    # home-lab build: hypervisor, isolated networks, snapshots,
    │                           # Kali/Parrot attacker, Win Server AD (GOAD), SIEM stack, safety
    ├── 00-foundations/         # networking, OS concepts, Linux CLI, Windows basics,
    │                           # Bash/Python/PowerShell, crypto basics, web/HTTP, virtualization
    ├── 10-linux/               # admin, permissions, systemd, logging/auditd, hardening (CIS),
    │                           # enumeration, privesc, persistence, Linux forensics
    ├── 20-windows/             # internals, registry, services, PowerShell, event logs, Sysmon,
    │                           # AD fundamentals, Kerberos/NTLM, privesc, AD attacks, hardening/tiering
    ├── 30-red-team/            # methodology & ROE, OSINT/recon, scanning, web (OWASP Top 10),
    │                           # network attacks, AD attack paths, exploitation/pwn, pivoting,
    │                           # C2 concepts, OPSEC, reporting
    ├── 40-blue-team/           # SOC workflow, SIEM (Wazuh/Elastic/Splunk Free), log sources,
    │                           # detection engineering (Sigma), threat hunting, IR lifecycle,
    │                           # DFIR (disk/memory/Volatility, Velociraptor), network security monitoring
    │                           # (Zeek/Suricata), malware analysis (static/dynamic), threat intel
    ├── 50-purple-team/         # ATT&CK-mapped emulation (Atomic Red Team, Caldera), detection
    │                           # validation loop, coverage tracking
    ├── 60-cloud-containers/    # AWS/Azure/GCP IAM & attacks, Docker/K8s security
    ├── 70-specialties/         # reverse engineering, binary exploitation, crypto, mobile, OSINT deep dive
    ├── 80-ai/                  # AI: how it works, using it, managing and securing it (see below)
    ├── 90-case-studies/        # famous CVEs + real breaches, old to new (see below)
    ├── resources/              # GENERATED catalog pages (by category, with level and cost tags)
    └── note-templates/         # recipe, case-study, lab-writeup, tool-card
```

## The cookbook "recipe" format (every topic note)
Each note follows `docs/note-templates/recipe.md`, so red and blue always appear side by side:
1. **What & why**: the concept, and where it fits in the roadmap level (L0–L5)
2. **How it works**: mechanics, with a diagram when it helps
3. **Linux / Windows**: commands in Material content tabs
4. **Red view**: how it's abused, with the ATT&CK technique ID
5. **Blue view**: what it leaves behind (event IDs, log paths, a Sigma rule or query), and how to prevent it
6. **Lab it**: a concrete exercise on a named free/self-hosted lab
7. **Check yourself**: 3–5 questions
8. **Go deeper**: links pulled from `resources.yml`

## AI track (`docs/80-ai/`)
A parallel track that runs alongside L1–L5, in five sub-sections:
1. **How models work**: ML basics, neural nets, tokens and embeddings, transformers and attention,
   pre-training vs fine-tuning vs RLHF, context windows, sampling (temperature, top-p),
   hallucination, and the difference between open-weight and hosted models.
2. **Using models**: prompting patterns, system prompts, structured output, RAG (embeddings and vector
   DBs), evals, running local models (Ollama, llama.cpp), and API basics with cost and token limits.
3. **Connecting models to tools**: function/tool calling, agents and agent loops, Model Context
   Protocol (MCP) servers and clients, sandboxing tool execution, and human-in-the-loop approval.
4. **Managing and restricting AI**: AI gateways and proxies (e.g. LiteLLM proxy: virtual keys, per-user
   budgets, rate limits, model allow-lists), RBAC in self-hosted UIs (Open WebUI), secrets handling,
   least-privilege tool scopes, logging and audit, data-leak controls, governance (NIST AI RMF,
   ISO 42001 overview, EU AI Act basics).
5. **AI security, red and blue**: OWASP Top 10 for LLM Applications, MITRE ATLAS, prompt injection
   (direct and indirect), jailbreaks, insecure output handling, tool/agent abuse, data and model
   poisoning, supply chain (model files, pickles); defences: guardrails (NeMo Guardrails, LLM Guard),
   input/output filtering, monitoring; offensive testing tools (garak, PyRIT, promptfoo); and AI used
   *for* security (SOC triage, detection writing, log summarisation) along with its limits.

Each note uses the same recipe format, with "Red view / Blue view" covering attacking vs securing
the AI system. Labs are all free or self-hosted: Lakera Gandalf, PortSwigger Web LLM attack labs,
Damn Vulnerable LLM Agent, a self-hosted lab of Ollama + Open WebUI + LiteLLM proxy + a toy MCP
server (written up in `docs/lab/ai-lab.md`).

## Case studies: famous CVEs and hacks (`docs/90-case-studies/`)
Each case uses `docs/note-templates/case-study.md`:
1. **Summary card**: date, CVE ID(s), CVSS score, affected product, impact, and whether it is on the CISA KEV list
2. **Timeline**: from initial access to disclosure to patch
3. **How it works**: the root cause explained (bug class, the vulnerable code path or design flaw),
   with a diagram; conceptual only, so no exploit code in the repo
4. **Attack chain**: each step mapped to an ATT&CK technique
5. **Use case, attacker side**: what an attacker gained, and why the target was valuable
6. **Use case, defender side**: logs and indicators that would have caught it, a detection idea
   (Sigma or query), the mitigation and patch, and what would have broken the chain earlier
7. **Lab it** (where safe): reproduce it against a pre-built vulnerable container (Vulhub has
   environments for many of these, e.g. Log4Shell, Struts2, Shellshock) inside the isolated home lab
8. **Lessons + links to related topic notes**, plus primary sources (vendor advisory, NVD, CISA,
   the researcher's write-up)

Grouped by category, with an index table sortable by year:
- **Linux / open source**: Heartbleed, Shellshock, Dirty COW, PwnKit, Dirty Pipe, regreSSHion,
  xz-utils backdoor
- **Windows / AD**: EternalBlue (MS17-010), Zerologon, PrintNightmare, ProxyLogon/ProxyShell,
  Follina, SharePoint "ToolShell"
- **Web / edge devices**: Equifax (Struts2), Log4Shell, MOVEit, Citrix Bleed, Ivanti Connect Secure chain
- **Supply chain**: SolarWinds SUNBURST, Kaseya VSA, 3CX, xz-utils (cross-listed)
- **Ransomware / worms**: Morris Worm, WannaCry, NotPetya, Colonial Pipeline, Change Healthcare
- **Identity / cloud / social engineering**: Target (HVAC vendor), Uber 2022 (MFA fatigue),
  MGM 2023, LastPass, Storm-0558 signing key, Midnight Blizzard, Snowflake customer breaches
- **Nation-state / ICS / telecom**: Stuxnet, Salt Typhoon telecom intrusions
- **Hardware**: Spectre/Meltdown
- **AI incidents**: data leaks via chat tools, indirect prompt injection in assistants (e.g. EchoLeak
  in M365 Copilot); cross-linked to `80-ai/`
- **Resilience (not a hack)**: the CrowdStrike July 2024 outage, as a change-management lesson

**Keeping it current:** a `watchlist.md` page lists where new cases come from (CISA KEV catalog,
NVD, vendor PSIRTs, Google Project Zero's "0-days in the wild" sheet, The DFIR Report, Mandiant /
Microsoft / Unit 42 threat blogs). During P7 I'll research incidents from 2025–2026 (past my
knowledge cutoff) on the web and add the most significant ones. A short "how to add a case"
checklist lets the owner keep adding new ones.

## Roadmap levels (`docs/roadmap.md`)
L0 Foundations → L1 Linux/Windows admin + networking → L2 Junior SOC / junior pentester →
L3 AD, web and DFIR practitioner → L4 Detection engineering / red-team operator → L5 Expert
(research, RE/exploit dev, purple-team leadership). Each level lists notes, labs, a capstone
project, and the free cert-prep material that maps to it (Sec+/CySA+/OSCP-style syllabi
used only as checklists).

## `resources.yml` schema + initial catalog
Fields: `name, url, repo (optional), category, level, cost: free|freemium|self-hosted, platform:
linux|windows|both, team: red|blue|purple|both, clone: bool, note`. Seed entries (each one is
checked during the build; any that turns out to be paywalled or dead is dropped):
- **Reference / reading**: HackTricks, PayloadsAllTheThings, The Hacker Recipes, ired.team,
  GTFOBins, LOLBAS, OWASP Cheat Sheet Series, OWASP WSTG, MITRE ATT&CK / D3FEND, Orange
  Cyberdefense AD mindmaps, Infosec_Reference, gracenolan/Notes, Linux Command Line (free book),
  Microsoft Learn security docs, Ultimate Windows Security event encyclopedia, SANS posters
- **Awesome lists**: awesome-pentest, awesome-security, Awesome-Red-Teaming, Red-Teaming-Toolkit,
  awesome-cybersecurity-blueteam, awesome-incident-response, awesome-threat-detection, awesome-osint,
  awesome-malware-analysis
- **Free online labs**: OverTheWire, picoCTF, pwn.college, PortSwigger Web Security Academy,
  CryptoHack, cryptopals, exploit.education, ROP Emporium, flaws.cloud / flaws2, Malware-Traffic-
  Analysis exercises, OpenSecurityTraining2; freemium-tagged: TryHackMe free rooms, HTB
  free tier, Blue Team Labs Online / CyberDefenders / LetsDefend free tiers
- **Self-hosted labs**: GOAD (AD), Vulhub, DVWA, OWASP Juice Shop, WebGoat, Metasploitable 2/3,
  VulnHub VMs, CloudGoat, Kubernetes Goat, Splunk Attack Range, DetectionLab (archived, noted as reference)
- **Blue tooling + datasets**: Wazuh, Security Onion, Elastic, Velociraptor, Zeek, Suricata,
  SigmaHQ, sysmon-modular / SwiftOnSecurity sysmon-config, Atomic Red Team, MITRE Caldera,
  OTRF Security-Datasets, EVTX-ATTACK-SAMPLES, Splunk BOTS v1–v3, Volatility 3, FLARE-VM, REMnux
- **RE / exploitation**: nightmare, how2heap, Ghidra, Practical Malware Analysis labs
- **AI**: Karpathy "Neural Networks: Zero to Hero", Hugging Face courses (LLM, agents), fast.ai,
  anthropics/courses + prompt-engineering tutorial, MCP specification + modelcontextprotocol/servers,
  OWASP GenAI / LLM Top 10, MITRE ATLAS, NIST AI RMF, garak, PyRIT, promptfoo, NeMo Guardrails,
  LLM Guard, LiteLLM, Ollama, Open WebUI, Lakera Gandalf, Damn Vulnerable LLM Agent

`clone: true` is set only for text-heavy repos worth reading offline (cheat sheets, awesome lists,
Sigma, Atomic Red Team, nightmare), not for big VM or tool repos.

## Phases (one session each, every phase ends committed + pushed)
- **P0 Scaffold** ✅ DONE 2026-11-17: repo, uv project, mkdocs.yml, the 3 scripts, `resources.yml`
  with the full verified catalog, generated catalog pages, roadmap, ethics page, templates,
  lab-setup section, both workflows, README. Create the GitHub repo, push, enable Pages.
- **P1 Foundations + Linux** (00, 10)
- **P2 Windows + Active Directory** (20)
- **P3 Red team** (30)
- **P4 Blue team** (40)
- **P5 Purple, cloud/containers, specialties** (50, 60, 70)
- **P6 AI track** (80 + `lab/ai-lab.md`)
- **P7 Case studies** (90): all the cases above, plus newly researched 2025–2026 incidents; each case
  links back to its topic notes (e.g. Zerologon → Windows/AD auth), then a final roadmap cross-link pass

The case-study template and `watchlist.md` ship in P0, so the earlier phases can already link
to case-study pages as placeholders.

Each content phase: write the notes in recipe format, link every lab exercise to a catalog entry,
run the checks below, then commit (conventional commits, no AI trailer) and push.

Content guardrails: everything is educational and lab-scoped. Offensive notes explain the
technique, its ATT&CK mapping and how to detect it, aimed at the owner's own lab. The repo ships
no weaponised payloads, no malware samples, and no step-by-step instructions for evading real-world
detection. Every red section links to `ethics-and-legal.md`.

## Verification
- `uv run mkdocs build --strict` passes (no broken internal links or nav errors)
- `uv run python scripts/check_links.py`: zero dead URLs in `resources.yml` and the docs
- `uv run python scripts/gen_catalog.py && git diff --exit-code docs/resources` (catalog in sync)
- `uv run python scripts/fetch_resources.py --dry-run`, then a real run of 2 repos into `resources/`;
  `git status` shows `resources/` as ignored
- `uv lock --check`
- After the push: the Pages workflow is green and the site loads at
  `https://premdon009.github.io/cyber-cookbook/`
- Look at `mkdocs serve` locally: nav, search, dark mode, content tabs on one sample recipe
