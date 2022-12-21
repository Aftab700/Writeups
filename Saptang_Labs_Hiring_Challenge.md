
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


