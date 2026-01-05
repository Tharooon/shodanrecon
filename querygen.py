#!/usr/bin/env python3
import os
import sys
import argparse
import shodan
import requests
import mmh3
import codecs
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

BANNER = r"""
 ██████╗ ██╗   ██╗███████╗██████╗ ██╗   ██╗
██╔═══██╗██║   ██║██╔════╝██╔══██╗╚██╗ ██╔╝
██║   ██║██║   ██║█████╗  ██████╔╝ ╚████╔╝
██║▄▄ ██║██║   ██║██╔══╝  ██╔══██╗  ╚██╔╝
╚██████╔╝╚██████╔╝███████╗██║  ██║   ██║
 ╚══▀▀═╝  ╚═════╝ ╚══════╝╚═╝  ╚═╝   ╚═╝

        QueryProGen by Tharooon
"""

SHODAN_API_KEY = os.getenv("SHODAN_API_KEY")

def get_favicon_hash(domain):
    try:
        r = requests.get(f"https://{domain}/favicon.ico", timeout=10, verify=False)
        if r.status_code == 200 and r.content:
            return mmh3.hash(codecs.encode(r.content, "base64"))
    except:
        pass
    return None

def get_real_infra(api, domain):
    orgs, asns = [], []
    query = f'hostname:"{domain}" -org:"Akamai" -org:"Cloudflare" -org:"Amazon"'
    try:
        res = api.count(query, facets=["org", "asn"])
        orgs = [o["value"] for o in res.get("facets", {}).get("org", [])][:2]
        asns = [a["value"] for a in res.get("facets", {}).get("asn", [])][:2]
    except:
        pass
    return orgs, asns

def main():
    print(BANNER)
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--domain", required=True)
    parser.add_argument("-o", "--output", default="queries.txt")
    args = parser.parse_args()

    if not SHODAN_API_KEY:
        print("[-] SHODAN_API_KEY not set")
        sys.exit(1)

    api = shodan.Shodan(SHODAN_API_KEY)
    queries = set()

    queries.add(f'hostname:"{args.domain}"')
    queries.add(f'ssl.cert.subject.cn:"{args.domain}"')
    queries.add(f'http.title:"{args.domain}"')

    orgs, asns = get_real_infra(api, args.domain)
    for org in orgs: queries.add(f'org:"{org}"')
    for asn in asns: queries.add(f'asn:{asn}')

    favicon = get_favicon_hash(args.domain)
    if favicon:
        queries.add(f"http.favicon.hash:{favicon}")
        queries.add(f"http.favicon.hash:{favicon} hostname:\"{args.domain}\"")

    with open(args.output, "w") as f:
        for q in sorted(queries):
            f.write(q + "\n")

    print(f"[✓] {len(queries)} queries written to {args.output}")

if __name__ == "__main__":
    main()
