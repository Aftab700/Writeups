# CyberHavoc CTF 2023

https://ctf.cyberhavoc.in/

FLAG FORMAT: `CHCTF{}`


## Challenges

### Reverse Engineering
- [Start The Dos](#Start-The-dos)

### Crypto
- [The Beginning Of All](#The-Beginning-Of-All)
- [Leaked Convo](#Leaked-Convo)

### Digital Forensics
- [The Cryptic Sound](#The-Cryptic-Sound)



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

<br>

### Leaked Convo

given text:
```
duv#r!|"rG Xrr} (|$! %|vpr y|&; Znxr "$!r {| |{r urn!" $";
a(!ryyG N!r (|$ q|{r &v#u (|$! "r#$}L
Yr|{G R%r!(#uv{t v" "r#; aur }n(y|nq" n!r "r#; aur #n!tr#" n!r sv'rq; V#â" w$"# n zn##r! |s #vzr {|&.
duv#r!|"rG aur p|{pr}# |s &nv#v{t or&vyqr!" zr; ]b]T`*>DBlD>g@lD=lBDArDlDb@lWAr,; dr {rrq #| xrr} !|#n#v{t |$! p|{%r!"n#v|{ "| #un# {|#uv{t tr#" yrnxrq;
a(!ryyG [|#rq.
```

It is rot 47 with n=81. and flag is in rot13.

```
flag: CHCTF{175_71M3_70_574r7_7H3_W4r}
```






<br>

--------------------

## Digital Forensics

### The Cryptic Sound

file: [Right or Wrong.wav](https://github.com/Manoj-Mukund/files/blob/main/Right%20or%20Wrong.wav)

it is morse code in audio 

tool used: https://morsecode.world/international/decoder/audio-decoder-adaptive.html

```
flag: CHCTF{BONSOIRELLIOT}
```



