## Quirky:

_This file is seems to have some strange pattern..._

_Attachment: [Quirky](files/quirky)_

-----

given file is hex of image raw data we can use [CyberChef](https://gchq.github.io/CyberChef/) to get the image
it will give us QR code after parsing the QRcode it gives the flag

filters to use in CyberChef:
- From Hex
- Render Image
- Parse QR code

```
flag{b7e2a32f5ae629dcfb1ac210d1f0c032}
```
