# AD lab: GOAD (Game Of Active Directory)

**Level:** L3 · **Goal:** a realistic, deliberately vulnerable multi-domain Active Directory
environment to attack and defend.

## Why GOAD
GOAD is an open-source project by Orange Cyberdefense. It builds a multi-domain AD with dozens
of planted misconfigurations: Kerberoasting, AS-REP roasting, ACL abuse, ADCS ESC paths,
delegation, MSSQL links, and more. It supports VirtualBox, VMware, Proxmox and some cloud
providers. **GOAD-Light** (3 VMs) suits 32 GB hosts; the full lab needs more.

## Install outline
Follow the official GOAD docs (linked in the [catalog](../resources/self-hosted-labs.md)). Roughly:
1. Install the prerequisites the docs list for your provider (Vagrant, Ansible, or Docker for the
   provisioning container).
2. Pick a lab (`GOAD-Light` first) and provider, then run the GOAD installer.
3. Provisioning downloads Windows evaluation images and takes 1–3 hours.
4. Attach the lab VMs to your `lab` network, or adjust the GOAD IP range to match it.

## Make it a blue lab too
- Deploy Sysmon + the Wazuh agent to every GOAD host (see [SIEM stack](siem-stack.md)).
- On the domain controllers, turn on advanced audit policy: Kerberos service ticket operations
  (4769), Kerberos authentication (4768), directory service changes (5136), and account management.
- Snapshot everything as `goad-clean` before you attack it.

## What it unlocks
The **Windows & AD** and **Red team → AD attack paths** recipes (phases P2–P3) map each GOAD
misconfiguration to the attack, the event IDs it creates, and the fix.
