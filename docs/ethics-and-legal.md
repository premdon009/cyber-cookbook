# Ethics & legal

!!! danger "The one rule"
    Only test systems you **own** or have **explicit written permission** to test. Scanning,
    exploiting or accessing a system without authorization is a crime in most countries,
    even if you "didn't break anything".

## What counts as authorization

- **Your own lab:** VMs and containers on your own hardware, on an isolated network.
- **Platforms that invite you:** OverTheWire, picoCTF, PortSwigger Academy, Hack The Box,
  TryHackMe and the others in the [catalog](resources/index.md), within *their* rules and scope.
- **Bug bounty programmes:** only the in-scope assets, following the programme's rules.
- **Work engagements:** a signed contract and rules of engagement (ROE) that state the scope, dates,
  contacts, and what is out of bounds.

Being able to reach a system doesn't make it yours to test. A misconfigured S3 bucket, an open
port, or a found password is **not** permission.

## Lab safety

- Keep vulnerable VMs on **host-only or internal networks**. Never bridge them to your home LAN or the
  internet.
- Real malware (for example the Practical Malware Analysis labs) runs **only** in a dedicated, isolated,
  snapshotted analysis VM with networking off or simulated (INetSim / FakeNet).
- Cloud labs (CloudGoat, flAWS) run in **your own** accounts. Set billing alerts, and destroy them when
  you're done.
- Don't store real credentials, customer data or work data in this repo or your lab.

## What this repo will not contain

To keep it a study resource and not a weapon: no ready-to-run exploit code, malware samples, or
guides to evading real security products. The notes explain *how techniques work*, how to *detect*
them, and point to the public, purpose-built labs where you can practise them.

## Responsible disclosure

If you find a real vulnerability outside a lab, report it to the vendor (look for
`/.well-known/security.txt` or a PSIRT page) or to a national CERT, and give them time to fix
it before you talk about it publicly.
