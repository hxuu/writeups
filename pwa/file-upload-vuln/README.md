```
author: 0xUu
topic: file upload vulnerabilities
date: August 8th, 2024
```

This README.md file is just an overview of what will be learned. It's in my own words (for learning purposes)

---

# What are file upload vulnerabilities?

File upload vulnerabilities are when a web server allows users to upload files to its filesystem without sufficiently validating things like their name, type, contents, or size. Failing to properly enforce restrictions on these could mean that even a basic image upload function can be used to upload arbitrary and potentially dangerous files instead. This could even include server-side script files that enable remote code execution.

In some cases, the act of uploading the file is in itself enough to cause damage. Other attacks may involve a follow-up HTTP request for the file, typically to trigger its execution by the server.


# What is the impact of file upload vulnerabilities?

The impact of file upload vulnerabilities generally depends on two key factors:

Which aspect of the file the website fails to validate properly, whether that be its size, type, contents, and so on.
What restrictions are imposed on the file once it has been successfully uploaded.
In the worst case scenario, the file's type isn't validated properly, and the server configuration allows certain types of file (such as .php and .jsp) to be executed as code. In this case, an attacker could potentially upload a server-side code file that functions as a web shell, effectively granting them full control over the server.

If the filename isn't validated properly, this could allow an attacker to overwrite critical files simply by uploading a file with the same name. If the server is also vulnerable to directory traversal, this could mean attackers are even able to upload files to unanticipated locations.

Failing to make sure that the size of the file falls within expected thresholds could also enable a form of denial-of-service (DoS) attack, whereby the attacker fills the available disk space.

---

Enjoy the labs...

