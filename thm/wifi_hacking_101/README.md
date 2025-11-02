```
author: 0xUu
date: Jun 11th, 2024
topic: Learn to attack WPA(2) networks! Ideally you'll want a smartphone with you for this, preferably one that supports hosting wifi hotspots so you can follow along.
```

# Task 1. The basics - An intro to WPA

* What type of attack on the encryption can you perform on WPA(2) personal?
```
answer: brute force
```

* Can this method be used to attack WPA2-EAP handshakes? (Yea/Nay)
```
answer: Nay

why? The key used in WPA2-EAP is derived from the EAP authentication process, making it much harder to crack compared to pre-shared keys used in WPA2-PSK.
```

* What three letter abbreviation is the technical term for the "wifi code/password/passphrase"?
```
answer: PSK
```

* What's the minimum length of a WPA2 Personal password?
```
answer: 8
```

# Task 2. You're being watched - Capturing packets to attack

We'll want to use aircrack-ng, airodump-ng and airmon-ng to attack WPA networks.


* How do you put the interface “wlan0” into monitor mode with Aircrack tools? (Full command)
```bash
# you have to run it as root
airmon-ng start wlan0
```

* What is the new interface name likely to be after you enable monitor mode?
```
wlan0mon
```

* What do you do if other processes are currently trying to use that network adapter? 
```bash
airmon-ng check kill
```

* What tool from the aircrack-ng suite is used to create a capture?
```
airodump-ng
```

* What flag do you use to set the BSSID to monitor?
```
--bssid
```

* And to set the channel?
```
--channel
```

* And how do you tell it to capture packets to a file?
```
-w
```

# Task 3. Aircrack-ng - Let's get cracking

* What flag do we use to specify a BSSID to attack?
```
-b
```

* What flag do we use to specify a wordlist?
```
-w
```

* How do we create a HCCAPX in order to use hashcat to crack the password?
```
-j

bonus-info 1: An HCCAPX file is a format used by hashcat, a popular password cracking tool, to store the captured WPA/WPA2 handshake along with the EAPOL authentication messages. 

bonus-info 2: EAPOL (Extensible Authentication Protocol over LAN) authentication messages are used in WPA/WPA2-protected Wi-Fi networks to facilitate the authentication and key management process between a client device and an access point. (exchanged during the the 4-way handshake)
```

* Using the rockyou wordlist, crack the password in the attached capture. What's the password?
```
answer: greeneggsandham

command: aircrack-ng -b 02:1A:11:FF:D9:BD -w /usr/share/wordlists/rockyou.txt NinjaJc01
```

* Where is password cracking likely to be fastest, CPU or GPU?
```
GPU
```

