Touchpads are not for everyone (as my case), for those people, one of the first things I do with a laptop is to disable the touchpad (TP). 

When I did that in my laptop, I noticed a strange behavior, the TP (model) is re-enabled every time Windows (10) starts.  Which means I had to disable it every time.

After some research I can across this wonderful solution where the [touchpad is disabled when a mouse detected](http://www.intowindows.com/how-to-turn-off-touchpad-when-mouse-is-connected-in-windows-78-1/). Unfortunately, my system detects an extra mouse with the keyboard (steelseries), enable the auto disable, would mean TF permanently disables, and who knows it could be useful (someday).

After diving in [Regedit](link to somewhere), I noticed two values that control the behavior in the touchpad, these are:

DisableDeviceUntilSessionEnd in HKEY_CURRENT_USER\SOFTWARE\Synaptics\SynTP\TouchPadPS2TM3163
and
DisableDeviceUntilSessionEnd in HKEY_CURRENT_USER\SOFTWARE\Synaptics\SynTP\TouchPadSMB2cTM3163

Basically, when they are 0 the TP remembers its state and when 1, the TP will be enabled the next login, in my case the present value was 1, and changing the value to 0 was the solution.

This can be done, in two way, changing the values in regedit (just do it if you know what you're doing)
Merging the reg files in your register (download it and execute it)
In case you miss the autono-enabling behavior, change the values back to 1, or run this reg file:


The scripts will work only, if you have the same TP model. 


After looking for a while i found this keys in regedit, which allow to disable the TP and
keep it like that until you enabled it again:

A value inside two keys:

TP remembers its state
HKEY_CURRENT_USER\SOFTWARE\Synaptics\SynTP\TouchPadPS2TM3163
DisableDeviceUntilSessionEnd = 0
HKEY_CURRENT_USER\SOFTWARE\Synaptics\SynTP\TouchPadSMB2cTM3163
DisableDeviceUntilSessionEnd = 0

TP goes enabled every single time
HKEY_CURRENT_USER\SOFTWARE\Synaptics\SynTP\TouchPadPS2TM3163
DisableDeviceUntilSessionEnd = 1
HKEY_CURRENT_USER\SOFTWARE\Synaptics\SynTP\TouchPadSMB2cTM3163
DisableDeviceUntilSessionEnd = 1

http://www.intowindows.com/how-to-turn-off-touchpad-when-mouse-is-connected-in-windows-78-1/
Synaptics Pointing Device

Title
Keeping Synaptics touchapad disabled

Create a reg to write those keys, and to return them to the original value

