# Hypervisor & network

**Level:** L0 · **Goal:** an isolated network where an attacker VM, a Linux VM and a Windows VM
can reach each other, but nothing in the lab can reach your home LAN or the internet.

## 1. Pick a hypervisor (all free)

| Hypervisor | Good for | Notes |
|---|---|---|
| **VirtualBox** | Beginners, any OS | Free, open source. GOAD supports it. |
| **VMware Workstation Pro** | Windows / Linux desktops | Free for personal use. Snapshots and networking are solid. GOAD supports it. |
| **Proxmox VE** | A spare PC or server | Bare-metal, web UI, best for a permanent lab. Ludus automates ranges on it. |
| **Hyper-V** | Windows Pro/Enterprise hosts | Built in; works alongside WSL2 with no conflicts. |

!!! note "Windows host running WSL2 / Hyper-V"
    WSL2 turns on the Hyper-V platform. Recent VirtualBox and VMware Workstation versions run on
    top of it, but more slowly. If VMs feel sluggish, use Hyper-V directly for the lab, or a separate
    Proxmox box.

## 2. Networks

Create two virtual networks:

| Network | Type | CIDR | Used by |
|---|---|---|---|
| `lab` | host-only / internal | `10.10.10.0/24` | every lab VM |
| `nat-updates` | NAT | hypervisor default | attacker VM only, switched on just for updates |

Optional: add an **OPNsense** or **pfSense** VM with one leg on each network, to practise firewall
rules, control egress and capture traffic. This becomes the network-monitoring tap later (Zeek/Suricata).

## 3. Base VMs

| VM | Get it | vCPU / RAM | Network |
|---|---|---|---|
| Kali Linux | kali.org prebuilt VM images | 2 / 4 GB | `lab` (+ `nat-updates` when updating) |
| Ubuntu Server LTS | ubuntu.com | 2 / 2 GB | `lab` |
| Windows 11 Enterprise eval | Microsoft Evaluation Center | 2 / 4 GB | `lab` |

## 4. Verify isolation

=== "Linux VM"

    ```bash
    ip -br addr                 # expect 10.10.10.x
    ping -c2 10.10.10.<win-ip>  # lab traffic works
    ping -c2 1.1.1.1            # must FAIL
    ```

=== "Windows VM"

    ```powershell
    Get-NetIPAddress -AddressFamily IPv4 | Select InterfaceAlias, IPAddress
    Test-NetConnection 10.10.10.<linux-ip>       # works
    Test-NetConnection 1.1.1.1 -Port 443         # must FAIL
    ```

Then **snapshot all three VMs** as `clean-base`.

## Check yourself
1. Why is a bridged adapter dangerous for a vulnerable VM?
2. What is the difference between host-only and NAT networking?
3. Why does the attacker get temporary NAT access but the targets don't?
