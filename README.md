
---

# ShodanRecon Suite

**Discover what others missed | Signal > Noise**

ShodanRecon Suite is a lightweight, domain-focused reconnaissance toolkit designed to help bug bounty hunters and security researchers discover **high-value, in-scope subdomains** while eliminating IP and CDN noise.

Built by **Tharooon**.

---

## Features

* Domain-specific Shodan reconnaissance
* High-signal query generation
* Favicon hash pivoting (mmh3)
* ASN and Organization enrichment
* CDN noise reduction
* Strict domain ownership filtering
* Clean outputs (domains only, no raw IPs)

---

## Tools

### QueryProGen

Advanced Shodan query generator that creates domain-specific queries using:

* SSL certificate fields
* HTTP content markers
* ASN and Organization discovery (CDN-filtered)
* Unique favicon hash extraction

Outputs a ready-to-use `queries.txt` file.

---

### ShodanRecon

Domain-safe Shodan reconnaissance engine that:

* Executes all queries from `queries.txt`
* Extracts hostnames from Shodan results
* Filters results to include **only target-owned domains**
* Removes IP-only noise
* Outputs unique, verified subdomains

---

## Repository Structure

```
shodanrecon-suite/
├── querygen/
│   └── queryprogen.py
├── shodanrecon/
│   └── shodanrecon.py
├── requirements.txt
├── README.md
└── LICENSE
```

---

## Installation

```bash
git clone https://github.com/<your-username>/shodanrecon-suite.git
cd shodanrecon-suite
pip3 install -r requirements.txt
```

---

## API Key Setup

This project does not hardcode API keys.

Set your Shodan API key as an environment variable:

```bash
export SHODAN_API_KEY="YOUR_SHODAN_API_KEY"
```

---

## Usage

### Generate Queries

```bash
python3 querygen/queryprogen.py -d tesla.com -o tesla_queries.txt
```

This generates high-signal Shodan queries tailored specifically to the target domain.

---

### Run Shodan Recon

```bash
python3 shodanrecon/shodanrecon.py \
  -d tesla.com \
  -q tesla_queries.txt \
  -o tesla_domains.txt
```

Output contains **only domains that belong to the target**, with duplicates and IP noise removed.

---

## Recommended Post-Recon Workflow

```bash
cat tesla_domains.txt | httpx -status-code -title -tech-detect
```

Then run targeted scans:

```bash
cat tesla_domains.txt | nuclei -severity medium,high,critical
```

---

## Why This Tool Exists

Most Shodan workflows:

* Mix unrelated IPs
* Return CDN customers
* Generate excessive noise

ShodanRecon Suite focuses on:

* Domain ownership validation
* Signal over volume
* Real-world bug bounty usability

---

## Disclaimer

This tool is intended for **authorized security testing only**.
The author is not responsible for misuse or illegal activity.

---

## License

MIT License
© 2026 Tharooon


