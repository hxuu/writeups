```
author: 0xUu
date: Jun 7th, 2024
topic: A brief introduction to research skills for pentesting.
```

# Task 1. Introduction 

```
no answer needed, just read the introduction 
```

# Task 2. Example reasearch question 


*  In the Burp Suite Program that ships with Kali Linux, what mode would you use to manually send a request (often repeating a captured request numerous times)?
```
answer: Repeater

I searched the following: send requests repeatedly burp suite
```


* What hash format are modern Windows login passwords stored in? 
```
answer: NTLM

I searched the following: hash format for windows login password 
```

* What are automated tasks called in Linux?
```
answer: cron jobs

I searched the following: automate tasks in linux
```

* What number base could you use as a shorthand for base 2 (binary)?
```
answer: base 16

I searched: shorthand for base 2 (interestingly found a stackoverflow post about this)
```

* If a password hash starts with $6$, what format is it (Unix variant)?
```
answer: sha512crypt

I searched: hash format and name
```

# Task 3. Vulnerability searching

* What is the CVE for the 2020 Cross-Site Scripting (XSS) vulnerability found in WPForms?
```
CVE-2020-10385

found in exploitdb, or nvd 
```

* There was a Local Privilege Escalation vulnerability found in the Debian version of Apache Tomcat, back in 2016. What's the CVE for this vulnerability? 
```
CVE-2016-1240

searched the following: Local Privilege Escalation vulnerability Debian version of Apache Tomcat cve
```

* What is the very first CVE found in the VLC media player?
```
CVE-2007-0017 

just sort the CVEs by date
```

* If you wanted to exploit a 2020 buffer overflow in the sudo program, which CVE would you use?
```
CVE-2019-18634 
```

# Task 4. Manual pages

* SCP is a tool used to copy files from one computer to another.
What switch would you use to copy an entire directory?
```
-r
```

* fdisk is a command used to view and alter the partitioning scheme used on your hard drive.
What switch would you use to list the current partitions?
```
-l
```

* nano is an easy-to-use text editor for Linux. There are arguably better editors (Vim, being the obvious choice); however, nano is a great one to start with.
What switch would you use to make a backup when opening a file with nano?
```
-B 
```

* Netcat is a basic tool used to manually send and receive network requests. 
What command would you use to start netcat in listen mode, using port 12345?
```
nc -l -p 12345
```

# Task 5. Final thoughts

from thm:
```
Having completed this room, you hopefully now have established the basis of a methodology to tackle research questions that you come across by yourself. The vast majority of rooms on TryHackMe can be solved purely using knowledge found on Google, so please take the opportunity to improve your skills by Googling any problems you come across!
```
