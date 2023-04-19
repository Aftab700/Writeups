# CyberHavoc CTF 2023

https://ctf.cyberhavoc.in/

FLAG FORMAT: `CHCTF{}`


## Challenges

### Reverse Engineering
- [Start The Dos](#Start-The-dos)

### Crypto
- [The Beginning Of All](#The-Beginning-Of-All)



## Reverse Engineering

### Start The Dos

DESCRIPTION :
_Leon wants you to be a part of Agents of Havoc. He wants you to understand this software as old as hacking itself so as to fire a DoS Attack against whiterose's targets. Help him before he suspects your intentions._

file: [dosser.s](https://github.com/Manoj-Mukund/files/raw/main/CyberHavoc/dosser.s)

if look in this assembly code we can see that it is checking characters one by on like this:

```
mov al, [esi]
    cmp al, 0o114
    jne cmp_fail
    inc esi
```

we can get flag by converting all this values we get from assembly `cmp`

python code to do that:

```python
print("CHCTF{", end='')
for i in [0o114, 0o63, 0o63, 0o124, 0o137, 0o103, 0o122, 0o64, 0o103, 0o113, 0o63, 0o122, 0o137, 0o65, 0o124, 0o122, 0o61, 0o113, 0o63, 0o123, 0o137, 0o64, 0o107, 0o64, 0o61, 0o116]:
    print(chr(i), end='')
print("}")
```

```
flag:  CHCTF{L33T_CR4CK3R_5TR1K3S_4G41N}
```

<br>













<br>

-------------------------------------

## Crypto

### The Beginning Of All

DESCRIPTION:

_I was working on my laptop when my laptop suddenly glitched. I discussed it with my friends and to our surprise we all had the same color glitch. I guess it has to do something with the odd behavior of the people around me._

_Remember the flag format!_

file: [glitches.mp4](https://github.com/Manoj-Mukund/files/blob/main/glitches.mp4)

When i first open this file it is just some random frames of color of 3x2 matrix. so i just googled "color code cipher ctf" and got this link:

https://www.dcode.fr/hexahue-cipher

After decoding we get this: `CHCTF5URR3ND3R 0R 5UFF3R`

<!--  char(67)char(72)char(67)char(84)char(70)char(53)char(85)char(82)char(82)char(51)char(78)char(68)char(51)char(82)char(32)char(48)char(82)char(32)char(53)char(85)char(70)char(70)char(51)char(82)  -->

```
flag: CHCTF{5URR3ND3R_0R_5UFF3R}
```




