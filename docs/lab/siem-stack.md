# SIEM stack: Wazuh + Sysmon

**Level:** L2 · **Goal:** every lab attack leaves evidence you can search.

## Why Wazuh for the home lab
It's free and open source. A single-node install covers Linux and Windows agents, log collection,
file integrity monitoring and ATT&CK-tagged rules, and it runs in ~8 GB of RAM. When you want to
try others, Elastic (free self-managed tier), Splunk Free (500 MB/day) and Security Onion (network-centric)
are in the [blue tooling catalog](../resources/blue-tooling.md).

## 1. Wazuh server
- An Ubuntu Server VM on `lab`, 4 vCPU / 8 GB / 60 GB.
- Follow the official **quickstart (all-in-one)** install in the Wazuh docs.
- Browse to the dashboard from the Kali VM: `https://<wazuh-ip>`.

## 2. Windows telemetry
1. Install **Sysmon** with a community config. Start with **sysmon-modular** or
   **SwiftOnSecurity sysmon-config**.
2. Turn on the PowerShell logs (Script Block Logging, Module Logging) and process command-line
   auditing (*Include command line in process creation events*) via local policy or GPO.
3. Install the Wazuh agent, and add `Microsoft-Windows-Sysmon/Operational` and
   `Microsoft-Windows-PowerShell/Operational` to its event channels.

## 3. Linux telemetry
1. Install the Wazuh agent.
2. Enable **auditd** with a community ruleset (detailed in the Linux section).
3. Check that `auth.log` / `journal` shipping works: run a failed `ssh` login and find it in the dashboard.

## 4. Smoke tests

| Do this on the target | You should see |
|---|---|
| `whoami /all` in cmd | Sysmon Event ID 1 (process create) with the command line |
| Create a local user | Security 4720 (Windows) / `useradd` audit record (Linux) |
| 5 failed RDP or SSH logins | a brute-force rule alert |
| Edit a file in a monitored directory | an FIM alert |

When all four show up, snapshot the server and agents as `siem-ready`.
