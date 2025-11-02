```
author: 0xUu
date: July 6th, 2024
topic: SQL injection - pwa
```


# Lab: SQL injection UNION attack, determining the number of columns returned by the query

This lab contains a SQL injection vulnerability in the product category filter. The results from the query are returned in the application's response, so you can use a UNION attack to retrieve data from other tables. The first step of such an attack is to determine the number of columns that are being returned by the query. You will then use this technique in subsequent labs to construct the full attack.

To solve the lab, determine the number of columns returned by the query by performing a SQL injection UNION attack that returns an additional row containing null values.

## Solution

the script I used is in `union-attack1.py`. Burpsuite needed another jdk version
which I didn't bother downloading, so I just used the requests module to make a request
to the url of the lab, open dev tools, see which requests are related to the category
where the vulnerability is mentioned, broke that down and tested how many columns
are present using `ORDER BY <number-of-column>--`, found that `category=Gifts`
contains **THREE** categories, I then solved the lab using the following injection:

```
<base-url>/filter?category=Gifts%27+UNION+SELECT+NULL%2C+NULL%2C+NULL--
```

# Lab: SQL injection UNION attack, finding a column containing text

This lab contains a SQL injection vulnerability in the product category filter. The results from the query are returned in the application's response, so you can use a UNION attack to retrieve data from other tables. To construct such an attack, you first need to determine the number of columns returned by the query. You can do this using a technique you learned in a previous lab. The next step is to identify a column that is compatible with string data.

The lab will provide a random value that you need to make appear within the query results. To solve the lab, perform a SQL injection UNION attack that returns an additional row containing the value provided. This technique helps you determine which columns are compatible with string data.

## Solution

the script I used is in `union-attack2.py`. I found the number of columns using
`UNION SELECT NULL--`. Note that some db management systems, oracle for example
require a proper `FROM <TABLE>` when using Selects. You can use a dummy table for that.

I automated the search for the position of the column that is compatible with the type string,
and just retrieved the required string from the query


# Lab: SQL injection UNION attack, retrieving data from other tables

This lab contains a SQL injection vulnerability in the product category filter. The results from the query are returned in the application's response, so you can use a UNION attack to retrieve data from other tables. To construct such an attack, you need to combine some of the techniques you learned in previous labs.

The database contains a different table called users, with columns called username and password.

To solve the lab, perform a SQL injection UNION attack that retrieves all usernames and passwords, and use the information to log in as the administrator user.

## Solution

the script I used is in `union-attack3.py`, it should be self-explanatory,
the technique is to just combine what we learned in the previous two labs


# Lab: SQL injection UNION attack, retrieving multiple values in a single column

This lab contains a SQL injection vulnerability in the product category filter. The results from the query are returned in the application's response so you can use a UNION attack to retrieve data from other tables.

The database contains a different table called users, with columns called username and password.

To solve the lab, perform a SQL injection UNION attack that retrieves all usernames and passwords, and use the information to log in as the administrator user.

## Solution

The script is in `union-attack4.py`, you'll find the explanation there.


# Lab: SQL injection attack, querying the database type and version on MySQL and Microsoft

This lab contains a SQL injection vulnerability in the product category filter. You can use a UNION attack to retrieve the results from an injected query.

To solve the lab, display the database version string.

## Solution

the script is in `union-attack5.py`, instead of making the comment using `--`,
we use `#`. The rest of the code is self-explanatory.


# Lab: SQL injection attack, listing the database contents on non-Oracle databases

This lab contains a SQL injection vulnerability in the product category filter. The results from the query are returned in the application's response so you can use a UNION attack to retrieve data from other tables.

The application has a login function, and the database contains a table that holds usernames and passwords. You need to determine the name of this table and the columns it contains, then retrieve the contents of the table to obtain the username and password of all users.

To solve the lab, log in as the administrator user.

## Solution

The script is in `union-attack6.py`, this one was actually fun.
