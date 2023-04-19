# CyberHavoc CTF 2023

https://ctf.cyberhavoc.in/

FLAG FORMAT: `CHCTF{}`


## Challenges

### Reverse Engineering
- [Start The Dos](#Start-The-dos)

### Crypto
- [The Beginning Of All](#The-Beginning-Of-All)
- [Leaked Convo](#Leaked-Convo)
- [Top Password](#Top-Password)

### Digital Forensics
- [The Cryptic Sound](#The-Cryptic-Sound)
- [Dump Digging](#Dump-Digging)

### Web
- [Tyrell's Password Maze](#Tyrells-Password-Maze)



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

<!--  {% raw %} --> 

given text:
```
duv#r!|"rG Xrr} (|$! %|vpr y|&; Znxr "$!r {| |{r urn!" $";
a(!ryyG N!r (|$ q|{r &v#u (|$! "r#$}L
Yr|{G R%r!(#uv{t v" "r#; aur }n(y|nq" n!r "r#; aur #n!tr#" n!r sv'rq; V#â" w$"# n zn##r! |s #vzr {|&.
duv#r!|"rG aur p|{pr}# |s &nv#v{t or&vyqr!" zr; ]b]T`*>DBlD>g@lD=lBDArDlDb@lWAr,; dr {rrq #| xrr} !|#n#v{t |$! p|{%r!"n#v|{ "| #un# {|#uv{t tr#" yrnxrq;
a(!ryyG [|#rq.
```

<!--  {% endraw %} --> 

It is rot 47 with n=81. and flag is in rot13.

```
flag: CHCTF{175_71M3_70_574r7_7H3_W4r}
```

<br>

### Top Password

DESCRIPTION:
_Out of nowhere, Leon signaled something to Cisco. Kind of some secret language. Since Leon is out of his place, why not a peek-a-boo into his room? I climbed to the 2nd floor to his room where I found his Tablet charging and a note pinned on the board. Maybe that's the password for the tablet. I NEED THAT!_

file: [image.png](https://github.com/Manoj-Mukund/files/blob/main/CyberHavoc/image.png)

cipher text: `WXERGT_CSZWQWREGIYQZ`

given image is French Sign Language which decode to : `JUMPINGEVENSTEPSONLY`

It is [hill cipher](https://www.dcode.fr/hill-cipher). the matrix number values are (2, 4, 6, 8) from the `JUMPINGEVENSTEPSONLY` and alphabet 27 character.

decoded text: `DESTRUCTION_AT_PEAK_`

```
flag: CHCTF{DESTRUCTION_AT_PEAK}
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

<br>

### Dump Digging

file: [Is it True.pcapng](https://github.com/Manoj-Mukund/files/blob/main/CyberHavoc/Is%20it%20True.pcapng)

there is one png file `zero or one.jpg` to extract it open Wireshark 

`File > Export Objects > HTTP` and select file and save.

inside this jpg image there is hexdump data 

<img width="480" alt="image" src="https://user-images.githubusercontent.com/79740895/233056542-f9587df2-4b5b-4094-b0a5-a3461876b12a.png">

copy that and convert to raw data and save and change the header to `89 50 4E 47 0D 0A 1A 0A` and save as .png there is flag in this image.

```
flag: CHCTF{Th3_most_pow3rful_motivator_in_th3_world_is_r3v3ng3}
```




<br>

---------------------------

## Web

### Tyrell's Password Maze

in HTML source code we can see this js:
```javascript
var _0xcb06=["\x76\x61\x6C\x75\x65","\x75\x73\x65\x72\x6E\x61\x6D\x65","\x67\x65\x74\x45\x6C\x65\x6D\x65\x6E\x74\x42\x79\x49\x64","\x70\x61\x73\x73\x77\x6F\x72\x64","\x43\x79\x62\x65\x72\x48\x61\x76\x6F\x63","\x43\x79\x62\x65\x72\x48\x61\x76\x6F\x63\x23\x31\x32\x33\x34\x35","\x4C\x6F\x67\x69\x6E\x20\x73\x75\x63\x63\x65\x73\x73\x66\x75\x6C\x21","\x51\x30\x68\x44\x56\x45\x5A\x37\x51\x6A\x42\x75\x4E\x54\x42\x70\x63\x6C\x38\x7A\x4D\x54\x45\x77\x4E\x31\x38\x33\x61\x47\x6B\x31\x58\x32\x6B\x31\x58\x32\x31\x35\x58\x32\x74\x70\x62\x6D\x64\x6B\x62\x32\x31\x66\x4E\x47\x35\x6B\x58\x33\x6B\x77\x64\x58\x49\x7A\x58\x32\x70\x31\x4E\x54\x64\x66\x4E\x46\x39\x32\x61\x54\x56\x70\x4E\x7A\x42\x79\x66\x51\x6F\x3D","\x6C\x6F\x67","\x69\x6E\x6E\x65\x72\x48\x54\x4D\x4C","\x72\x65\x73\x75\x6C\x74","\x57\x65\x6C\x6C\x20\x64\x6F\x6E\x65\x2C\x20\x45\x6C\x6C\x69\x6F\x74\x2E\x20\x59\x6F\x75\x20\x68\x61\x76\x65\x20\x70\x72\x6F\x76\x65\x6E\x20\x79\x6F\x75\x72\x73\x65\x6C\x66\x20\x74\x6F\x20\x62\x65\x20\x61\x20\x73\x6B\x69\x6C\x6C\x65\x64\x20\x68\x61\x63\x6B\x65\x72\x2E\x20\x42\x75\x74\x20\x74\x68\x65\x20\x72\x65\x61\x6C\x20\x63\x68\x61\x6C\x6C\x65\x6E\x67\x65\x20\x69\x73\x20\x79\x65\x74\x20\x74\x6F\x20\x63\x6F\x6D\x65\x2E\x20\x41\x72\x65\x20\x79\x6F\x75\x20\x72\x65\x61\x64\x79\x20\x74\x6F\x20\x75\x6E\x72\x61\x76\x65\x6C\x20\x74\x68\x65\x20\x73\x65\x63\x72\x65\x74\x73\x20\x6F\x66\x20\x74\x68\x65\x20\x6D\x61\x7A\x65\x20\x61\x6E\x64\x20\x64\x69\x73\x63\x6F\x76\x65\x72\x20\x74\x68\x65\x20\x74\x72\x75\x74\x68\x20\x62\x65\x68\x69\x6E\x64\x20\x74\x68\x65\x20\x63\x68\x61\x6F\x73\x20\x69\x6E\x20\x74\x68\x65\x20\x63\x79\x62\x65\x72\x20\x77\x6F\x72\x6C\x64\x3F","\x49\x6E\x76\x61\x6C\x69\x64\x20\x75\x73\x65\x72\x6E\x61\x6D\x65\x20\x6F\x72\x20\x70\x61\x73\x73\x77\x6F\x72\x64\x2E"];function login(){const _0x4367x2=document[_0xcb06[2]](_0xcb06[1])[_0xcb06[0]];const _0x4367x3=document[_0xcb06[2]](_0xcb06[3])[_0xcb06[0]];if(_0x4367x2=== _0xcb06[4]&& _0x4367x3=== _0xcb06[5]){alert(_0xcb06[6]);console[_0xcb06[8]](_0xcb06[7]);document[_0xcb06[2]](_0xcb06[10])[_0xcb06[9]]= _0xcb06[11]}else {alert(_0xcb06[12])}}
```

we can use devtools to deobfuscate this 


we can see the username, password, and base64 string

<img width="899" alt="image" src="https://user-images.githubusercontent.com/79740895/233036027-090718f7-ba4c-47fc-9d58-674a508cc7b8.png">


`Q0hDVEZ7QjBuNTBpcl8zMTEwN183aGk1X2k1X215X2tpbmdkb21fNG5kX3kwdXIzX2p1NTdfNF92aTVpNzByfQo=`

```
flag: CHCTF{B0n50ir_31107_7hi5_i5_my_kingdom_4nd_y0ur3_ju57_4_vi5i70r}
```

