# IWCON CTF 2023
> Start Time: 14th December 2023, 5:30 PM IST

> End Time: 15th December 2023, 5:30 PM IST

<br>

## Challenges

### WARMUP
- [Socialize](#socialize)
- [runme](#runme)

<br>

---------------------------

<br>

## Socialize

- Learn to socialize!
- https://discord.gg/H7sQx76n
- Flag format: IWCON{}

Flag is in `iwcon-ctf` channel

<img width="396" alt="image" src="https://github.com/Aftab700/Writeups/assets/79740895/89de8ffe-c4e1-421f-9fb8-f0d591c9f2fc">

Flag: `IWCON{y0u_w3r3_h3r3_f!rst}`


## runme

- code me!
- Flag format: IWCON{}
- [runme.class](../files/runme.class)

using online decompiler we get [java code](https://www.decompiler.com/jar/6ae10a74e255424f99b8b8b431e7975b/runme.java)

<details><summary markdown="span">Click to see code :diamond_shape_with_a_dot_inside: </summary>

```java

import java.util.Arrays;
import java.util.Base64;

public class iwcon {
   public static String get_flag() {
      byte[] var0 = "YPSiRhFjpXbIfgVc]NnHoeWlJ_mOEUQT[L`^kKGMda\\Z".getBytes();
      byte[] var1 = "c54h1dW2z1yVNTdfzRITS9MJMnj53ByM3Xz0D7azN9Xe".getBytes();
      byte[] var2 = new byte[var1.length];

      for(int var3 = 0; var3 < var1.length; ++var3) {
         var2[var3] = var1[var0[var3] - 69];
      }

      System.out.println(Arrays.toString(Base64.getDecoder().decode(var2)));
      return new String(Base64.getDecoder().decode(var2));
   }

   public static void main(String[] var0) {
      System.out.println();
   }
}

```
</details>


in this code we modify main function to add call to `get_flag()`

```java
public static void main(String[] var0) {
      System.out.println(get_flag());
   }
```

<img width="586" alt="image" src="https://github.com/Aftab700/Writeups/assets/79740895/5887d9de-d232-4534-8825-6c621f3551bc">

Flag: `IWCON{y0u_4r3_a_r3v3rs3_3ngin33r}`



