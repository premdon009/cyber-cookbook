# Case study template (CVE / breach)

Copy this into `docs/90-case-studies/<category>/<name>.md`. Explain how the bug or attack works
conceptually; **don't paste exploit code**. Link to primary sources.

````markdown
# <Name> (<CVE-YYYY-NNNNN>)

| | |
|---|---|
| **Date** | disclosed YYYY-MM-DD; exploited since … |
| **CVE / CVSS** | CVE-… / 9.8 (link to NVD) |
| **CISA KEV** | yes / no (date added) |
| **Affected** | product + versions |
| **Bug class** | e.g. buffer over-read, deserialization, auth bypass, supply-chain backdoor |
| **Impact** | what attackers got: data, RCE, domain takeover, outage |

## Timeline
- YYYY-MM-DD: introduced / initial access
- YYYY-MM-DD: discovered / disclosed
- YYYY-MM-DD: patch / mitigation released
- YYYY-MM-DD: mass exploitation / public PoC

## How it works
The root cause in plain words: which code path or design decision failed, and why. Add a diagram.

## Attack chain
| Step | What happened | ATT&CK |
|---|---|---|
| Initial access | … | T1190 |
| … | … | … |

## Use case: attacker side
What the attacker wanted, why this target was valuable, and what the bug let them do next.

## Use case: defender side
- **Signals that would have caught it:** logs, network indicators, process trees
- **Detection idea:** a Sigma rule or query (link to a public rule if there is one)
- **Mitigation:** the patch, config change, or compensating control
- **What would have broken the chain earlier:** segmentation, MFA, least privilege, egress filtering…

## Lab it
Where safe: the Vulhub (or similar) environment that reproduces it, run inside the isolated lab.
Do the detection side too.

## Lessons
3–5 bullet points, each linked to the related topic notes in this cookbook.

## Sources
- Vendor advisory
- NVD entry
- CISA alert / KEV entry
- Researcher or incident-response write-up
````
