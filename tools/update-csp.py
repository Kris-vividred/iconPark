#!/usr/bin/env python3
"""Refresh the script hashes in index.html's Content-Security-Policy.

The CSP only allows inline <script> blocks whose SHA-256 hash it lists, so any edit to a
<script> in index.html must be followed by:  python3 tools/update-csp.py
(--check only verifies, exits 1 if the hashes are stale; handy before a commit or push.)
"""
import base64, hashlib, pathlib, re, sys

page = pathlib.Path(__file__).resolve().parent.parent / 'index.html'
html = page.read_text(encoding='utf-8')
scripts = re.findall(r'<script>(.*?)</script>', html, re.S)
hashes = ' '.join("'sha256-%s'" % base64.b64encode(hashlib.sha256(s.encode('utf-8')).digest()).decode()
                  for s in scripts)
m = re.search(r"script-src [^;]*;", html)
if not m:
    sys.exit('no script-src directive found in index.html')
new = f"script-src {hashes};"
if '--check' in sys.argv:
    ok = m.group(0) == new
    print('CSP script hashes are up to date' if ok else 'CSP script hashes are STALE: run python3 tools/update-csp.py')
    sys.exit(0 if ok else 1)
page.write_text(html.replace(m.group(0), new, 1), encoding='utf-8')
print(f'{len(scripts)} inline scripts hashed')
