## Wizard:

_You have stumbled upon a wizard on your path to the flag. You must answer his questions!_

------

Connect with:

`nc challenge.nahamcon.com 32201`

it gives us the questions and we have to give input the answers

First Question: What is the ASCII plaintext corresponding to this binary string?
```
010110100110010101110010011011110111001100100000001001100010000001001111011011100110010101110011
```
From Binary: "Zeros & Ones"

Second Question: What is the ASCII plaintext corresponding to this hex string?
```
4f6820776f77777721204261736520313020697320636f6f6c20616e6420616c6c2062757420486578787878
```
From Hex: "Oh wowww! Base 10 is cool and all but Hexxxx"

Third Question: What is the ASCII plaintext corresponding to this octal string?
(HINT: octal -> int -> hex -> chars)
```
535451006154133420162312701623127154533472040334725553046256234620151334201413347444030460563312201673122016730267164
```
- Octal to HexaDecimal
- From Hex

"We can represent numbers in any base we want"

Fourth Question: What is the ACII representation of this integer?
(HINT: int -> hex -> chars)
```
8889185069805239596091046045687553579520816794635237831028832039457
```
- Desimal to HexaDecimal
- From Hex

"This is one big 'ol integer!"

Fifth Question: What is the ASCII plaintext of this Base64 string?
```
QmFzZXMgb24gYmFzZXMgb24gYmFzZXMgb24gYmFzZXMgOik=
```
From Base64: "Bases on bases on bases on bases :)"

Last Question: What is the Big-Endian representation of this Little-Endian hex string?
```
293a2065636e657265666669642065687420776f6e6b206f7420646f6f672073277449
```
[LITTLE to BIG ENDIAN](https://www.save-editor.com/tools/wse_hex.html)
- From Hex
"It's good to know the difference :)"

```
flag{c2ed35aba037cd93381b298caa2720ee}
```
