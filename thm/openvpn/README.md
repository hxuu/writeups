```
author: 0xUu
date: Jun 7th, 2024
topic: A guide to connecting to our network using OpenVPN.
```

# pre-requisites

```
what is a vpn?

A Virtual Private Network is a way to create a secure "tunnel" between two networks. For example, you use a VPN on TryHackMe to access the private network on which the machines operate. VPNs are also commonly used for an employee to log into their workplace when they are not on site (such as working from home or travelling for business matters). VPNs are also used where networks (such as coffee shops) do not provide encryption, and are a great way of preventing others from reading your network traffic.
```

## How to connect to thm private network using openvpn

```bash
sudo apt install openvpn

# locate the config file
sudo openvpn ../0xUu.ovpn

# and that's it!
```

### What is the flag displayed on the deployed machine's website?

```
flag{connection_verified}
```
