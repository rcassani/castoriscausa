Title: Keeping Synaptics touchpad disabled
Date: 2016-12-06 19:00
Category: Blog
Tag: Fix
Slug: touchpad
Author: Ray Cassani

Touchpads are not for everyone, one of the first things to do when a I get a new computer is to plug a mouse and disable the touchpad (TP).

Few month ago, I noticed a strange behavior in my [laptop]([https://us.msi.com/Laptop/GE62VR-Apache-Pro-6th-Gen-GTX-1060.html#hero-overview), the TP (model) no matte the status of the TP, every time Windows started, the touchpad was enabled, which means I had to disable it every time.

After some research I came across this wonderful solution where the [touchpad is disabled when a mouse detected](http://www.intowindows.com/how-to-turn-off-touchpad-when-mouse-is-connected-in-windows-78-1/). Unfortunately, the [steelseries keyboard]() in my computer is detected as keyboard-mouse combo, enabling the auto disable, would imply permanently disable the touchpad, and who knows it could be useful (someday).

After diving in [Regedit](link to somewhere), I noticed two values that control the behavior in the touchpad, these are:

`DisableDeviceUntilSessionEnd` in `HKEY_CURRENT_USER\SOFTWARE\Synaptics\SynTP\TouchPadPS2TM3163`
and
`DisableDeviceUntilSessionEnd` in `HKEY_CURRENT_USER\SOFTWARE\Synaptics\SynTP\TouchPadSMB2cTM3163`

Basically, when they are 0 the TP remembers its state and when 1, the TP will be enabled the next login, in my case the present value was 1, and changing the value to 0 was the solution.

This can be done, in two ways,

* changing the values in Regedit (just do it if you know what you're doing)

For this specfic model of TP


* Merging the reg files in your register (download it and execute it)
In case you miss the auto-enabling behavior, change the values back to 1, or run this reg file:

The scripts will work only, if you have the same TP model.

http://www.intowindows.com/how-to-turn-off-touchpad-when-mouse-is-connected-in-windows-78-1/
Synaptics Pointing Device

Title

Create a reg to write those keys, and to return them to the original value
