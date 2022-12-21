
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
