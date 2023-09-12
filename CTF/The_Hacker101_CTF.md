# The Hacker101 CTF

https://ctf.hacker101.com/ctf

</br>

## Challenges

- [A little something to get you started](#A-little-something-to-get-you-started)
- [Micro-CMS v1](#Micro-CMS-v1)
- [](#)
- [](#)
- [](#)
- [](#)
- [](#)
- [](#)
- [](#)
- [](#)


</br>

## A little something to get you started

In source code we can see one image

<img width="301" alt="image" src="https://github.com/Aftab700/Writeups/assets/79740895/0724ca59-0e68-4dd8-9e00-196460d77d4c">

viewing this image we get the flag

flag: `^FLAG^05f132dbc0e8a0cbb312952e6703e8f4703e921669676a096b385a49b34c94b2$FLAG$`

</br>

## Micro-CMS v1

number of flag: 4

Here we have functionality to create page in that using the payload: `<img src=xx onerror=alert(1)>` will create an alert pop-up and it will give us the first flag in source code.

flag: `^FLAG^94f26fe56dec79812241c348ed6b5718a9e00fc2df643403fef30f6c0e8faee1$FLAG$`



