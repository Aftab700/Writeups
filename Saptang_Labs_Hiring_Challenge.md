
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


