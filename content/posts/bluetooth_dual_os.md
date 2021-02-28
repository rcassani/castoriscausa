Title: Shared Bluetooth devices in dual-boot PC
Date: 2021-02-28 14:10
Tags: Linux, Windows, tutorial, Bluetooth
Author: Raymundo Cassani
Slug: bluetooth-dual-boot
Thumbnail: bluetooth_dual.png

### Scenario
You have a Bluetooth (BT) Device (headphones, keyboard, mouse, etc.) with [MAC address](https://en.wikipedia.org/wiki/MAC_address) `XX:XX:XX:XX:XX:XX`, and you want to use this BT device in a dual OS PC (in this case Linux and Windows), which as a BT Adapter with MAC address `YY:YY:YY:YY:YY:YY`.

**Pairing the device in both OS does not work!**

Because of the way the [Bluetooth pairing process](https://www.ellisys.com/technology/een_bt07.pdf) happens: every time the Device and the Adapter are paired a **shared secret Link Key** is generated. This **Link Key** is used to authenticate the Device-Adapter connection. As such pairing in one OS will overwrite the **Link Key**.

### The solution
The solution is to use the same **Link Key** in both operative systems.

1. First, pair the Device and Adapter in OS A  
2. Pair the Device and Adapter in OS B  
3. Get the Link Key generated in OS B  
4. Modify the Link Key in OS A to be the one you got from OS B.

The specific instruction vary depending of which OS does first the pairing. Below the instructions for both cases:  

* If Linux is the OS A: [instructions](#linux-first)  
* If Windows is the OS A [instructions](#windows-first)  

### Linux first
1. Pair the Device in Linux
2. Pair the Device on Windows
3. Get the Link Key in Windows

    Get PSTools: https://docs.microsoft.com/en-us/sysinternals/downloads/psexec

    Run as Administrator:

        :::bash
        $ ./psexec -s -i regedit.exe

    Go to:  
    `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\BTHPORT\Parameters\Keys\YYYYYYYYYYYY\`

    Copy the Value (this is the Link Key) corresponding to Key: MAC address of the Device (`XXXXXXXXXXXX`)

    The Link Key in Windows has spaces and lower cases. To be used in Linux, it should not have spaces and be in Capitals.

4. Set the Link Key from Windows into Linux  
    Open the directory: `/var/lib/bluetooth/[YY:YY:YY:YY:YY:YY]/[XX:XX:XX:XX:XX:XX]/`  
    Edit the `Key` field in `[LinkKey]` section of the `info` file with the Value obtained from Windows

        :::bash
        [LinkKey]
        Key=B99999999FFFFFFFFF999999999FFFFF

    Reboot

### Windows first
1. Pair the Device in Windows
2. Pair the Device on Linux
3. Get the Link Key in Linux

    Open the directory: `/var/lib/bluetooth/[YY:YY:YY:YY:YY:YY]/[XX:XX:XX:XX:XX:XX]/info`  
    Copy the `Key` field in `[LinkKey]` section of the `info` file, this is the Link Key

        :::Bash
        [LinkKey]
        Key=B99999999FFFFFFFFF999999999FFFFF [the LinkKeys for the device]

4. Set the Link Key from Linux into Windows
    Get PSTools: https://docs.microsoft.com/en-us/sysinternals/downloads/psexec

        :::bash
        $ ./psexec -s -i regedit.exe

    Go to:
    `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\BTHPORT\Parameters\Keys\YYYYYYYYYYYY`

    Edit the Value (this is the Link Key) corresponding to Key: MAC address of the Device (`XXXXXXXXXXXX`)

    The Link Key in Windows has spaces is in lower case. Format the Link Key from Linux accordingly.  

5. Reboot

    If the Device cannot be forgotten in Windows (to do a fresh pairing), use [BluetoothCLTools](https://bluetoothinstaller.com/bluetooth-command-line-tools) to remove it from the Command Line.
