## Personnel:

A challenge that was never discovered during the 2021 Constellations mission... now ungated :)

Attachment: [app.py](files/Personnel-app.py)

-------

looking at app.py it will remove first character from name parameter `name = name[1:]` and put it in regex

`results = re.findall(r"[A-Z][a-z]*?" + name + r"[a-z]*?\n", users, setting)`
in regex `.*` means everything and we can escape other conditions with use of or operator "|".

payload: `A|.*|`

```
flag{f0e659b45b507d8633065bbd2832c627}
```
