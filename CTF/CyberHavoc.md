# CyberHavoc CTF 2023

https://ctf.cyberhavoc.in/

FLAG FORMAT: `CHCTF{}`


## Challenges

### Reverse Engineering
- [Start The Dos](#Start-The-dos)



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








