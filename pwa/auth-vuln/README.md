```
author: 0xUu
date: July 16th, 2024
topic: authentication vulnerabilities
```

Friendly note for those who read this: It's been three or four days since I actively
solved a lab on portswigger, I finished SQLi, and had some time playing valorant.

I AM NOT EVEN BRONZE RANK. Willing to get better though, let's get to work now.


# Lab: Username enumeration via subtly different responses

This lab is subtly vulnerable to username enumeration and password brute-force attacks. It has an account with a predictable username and password, which can be found in the following wordlists:

* Candidate usernames
* Candidate passwords

To solve the lab, enumerate a valid username, brute-force this user's password, then access their account page.

## Solution


