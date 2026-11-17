# Case studies: famous CVEs and hacks

Real incidents are where the topics connect. Each case explains **how it worked**, the
**attack chain mapped to ATT&CK**, the **attacker's and defender's use case**, and how
to **reproduce it safely** in the lab where a purpose-built vulnerable environment exists.
Every case follows the [case-study template](../note-templates/case-study.md).

!!! info "Status"
    The cases are written in phase **P7**, which also adds researched 2025–2026 incidents.
    New incidents are picked from the [watchlist](watchlist.md).

## Planned cases

| Year | Case | Category | Lab repro |
|---|---|---|---|
| 1988 | Morris Worm | Worm | n/a (history) |
| 2010 | Stuxnet | Nation-state / ICS | n/a |
| 2013 | Target breach (HVAC vendor access) | Identity / third party | n/a |
| 2014 | Heartbleed (CVE-2014-0160) | Linux / open source | Vulhub |
| 2014 | Shellshock (CVE-2014-6271) | Linux / open source | Vulhub |
| 2016 | Dirty COW (CVE-2016-5195) | Linux kernel | VM with an old kernel |
| 2017 | Equifax / Apache Struts2 (CVE-2017-5638) | Web | Vulhub |
| 2017 | EternalBlue (MS17-010) → WannaCry, NotPetya | Windows / worms | Metasploitable 3 |
| 2018 | Spectre / Meltdown | Hardware | n/a (concept) |
| 2020 | Zerologon (CVE-2020-1472) | Windows / AD | GOAD (unpatched DC snapshot) |
| 2020 | SolarWinds SUNBURST | Supply chain | n/a |
| 2021 | ProxyLogon / ProxyShell | Windows / Exchange | n/a |
| 2021 | PrintNightmare (CVE-2021-34527) | Windows | GOAD |
| 2021 | Colonial Pipeline | Ransomware | n/a |
| 2021 | Kaseya VSA | Supply chain / ransomware | n/a |
| 2021 | Log4Shell (CVE-2021-44228) | Web / Java | Vulhub |
| 2022 | PwnKit (CVE-2021-4034) | Linux | Vulhub / old distro VM |
| 2022 | Dirty Pipe (CVE-2022-0847) | Linux kernel | VM with an old kernel |
| 2022 | Follina (CVE-2022-30190) | Windows / Office | n/a |
| 2022 | Uber (MFA fatigue) | Identity / social engineering | n/a |
| 2022 | LastPass | Identity / cloud | n/a |
| 2023 | 3CX | Supply chain | n/a |
| 2023 | MOVEit Transfer (CVE-2023-34362) | Web / edge | n/a |
| 2023 | Citrix Bleed (CVE-2023-4966) | Edge device | n/a |
| 2023 | MGM Resorts (help-desk social engineering) | Identity / social engineering | n/a |
| 2023 | Storm-0558 signing key | Cloud identity | n/a |
| 2024 | Ivanti Connect Secure chain (CVE-2023-46805 / CVE-2024-21887) | Edge device | n/a |
| 2024 | xz-utils backdoor (CVE-2024-3094) | Supply chain / Linux | n/a (concept) |
| 2024 | Midnight Blizzard vs Microsoft | Cloud identity | n/a |
| 2024 | Change Healthcare | Ransomware | n/a |
| 2024 | Snowflake customer breaches | Cloud identity | n/a |
| 2024 | regreSSHion (CVE-2024-6387) | Linux / OpenSSH | VM with an old OpenSSH |
| 2024 | Salt Typhoon telecom intrusions | Nation-state / telecom | n/a |
| 2024 | CrowdStrike outage (not a hack) | Resilience | n/a |
| 2025 | EchoLeak in M365 Copilot (CVE-2025-32711) | AI | links to the [AI](../80-ai/index.md) track |
| 2025 | SharePoint "ToolShell" (CVE-2025-53770) | Windows / web | n/a |
| 2025–26 | *researched in P7* | | |

"n/a" for lab repro means no safe, purpose-built environment exists. Those cases are studied from
public write-ups and the detection side, using public log datasets where possible.
