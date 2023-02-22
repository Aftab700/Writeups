### Prisoner:

_Have you ever broken out of jail ? Maybe it is easier than you think !_

----

After starting the instance we are given ssh creds:
Connect with:
# Password is "userpass"
ssh -p 32233 user@challenge.nahamcon.com
It turns out that the shell dropped us into a running python terminal. This can exit the python interpreter with the CTRL + D keys.
then,we run some basic python to attain command execution and get the flag
