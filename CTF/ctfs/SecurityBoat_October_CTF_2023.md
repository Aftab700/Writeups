#  SecurityBoat - October CTF 2023

> best solution wins a 1-month PentesterLab Pro Voucher!

<br>

Challange page: http://ctf.securityboat.in:4000/october_challenge/

<img width="806" alt="image" src="https://github.com/Aftab700/Writeups/assets/79740895/48daab9f-b9f9-428e-9d19-77840af1dea9">

Here we have one `light Mode` switch which changes the theme to dark mode

It set the cookie to `dark_mode=czo1OiJsaWdodCI7`\
Base64 decoding this we get `s:5:"light";`\
this seems like a php serialized object\
we also have the php source code which was shared on the [comments of LinkedIn post](https://www.linkedin.com/feed/update/urn:li:activity:7118920886455312384?commentUrn=urn%3Ali%3Acomment%3A%28activity%3A7118920886455312384%2C7119579033029255168%29&dashCommentUrn=urn%3Ali%3Afsd_comment%3A%287119579033029255168%2Curn%3Ali%3Aactivity%3A7118920886455312384%29) of the challange.

![image](https://github.com/Aftab700/Writeups/assets/79740895/e0e26f90-939a-4b78-9db3-a30e55c65881)

In the source code we can see that code will call unserialize() function on base64 decoded cookie value of `dark_mode`

In the source code we notice the `GetThemeNameFromFile` class contains the `__tostring()` magic method. This will 
invoke the `file_get_contents()` method on the `filename` attribute and it will return the file content.

now we have to create serialized PHP object `GetThemeNameFromFile` with `filename` attribute\
testing payload: `O:20:"GetThemeNameFromFile":1:{s:8:"filename";s:9:"index.php";}`

In response we get the source code of the `index.php`

<img width="776" alt="image" src="https://github.com/Aftab700/Writeups/assets/79740895/248239f1-e925-42d0-b3ab-a6775e92da7d">

now we have to locate the flag file\
after few try and error for the flag path we get flag at:`/home/flag` \
payload:`O:20:"GetThemeNameFromFile":1:{s:8:"filename";s:10:"/home/flag";}`

<img width="760" alt="image" src="https://github.com/Aftab700/Writeups/assets/79740895/080230a4-5b66-438f-a9d4-a0b98a762667">

But it not the correct flag\
When submitting the wrong flag hint is given: 

```
That is rabbit hole with wrong path. Please try on other different popular paths as well😊
```

So when trying different paths we get one more flag at `/etc/flag`

```
O:20:"GetThemeNameFromFile":1:{s:8:"filename";s:10:"/home/flag";}
```

<img width="769" alt="image" src="https://github.com/Aftab700/Writeups/assets/79740895/dc8bddff-ff2d-4e80-ad5a-7016c0174bcd">

Flag: `Flag{__inS3cur3_d3seR14liz47iOn_ftw}`

<br>

:octocat: Happy Hacking :octocat:
