## FooBar CTF 2023

https://foobar.nitdgplug.org/challenges

---

<img width="463" alt="image" src="https://user-images.githubusercontent.com/79740895/224527980-236d738b-42c8-4305-a352-cd6ec4fdcdc7.png">


---

### Crypto:

#### Pixelite :

we are given with two files: [chall.py](files/chall.py) and [pixelite.png](files/pixelite.png)

and we are also given this number: 1678519928.9423187

looking at code we know that this code is doing xor of every pixel of flag.png with random int between 0 to 255

```python
flag_matrix[i, j] = tuple(
    map(
        lambda x: x ^ random.randint(0, 255),
        flag_matrix[i, j]
    )
)          
```

Here the random module of python can be predicted. If we know the seed value than all the next random int are same every time.

```python
random.seed(time.time())
```

The seed is set to time.time() and we are given this value in challenge:
`1678519928.9423187`

know we can easily reverse this xor operation to get original image.

<details><summary markdown="span">Click to see code :diamond_shape_with_a_dot_inside: </summary>

```python
import time
import random

from PIL import Image


random.seed(1678519928.9423187)

flag_matrix = (img := Image.open('pixelite.png')).load()
w, h = img.size

for i in range(w):
    for j in range(h):
        flag_matrix[i, j] = tuple(
            map(
                lambda x: x ^ random.randint(0, 255),
                flag_matrix[i, j]
            )
        )

img.save('flag.png')

```
</details>

<br>

flag.png:

<img width="289" alt="image" src="https://user-images.githubusercontent.com/79740895/224524411-1518d6e6-0e4a-452e-bbf7-540b38ac204d.png">

`GLUG{Y0u_4Re_noT_5o_w34k}`

<br>

#### funwithrandom-1:

description: _randcrack is fun or is it . let's see if you can create your own_

_nc chall.foobar.nitdgplug.org 30001_

file: [chall.py](files/Chall_funwithrandom-1.py)

In this code we have `rand_gen()` function. if mt_index > 624 than it go inside if statement. 
else it will do the following operations:

```python
y = mt[mt_index]
y ^= (y >> 43)
y ^= (y << 12) & TemperingMaskB
y ^= (y << 67) & TemperingMaskC
y ^= (y >> 69)
mt_index += 1

return y
```

getstate() Return an object capturing the current internal state of the generator.
and the seed is set through os.urandom(8) which is not predictable.

```python
random.seed(os.urandom(8))
mt = list(random.getstate()[1])
```

here output is filled 624 times with rand_gen() function.

```python
output = []
for _ in range(624):
    output.append(rand_gen())
```

again looking at this code we know that it will do this operations on mt aaray from 0 to 624 index.

```python
y = mt[mt_index]
y ^= (y >> 43)
y ^= (y << 12) & TemperingMaskB
y ^= (y << 67) & TemperingMaskC
y ^= (y >> 69)
mt_index += 1

return y
```

and we are given with the output's value so by reversing this operations we can get the value of mt.

with this small trial and error experiment:

```python
y = 1111121111
y ^= (y >> 43)
print("y ^= (y >> 43)")
print(y)
y ^= (y << 12) & TemperingMaskB
print("y ^= (y << 12) & TemperingMaskB")
print(y)
y ^= (y << 67) & TemperingMaskC
print("y ^= (y << 67) & TemperingMaskC")
print(y)
y ^= (y >> 69)
print("y ^= (y >> 69)")
print(y)
```
```shell
output:
y ^= (y >> 43)
1111121111
y ^= (y << 12) & TemperingMaskB
1736326359
y ^= (y << 67) & TemperingMaskC
1736326359
y ^= (y >> 69)
1736326359
```

now we know that only `y ^= (y << 12) & TemperingMaskB` this operation is effective rest are not making any changes.

so now we have to reverse this tempering here is python code for that:

```python
def untemper(y):
    a = y << 12
    b = y ^ (a & TemperingMaskB)
    c = b << 12
    d = y ^ (c & TemperingMaskB)
    e = d << 12
    f = y ^ (e & TemperingMaskB)
    g = f << 12
    h = y ^ (g & TemperingMaskB)
    i = h << 12
    final = y ^ (i & TemperingMaskB)
    return final
```

now from output[] we can get mt[].
but the for loop was run 624 times so next time we call rand_gen() it will go inside if condition.

```python

for kk in range(N - M):
    y = (mt[kk] & UPPER_MASK) | (mt[kk + 1] & LOWER_MASK)
    mt[kk] = mt[kk + M] ^ (y >> 1) ^ mag01[y & 0x1]

for kk in range(N - M, N - 1):
    y = (mt[kk] & UPPER_MASK) | (mt[kk + 1] & LOWER_MASK)
    mt[kk] = mt[kk + (M - N)] ^ (y >> 1) ^ mag01[y & 0x1]

y = (mt[N - 1] & UPPER_MASK) | (mt[0] & LOWER_MASK)
mt[N - 1] = mt[M - 1] ^ (y >> 1) ^ mag01[y & 0x1]

```

we will apply the same changes to our recovered mt[].

now we can get the next 5 int by applying this operations to first 5 elements of mt[].
```python
y = mt[mt_index]
y ^= (y >> 43)
y ^= (y << 12) & TemperingMaskB
y ^= (y << 67) & TemperingMaskC
y ^= (y >> 69)
mt_index += 1
```

now that we have the next 5 random element we can get the flag.

final python script:

<details><summary markdown="span">Click to see code :diamond_shape_with_a_dot_inside: </summary>

```python
import random
from pwnlib.tubes.remote import remote

N = 624
M = 397
MATRIX_A = 0x83a2b0c3
UPPER_MASK = 0x80000000
LOWER_MASK = 0x7fffffff
TemperingMaskB = 0x3f5663d0
TemperingMaskC = 0x56e90000
mag01 = [0, MATRIX_A]


def untemper(y):
    a = y << 12
    b = y ^ (a & TemperingMaskB)
    c = b << 12
    d = y ^ (c & TemperingMaskB)
    e = d << 12
    f = y ^ (e & TemperingMaskB)
    g = f << 12
    h = y ^ (g & TemperingMaskB)
    i = h << 12
    final = y ^ (i & TemperingMaskB)
    return final

conn = remote('chall.foobar.nitdgplug.org', 30001)
conn.recvuntil("Generator\n\n".encode())
output = [int(i) for i in (conn.recvline().decode()[1:-2].split(','))]
print(output)
for i in range(len(output)):
    output[i] = untemper(output[i])
# print(output)
mt = output
for kk in range(N - M):
    y = (mt[kk] & UPPER_MASK) | (mt[kk + 1] & LOWER_MASK)
    mt[kk] = mt[kk + M] ^ (y >> 1) ^ mag01[y & 0x1]

for kk in range(N - M, N - 1):
    y = (mt[kk] & UPPER_MASK) | (mt[kk + 1] & LOWER_MASK)
    mt[kk] = mt[kk + (M - N)] ^ (y >> 1) ^ mag01[y & 0x1]

y = (mt[N - 1] & UPPER_MASK) | (mt[0] & LOWER_MASK)
mt[N - 1] = mt[M - 1] ^ (y >> 1) ^ mag01[y & 0x1]

# print(mt)
mt_index = 0
for i in range(5):
    y = mt[mt_index]
    y ^= (y >> 43)
    y ^= (y << 12) & TemperingMaskB
    y ^= (y << 67) & TemperingMaskC
    y ^= (y >> 69)
    mt_index += 1
    conn.recvuntil(":".encode())
    print(f'{i+1}= {y}')
    conn.sendline(f'{y}'.encode())

print(conn.recvline().decode())
conn.close()

```

</details>

`flag: GLUG{R4nd0m_Numb3r_G3n3r470r_15_tru3ly_r4nd0m_0r_15_17}`



### Web:

#### inspect:

Description: Don't think too much. Just push to production http://chall.foobar.nitdgplug.org:30045/

Rest API was boring so I used modern technology.

Let's open this website

<img width="128" alt="image" src="https://user-images.githubusercontent.com/79740895/224526224-ea11b319-230a-42fe-92cf-84090ed2f17a.png">

Hmn Cannot GET / 

I tried robots.txt and checked http response headers but nothing, so I did directory bruteforce and got this endpoint: `/graphql`
GraphQL is a query language developed by Facebook

http://chall.foobar.nitdgplug.org:30045/graphql

<img width="912" alt="image" src="https://user-images.githubusercontent.com/79740895/224526458-6af4998c-6aca-405d-900d-d81e0de2779d.png">

Reference : https://blog.yeswehack.com/yeswerhackers/how-exploit-graphql-endpoint-bug-bounty/

_Introspection is the ability to query which resources are available in the current API schema. Given the API, via introspection, we can see the queries, types, fields, and directives it supports._

GraphQL introspection payload:
```
{__schema{queryType{name}mutationType{name}subscriptionType{name}types{...FullType}directives{name description locations args{...InputValue}}}}fragment FullType on __Type{kind name description fields(includeDeprecated:true){name description args{...InputValue}type{...TypeRef}isDeprecated deprecationReason}inputFields{...InputValue}interfaces{...TypeRef}enumValues(includeDeprecated:true){name description isDeprecated deprecationReason}possibleTypes{...TypeRef}}fragment InputValue on __InputValue{name description type{...TypeRef}defaultValue}fragment TypeRef on __Type{kind name ofType{kind name ofType{kind name ofType{kind name ofType{kind name ofType{kind name ofType{kind name ofType{kind name}}}}}}}}
```

response:

<img width="897" alt="image" src="https://user-images.githubusercontent.com/79740895/224526602-52da26c6-020d-48af-a460-421d6e0107f3.png">

This secret field looks interesting let's extract this.

payload:
```
{
  secret {
    text
  }
}
```

response:

<img width="628" alt="image" src="https://user-images.githubusercontent.com/79740895/224526694-ede5c243-723e-496f-8fe7-bce808c170cb.png">

when I saw the flag I immediately tried to submit it, but it was wrong then I realised that there are multiple flags.

75 in total.

first I thought it is rabbit hole, but I went through every flag and found this:

<img width="283" alt="image" src="https://user-images.githubusercontent.com/79740895/224526864-605393f7-34fc-4ce6-8bb3-2c8e371cd3e1.png">

this makes sense `inspect` is challenge name and `graphql` is endpoint.

`flag: GLUG{1nsp3c7_1n_gr4phq6}`

This is correct one.

