```
author: 0xUu
date: July 12th, 2024
topic: Exploiting blind SQL injection using out-of-band (OAST) techniques
```


# Lab: Blind SQL injection with out-of-band interaction

This lab contains a blind SQL injection vulnerability. The application uses a tracking cookie for analytics, and performs a SQL query containing the value of the submitted cookie.

The SQL query is executed asynchronously and has no effect on the application's response. However, you can trigger out-of-band interactions with an external domain.

To solve the lab, exploit the SQL injection vulnerability to cause a DNS lookup to Burp Collaborator.

## Solution

Due to this note:

```
To prevent the Academy platform being used to attack third parties, our firewall blocks interactions between the labs and arbitrary external systems. To solve the lab, you must use Burp Collaborator's default public server.
```

We can't solve the lab, but the method to do so is in script `oast1.py`

As for the next lab, exfiltrating data is as easy as making a SELECT statement, and just appending that to the front of the domain we control
