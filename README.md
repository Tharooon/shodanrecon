# shodanrecon
**Discover subdomains what others missed | Signal > Noise**
# ShodanRecon Suite

**Discover what others missed | Signal > Noise**

A lightweight Shodan-based recon suite to:
- Generate high-quality Shodan queries per domain
- Extract unique, in-scope subdomains
- Reduce CDN and IP noise

Built for bug bounty hunters and red teamers.

---

## Tools

### 1️⃣ QueryGen
Generate domain-specific Shodan queries (ASN, favicon, certs, org, etc.)

### 2️⃣ ShodanRecon
Run queries against Shodan and extract **only valid subdomains**
belonging to the target domain.

---

## Installation

```bash
git clone https://github.com/<your-username>/shodanrecon-suite.git
cd shodanrecon-suite
pip3 install -r requirements.txt
