### Prisoner:

_Have you ever broken out of jail ? Maybe it is easier than you think !_

----

After starting the instance we are given ssh creds:

Connect with:

Password is _"userpass"_

```
ssh -p 32233 user@challenge.nahamcon.com
```

It turns out that the shell dropped us into a running python terminal. This can exit the python interpreter with the CTRL + D keys.
then,we run some basic python to attain command execution and get the flag

![image](https://user-images.githubusercontent.com/79740895/220685652-3a7304a1-e937-46e2-93b8-f581ee5e861b.png)

```
flag{c31e05a24493a202fad0d1a827103642}
```
