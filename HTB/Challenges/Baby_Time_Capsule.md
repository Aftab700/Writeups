
## Baby Time Capsule

`EASY` , `Crypto`

DESCRIPTION: _Qubit Enterprises is a new company touting it's propriety method of qubit stabilization._
_They expect to be able to build a quantum computer that can factor a RSA-1024 number in the next 10 years._
_As a promotion they are giving out "time capsules" which contain a message for the future encrypted by 1024 bit RSA._ 
_They might be great engineers, but they certainly aren't cryptographers, can you find a way to read the_ 
_message without having to wait for their futuristic machine?_

https://app.hackthebox.com/challenges/365

--------

Baby Time Capsule is cryptography challenge. we are given with python source code server.py file.

<details><summary markdown="span">Click to see source code :diamond_shape_with_a_dot_inside: </summary>
  

```python
from Crypto.Util.number import bytes_to_long, getPrime
import socketserver
import json

FLAG = b'HTB{--REDACTED--}'


class TimeCapsule():

    def __init__(self, msg):
        self.msg = msg
        self.bit_size = 1024
        self.e = 5

    def _get_new_pubkey(self):
        while True:
            p = getPrime(self.bit_size // 2)
            q = getPrime(self.bit_size // 2)
            n = p * q
            phi = (p - 1) * (q - 1)
            try:
                pow(self.e, -1, phi)
                break
            except ValueError:
                pass

        return n, self.e

    def get_new_time_capsule(self):
        n, e = self._get_new_pubkey()
        m = bytes_to_long(self.msg)
        m = pow(m, e, n)

        return {"time_capsule": f"{m:X}", "pubkey": [f"{n:X}", f"{e:X}"]}


def challenge(req):
    time_capsule = TimeCapsule(FLAG)
    while True:
        try:
            req.sendall(
                b'Welcome to Qubit Enterprises. Would you like your own time capsule? (Y/n) '
            )
            msg = req.recv(4096).decode().strip().upper()
            if msg == 'Y' or msg == 'YES':
                capsule = time_capsule.get_new_time_capsule()
                req.sendall(json.dumps(capsule).encode() + b'\n')
            elif msg == 'N' or msg == "NO":
                req.sendall(b'Thank you, take care\n')
                break
            else:
                req.sendall(b'I\'m sorry I don\'t understand\n')
        except:
            # Socket closed, bail
            return


class MyTCPRequestHandler(socketserver.BaseRequestHandler):

    def handle(self):
        req = self.request
        challenge(req)


class ThreadingTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass


def main():
    socketserver.TCPServer.allow_reuse_address = True
    server = ThreadingTCPServer(("0.0.0.0", 1337), MyTCPRequestHandler)
    server.serve_forever()


if __name__ == '__main__':
    main()

```

</details>
  

To solve this we need knowledge of the Chinese remainder theorem.

m=message, e=5, n=public key, c=cipher text

m<sup>e</sup> mod n = c

let's take x = m<sup>e</sup>

x mod n = c

here x module n is remainder c, so we can say that x anc c are congruent modulo.

x ≡ c (mod n)

Here server encrypt same message with different public keys.

x ≡ c1 (mod n1)

x ≡ c2 (mod n2)

x ≡ c3 (mod n3)

The Chinese Remainder Theorem (CRT) is used to solve a set of different 
congruent equations with one variable but different moduli which are relatively
prime.

To find x:

x = (c1 <span>&#215;</span> N1 <span>&#215;</span> N1<sup>-1</sup> + c2 <span>&#215;</span> N2 <span>&#215;</span> N2<sup>-1</sup> + 
c3 <span>&#215;</span> N3 <span>&#215;</span> N3<sup>-1</sup>) mod N

here, N = n1 <span>&#215;</span> n2 <span>&#215;</span> n3

N1 = N / n1

N2 = N / n2

N3 = N / n3

N1 <span>&#215;</span> N1<sup>-1</sup> = 1 mod n1

N2 <span>&#215;</span> N2<sup>-1</sup> = 1 mod n2

N3 <span>&#215;</span> N3<sup>-1</sup> = 1 mod n3

we can use extended euclidean algorithm to find N1<sup>-1</sup>.


I used python library to perform CRT.


Python code:

<details><summary markdown="span">Click to see python code :diamond_shape_with_a_dot_inside: </summary>
  

```python
import json
from Crypto.Util.number import long_to_bytes
from pwn import *
from sympy.ntheory.modular import crt
from sympy.simplify.simplify import nthroot

conn = remote('209.97.185.157', 32141)
rem = list()
num = list()
for i in range(3):
    conn.sendline(b'Y')
    a = conn.recvline()
    r = json.loads(a[74:-1].decode())
    m = r['time_capsule']
    n = r['pubkey'][0]
    e = 5
    m = int(m, 16)
    n = int(n, 16)
    rem.append(m)
    num.append(n)

x = crt(num, rem, check=True)
# print(f'x = {x[0]}')
flag = nthroot(x[0], 5)
print(flag)
print(long_to_bytes(flag))

conn.sendline(b'N')
conn.recvline()
conn.close()
```
  
</details>
  
<details><summary markdown="span">Click to see output :diamond_shape_with_a_dot_inside: </summary>
  

```shell
[x] Opening connection to 209.97.185.157 on port 32141
[x] Opening connection to 209.97.185.157 on port 32141: Trying 209.97.185.157
[+] Opening connection to 209.97.185.157 on port 32141: Done
3133512701921564926666059129802238375015291423590355094862405004229914481893581069974415008616334994674940586670768933862016098685
b'HTB{t3h_FuTUr3_15_bR1ghT_1_H0p3_y0uR3_W34r1nG_5h4d35!}'
[*] Closed connection to 209.97.185.157 port 32141

Process finished with exit code 0

```
  
</details>
  
flag= HTB{t3h_FuTUr3_15_bR1ghT_1_H0p3_y0uR3_W34r1nG_5h4d35!}
