# Lost Modulus

`Crypto`

https://app.hackthebox.com/challenges/lost-modulus

CHALLENGE DESCRIPTION
_I encrypted a secret message with RSA but I lost the modulus. Can you help me recover it?_

----------------------

In the file given `challenge.py` we can see that it is RSA encryption and the value of `e` is `3` \
Here the `e` is small and `n` is too large, so `m^e < N` \
When the value of `e` is as small as 3, we can just do the 3rd root of cipher text and we can get the message 

Python code:

```python
import gmpy2
from Crypto.Util.number import long_to_bytes

cipher = int(
    "05c61636499a82088bf4388203a93e67bf046f8c49f62857681ec9aaaa40b4772933e0abc83e938c84ff8e67e5ad85bd6eca167585b0cc03eb1333b1b1462d9d7c25f44e53bcb568f0f05219c0147f7dc3cbad45dec2f34f03bcadcbba866dd0c566035c8122d68255ada7d18954ad604965",
    16,
)
with gmpy2.local_context(gmpy2.context(), precision=800) as ctx:
    ctx.precision += 800
    croot = gmpy2.cbrt(cipher)
    print(long_to_bytes(int(croot)))
```

Flag: `HTB{n3v3r_us3_sm4ll_3xp0n3n7s_f0r_rs4}`

:octocat: Happy Hacking :octocat:
