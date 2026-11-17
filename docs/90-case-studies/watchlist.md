# Watchlist: where new cases come from

Check these weekly. Write up an incident as a case study when it is **widely exploited**,
**teaches a new technique**, or **changes how defenders work**.

| Source | Why |
|---|---|
| [CISA KEV catalog](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) | CVEs confirmed exploited in the wild; the strongest signal |
| [NVD](https://nvd.nist.gov/) | CVE details, CVSS, references |
| [Project Zero: 0-days in the wild](https://googleprojectzero.github.io/0days-in-the-wild/) | root-cause analyses of exploited zero-days |
| [The DFIR Report](https://thedfirreport.com/) | full intrusion timelines with ATT&CK mapping and detections |
| [MITRE ATT&CK campaigns](https://attack.mitre.org/campaigns/) | documented campaigns mapped to techniques |
| [MITRE ATLAS case studies](https://atlas.mitre.org/) | real attacks on AI systems |
| Vendor PSIRTs (Microsoft MSRC, Cisco, Fortinet, Ivanti, Citrix…) | the official advisory, the first primary source |
| Vendor threat-intel blogs (Mandiant / Google, Microsoft Threat Intelligence, Unit 42, Talos) | attribution and TTP detail |

## How to add a case

- [ ] Confirm the facts from **at least two primary sources** (vendor advisory, NVD, CISA,
      the original researcher).
- [ ] Copy the [case-study template](../note-templates/case-study.md) and fill in every section.
- [ ] Map each attack-chain step to an ATT&CK technique.
- [ ] Write the defender side: at least one concrete detection idea.
- [ ] Look on Vulhub for a lab environment. If there is one, write the *Lab it* section and test it
      in the isolated lab.
- [ ] Link the case from the related topic notes, and the topic notes back from the case.
- [ ] Add a row to the [case index](index.md).
- [ ] No exploit code, no live IOCs that could harm someone, and no victim data beyond what is
      public.
