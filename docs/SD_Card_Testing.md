# Verifying the SD Card 
 

There has been a lot of discussion recently about bad SD cards which are not the advertised size. The card I was using with my Raspberry Pi always seemed a 
bit strange so I decided to check it and found the following command:

```f3write```

This command writes to every sector on the card and the corresponding command reads from every sector confirming that the write was good.

When I tested my 128GB card it was automatically eject after a few minutes and couldn't be tested. I wondered whether the multi card reader that was plugged 
into the USB C port on my Mac was getting moved slightly due vibration and losing the connection so I tried again. The same problem occured.

Since I thougth it was a physical problem I decided to get a single function mini-SD card reader which arrived from Amazon the following day. Testing reading 
and writing to the card worked perfectly and that it wasn't the card that was a fault but the multi card reader.

Also see:

* [Verifying SD-card size/capacity on Mac OS X](https://daniel-starling.com/blog/2017/10/15/mac-os-x-verify-sd-card/)
* [How to Find if Your Thumb Drive/SD Card Is Fake With f3 (Linux Tutorial) Make sure your data is safe.](https://medium.com/@drawn_stories/how-to-find-if-your-thumb-drive-sd-card-is-fake-with-f3-linux-tutorial-f0109bef63ea)
