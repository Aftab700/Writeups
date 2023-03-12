## Easy Peasy

Tags: `picoCTF 2021`, `cryptography`


Description:

_A one-time pad is unbreakable, but can you manage to recover the flag? (Wrap with picoCTF{})._
`nc mercury.picoctf.net 36449`


<details><summary markdown="span">Click to see code otp.py :diamond_shape_with_a_dot_inside: </summary>

```python
#!/usr/bin/python3 -u
import os.path
KEY_FILE = "key"
KEY_LEN = 50000
FLAG_FILE = "flag"


def startup(key_location):
	flag = open(FLAG_FILE).read()
	kf = open(KEY_FILE, "rb").read()

	start = key_location
	stop = key_location + len(flag)

	key = kf[start:stop]
	key_location = stop

	result = list(map(lambda p, k: "{:02x}".format(ord(p) ^ k), flag, key))
	print("This is the encrypted flag!\n{}\n".format("".join(result)))

	return key_location

def encrypt(key_location):
	ui = input("What data would you like to encrypt? ").rstrip()
	if len(ui) == 0 or len(ui) > KEY_LEN:
		return -1

	start = key_location
	stop = key_location + len(ui)

	kf = open(KEY_FILE, "rb").read()

	if stop >= KEY_LEN:
		stop = stop % KEY_LEN
		key = kf[start:] + kf[:stop]
	else:
		key = kf[start:stop]
	key_location = stop

	result = list(map(lambda p, k: "{:02x}".format(ord(p) ^ k), ui, key))

	print("Here ya go!\n{}\n".format("".join(result)))

	return key_location


print("******************Welcome to our OTP implementation!******************")
c = startup(0)
while c >= 0:
	c = encrypt(c)
```
</details>

<br>

one-time pad is unbreakable only if you don't use the same key twice. this code is like sliding window next message is encrypted from the end of last messages length in key file and we can find the loop hole in this part of the code.
```python
if stop >= KEY_LEN:
	stop = stop % KEY_LEN
	key = kf[start:] + kf[:stop]
```
If length is greater than key it will start from zero so we can encrypt our message with same key used to encrypt flag and we are given the encrypted flag. To make stop = 0
`length of message = length of key – length of flag`

`length of key = 50000`

`length of flag = (encrypted flag/2)`

`encrypted flag = flag xor key`

`encrypted message = (known message) xor key`

so we can find key with,

`key = (known message) xor (encrypted message)`

and `flag = (encrypted flag) xor key`

here is python script to find flag:

<details><summary markdown="span">Click to see code :diamond_shape_with_a_dot_inside: </summary>
<!-- {::options parse_block_html="false" /}  -->

```python
from Crypto.Util.number import long_to_bytes
from pwn import *
conn = remote('mercury.picoctf.net', 36449)
conn.recvuntil("This is the encrypted flag!\n".encode())
encrypted_flag = str(conn.recvline(), "ascii").strip()
flag_len = int(len(encrypted_flag)/2)
padding = "a" * (50000 - flag_len)
conn.sendlineafter("What data would you like to encrypt?".encode(), padding.encode())
message = "a" * flag_len
conn.sendlineafter("What data would you like to encrypt?".encode(), message.encode())
conn.recvuntil("Here ya go!\n".encode())
encrypted_message = str(conn.recvline(), "ascii").strip()
key = xor(long_to_bytes(int("0x" + encrypted_message, 16)), message.encode())
flag = xor(long_to_bytes(int("0x" + encrypted_flag, 16)), key).decode()
print(f"Flag: picoCTF{{{flag}}}")
conn.close()

```
<!-- {::options parse_block_html="true" /}  -->
</details>

<br>

```
flag: picoCTF{75302b38697a8717f0faee9c0fd36a57}
```

