# RLotto

`EASY` , `Crypto`

CHALLENGE DESCRIPTION:
_Are you ready to win lottery? Guess the Random Lotto Numbers. It's TIME you become a millionaire._

--------

In the given code we can see that it is using `seed = int(time.time())` to generate 5 random digits using `random.randint(1, 90)` \
It will give us the first 5 random digits and we have to guess next 5 to get the flag.

Because we have the first 5 random generated digits we can brute force the seed. Initial seed value would be `time.time()` befor we connect to server and incriment it by one. \
when we get the seed we can generate the next 5 digits.

python code:
```python
import time
import random

# seed = int(time.time())
seed = 1703848677

def find_solution(s_extracted):
    global seed
    s_extracted = [int(i) for i in s_extracted.split(" ")]
    while True:
        random.seed(seed)
        extracted = []
        while len(extracted) < 5:
            r = random.randint(1, 90)
            if(r not in extracted):
                extracted.append(r)
        if extracted == s_extracted:
            print(seed)
            break
        seed += 1
    solution = ""
    next_five = []
    while len(next_five) < 5:
        r = random.randint(1, 90)
        if(r not in next_five):
            next_five.append(r)
            solution += str(r) + " "
    solution = solution.strip()
    print("[+] SOLUTION: " + solution)
    pass

find_solution("40 8 6 17 63") # [+] EXTRACTION Value
```

Flag: `HTB{n3v3r_u53_pr3d1c74bl3_533d5_1n_p53ud0-r4nd0m_numb3r_63n3r470r}`
