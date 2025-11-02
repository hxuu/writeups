# THM - Further Nmap

```
author: 0xUu
date: Jun 2nd, 2024
topic: nmap (network mapper)
```

*If you want to follow along with the write-up, make sure you deploy the machine and run `export IP=<ip-addr-given>` *

This contains the answers to the task questions. the room is a walkthrough, so details **are** on thm.

## Task 11 - Working with the NSE

* What optional argument can the ftp-anon.nse script take?
```
answer: maxlist

bonus-info: The maximum number of files to return in the directory listing. By default it is 20, or unlimited if verbosity is enabled. Use a negative number to disable the limit, or 0 to disable the listing entirely.
```

## Task 12 - Searching for scripts

* Search for "smb" scripts in the `/usr/share/nmap/scripts/` directory using either of the demonstrated methods.
What is the filename of the script which *determines the underlying OS of the SMB server?*
```
answer: smb-os-discovery.nse
```

* Read through this script. What does it depend on?
```
answer: smb-brute

bonus-info: This script is specifically targeted towards security auditors or penetration testers. One example of its use, suggested by Brandon Enright, was hooking up smb-brute.nse to the database of usernames and passwords used by the Conficker worm (the password list). Then, the network is scanned and all systems that would be infected by Conficker are discovered.
```

## Task 13 - Firewall evasion 

* Which simple (and frequently relied upon) protocol is often blocked, requiring the use of the -Pn switch?
```
answer: ICMP
```

* **[Research]** Which Nmap switch allows you to append an arbitrary length of random data to the end of packets?
```
answer: --data-length

bonus-info: By appending random data, you can alter the packet size and content, making it more difficult for many IDS/IPS systems to match the packet to known scanning signatures.
```

## Task 14 - Practical 

* Does the target ip respond to ICMP echo (ping) requests (Y/N)?
```
answer: N
```

* Perform an Xmas scan on the first 999 ports of the target -- how many ports are shown to be open or filtered?
```bash
## answer: 999

sudo nmap -Pn -sX -p 1-999 $IP -vv 
```

There is a reason given for this -- what is it?

Note: The answer will be in your scan results. Think carefully about which switches to use -- and read the hint before asking for help!
```
answer: no response
```

* Perform a TCP SYN scan on the first 5000 ports of the target -- how many ports are shown to be open?
```bash
## answer: 5
```

* Open Wireshark (see Cryillic's Wireshark Room for instructions) and perform a TCP Connect scan against port 80 on the target, monitoring the results. Make sure you understand what's going on. Deploy the ftp-anon script against the box. Can Nmap login successfully to the FTP server on port 21? (Y/N)
```
Y

bonus-info: open wireshark and capture packets on the tun0 interface, run nmap and watch for the packets sent.
```