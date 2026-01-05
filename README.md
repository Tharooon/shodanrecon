
# ShodanRecon Suite

**Discover what others missed | Signal > Noise**

A domain-focused Shodan recon suite built for **bug bounty hunters, red teamers, and security researchers** to discover **untouched, high-value subdomains** while eliminating IP and CDN noise.

Built by **Tharooon**.

---

## ✨ Features

* 🎯 Domain-specific Shodan recon
* 🧠 High-signal query generation
* 🧩 Favicon hash pivoting (mmh3)
* 🏗 ASN & Organization enrichment
* 🛡 CDN noise reduction
* 📛 Strict domain ownership filtering
* 📄 Clean outputs (domains only, no IP junk)

---

## 🧰 Tools Included

### 1️⃣ QueryProGen

**Advanced Shodan query generator**

Generates high-quality, domain-specific Shodan queries using:

* SSL certificate fields
* HTTP content markers
* ASN & Organization discovery (CDN-filtered)
* Unique favicon hash extraction

Output is a ready-to-use `queries.txt` file for Shodan hunting.

---

### 2️⃣ ShodanRecon

**Domain-safe Shodan recon engine**

* Executes all queries from `queries.txt`
* Extracts hostnames from Shodan results
* Filters results to include **only in-scope domains**
* Removes raw IP noise
* Outputs **unique, verified subdomains**

---

## 📂 Repository Structure

```
shodanrecon-suite/
├── querygen/
│   ├── queryprogen.py
│   └── examples/
│       └── tesla_queries.txt
│
├── shodanrecon/
│   ├── shodanrecon.py
│   └── examples/
│       └── tesla_domains.txt
│
├── requirements.txt
├── README.md
└── LICENSE
```

---

## ⚙️ Installation

```bash
git clone https://github.com/<your-username>/shodanrecon-suite.git
cd shodanrecon-suite
pip3 install -r requirements.txt
```

---

## 🔑 API Key Setup

This project **never hardcodes API keys**.

Set your Shodan API key as an environment variable:

```bash
export SHODAN_API_KEY="YOUR_SHODAN_API_KEY"
```

---

## 🚀 Usage

### Generate Shodan Queries

```bash
python3 querygen/queryprogen.py -d tesla.com -o tesla_queries.txt
```

Example output:

```
asn:AS16625
org:"Akamai Technologies, Inc."
http.favicon.hash:-1166125415
ssl.cert.subject.cn:"tesla.com"
```

---

### Run Shodan Recon

```bash
python3 shodanrecon/shodanrecon.py \
  -d tesla.com \
  -q tesla_queries.txt \
  -o tesla_domains.txt
```

Example output:

```
bettertime-stage.tesla.com
serviceapp.tesla.com
akamai-apigateway-vehicleextinfogw-prdsvc-st.tesla.com
```

---

## 🔍 Post-Recon Workflow (Recommended)

```bash
cat tesla_domains.txt | httpx -status-code -title -tech-detect
```

Then:

```bash
cat tesla_domains.txt | nuclei -severity medium,high,critical
```

---

## 🧠 How This Is Different

* ❌ No random IP dumping
* ❌ No unrelated CDN customers
* ❌ No bloated queries
* ✅ Only domains that **belong to your target**
* ✅ Designed for **real-world bug bounty**

---

## ⚠️ Disclaimer

This tool is intended for **authorized security testing only**.
The author is **not responsible for misuse** or illegal activity.

---

## 📜 License

MIT License
© 2026 Tharooon

---


