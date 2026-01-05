#!/usr/bin/env python3
import os
import shodan
import argparse

BANNER = r"""
███████╗██╗  ██╗ ██████╗ ██████╗  █████╗ ███╗   ██╗
██╔════╝██║  ██║██╔═══██╗██╔══██╗██╔══██╗████╗  ██║
███████╗███████║██║   ██║██║  ██║███████║██╔██╗ ██║
╚════██║██╔══██║██║   ██║██║  ██║██╔══██║██║╚██╗██║
███████║██║  ██║╚██████╔╝██████╔╝██║  ██║██║ ╚████║
╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝

        shodanrecon by Tharooon
"""

SHODAN_API_KEY = os.getenv("SHODAN_API_KEY")

def belongs(domain, target):
    return domain == target or domain.endswith("." + target)

def main():
    print(BANNER)

    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--domain", required=True)
    parser.add_argument("-q", "--queries", required=True)
    parser.add_argument("-o", "--output", default="domains.txt")
    args = parser.parse_args()

    if not SHODAN_API_KEY:
        print("[-] SHODAN_API_KEY not set")
        return

    api = shodan.Shodan(SHODAN_API_KEY)
    domains = set()

    with open(args.queries) as f:
        queries = [q.strip() for q in f if q.strip()]

    for q in queries:
        print(f"[+] Running query: {q}")
        try:
            res = api.search(q, limit=100)
            for host in res.get("matches", []):
                for h in host.get("hostnames", []):
                    if belongs(h, args.domain):
                        domains.add(h)
        except:
            continue

    with open(args.output, "w") as f:
        for d in sorted(domains):
            f.write(d + "\n")

    print(f"[✓] Unique domains found: {len(domains)}")
    print(f"[✓] Output saved to: {args.output}")

if __name__ == "__main__":
    main()
