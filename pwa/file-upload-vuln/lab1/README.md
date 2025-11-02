```
author: 0xUu
date: Jun 10th, 2024
topic: file upload vulnerability (portswigger academy)
```

# Basics of php (personal use)

PHP (Hypertext Preprocessor) is a widely-used, open-source server-side scripting language primarily designed for web development. It was created by Rasmus Lerdorf in 1994 and has since evolved into a powerful tool for creating dynamic web pages and web applications. PHP scripts are executed on the server, generating HTML which is then sent to the client's web browser.

We'll use it as a scripting language to run an exploit on the server.

# The idea

File upload vulnerabilities are when a web server allows users to upload files to its filesystem without sufficiently validating things like their name, type, contents, or size. Failing to properly enforce restrictions on these could mean that even a basic image upload function can be used to upload arbitrary and potentially dangerous files instead. This could even include server-side script files that enable remote code execution.


# LAB1 - Remote code execution via web shell upload 

I first tried to upload a normal image to the server. I was met with a success reponse, then created a simple php script that read the contents of the flag

```php
<?php echo file_get_contents('/home/carlos/secret'); ?> 
```

Uploading the file normally, I then use burp proxy to intercept traffic to my-account. I found that we make a GET request to `/files/avatars/OUR-FILES`. I sent this request to burp repeater and got the flag


---

flag: `i4ym39xKQ77CEaRi0LvIqCeGABOjf8Sp`


# LAB2 - Web shell upload via Content-Type restriction bypass

This lab contains a vulnerable image upload function. It attempts to prevent users from uploading unexpected file types, but relies on checking user-controllable input to verify this.

Here, we just change the `Content-Type` header in the POST request to match the allowed content type.

---

flag: `YakMIXfWInuaOwIup9UuVbcU13iPmhII`
