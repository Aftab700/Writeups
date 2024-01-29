# The Hacker101 CTF

https://ctf.hacker101.com/ctf

<br />

## Challenges

- [A little something to get you started](#A-little-something-to-get-you-started)
- [Micro-CMS v1](#Micro-CMS-v1)
- [Photo Gallery](#Photo-Gallery)
- [](#)
- [](#)
- [](#)
- [](#)
- [](#)
- [](#)
- [](#)


<br />

## A little something to get you started

In source code we can see one image

<img width="301" alt="image" src="https://github.com/Aftab700/Writeups/assets/79740895/0724ca59-0e68-4dd8-9e00-196460d77d4c">

viewing this image we get the flag

flag: `^FLAG^05f132dbc0e8a0cbb312952e6703e8f4703e921669676a096b385a49b34c94b2$FLAG$`

<br />

## Micro-CMS v1

number of flag: 4

Here we have functionality to create page in that using the payload: `<img src=xx onerror=alert(1)>` in body will create an alert pop-up and it will give us the first flag in source code, and using this same payload in title will give us the second flag but it will be executed in home page.

Flag 1: `^FLAG^94f26fe56dec79812241c348ed6b5718a9e00fc2df643403fef30f6c0e8faee1$FLAG$`

Flag 2: `^FLAG^bd75d9a3aba5709358c413cd1f69819783524094e15dd117c569bdb9f0006a06$FLAG$`

## Photo Gallery

- SQLi in `https://6b6c2ec7bb58b712c873fbbd19cd1a32.ctf.hacker101.com/fetch?id=1`
- File read via SQLi `https://6b6c2ec7bb58b712c873fbbd19cd1a32.ctf.hacker101.com/fetch?id=4+UNION+SELECT+'main.py'--`
- RCE via modifying `filename` column in `photos` table



