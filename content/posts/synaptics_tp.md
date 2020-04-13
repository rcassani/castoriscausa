Title: Keeping Synaptics Touchpad disabled
Date: 2016-12-06 19:00
Category: Blog
Tags: Windows, touchpad
Slug: touchpad-disable
Author: Raymundo Cassani
Thumbnail: touchpad_keyboard_ge62vr.jpg

Touchpads in laptops are not for everyone, one of the first things to do when a I get a new computer is to plug a mouse and disable the touchpad (TP).

Few weeks ago, I noticed a strange behavior, in my [laptop]([https://us.msi.com/Laptop/GE62VR-Apache-Pro-6th-Gen-GTX-1060.html#hero-overview), every time I started a session in Windows, the touchpad was **enabled**, that is to say it did not keep its previous status. The touchpad is a **Synaptics SMBus TouchPad**. As this behavior was **annoying**, something needed to be done.

After some research I came across this wonderful solution where the [touchpad is automatically disabled when a mouse is  detected](http://www.intowindows.com/how-to-turn-off-touchpad-when-mouse-is-connected-in-windows-78-1/). Unfortunately, the **Steelseris Keyboard** in my laptop is detected as **keyboard-mouse combo**, then, the auto-disable, would permanently disable the touchpad, without option to enable it and who knows it could be useful (someday).

<center>
[![Alt](/images/touchpad_keyboard_ge62vr.jpg)](/images/touchpad_keyboard_ge62vr.jpg)  
Touchpad and Keyboard in GE62VR
</center>  


Later, after diving in [Windows Register](https://en.wikipedia.org/wiki/Windows_Registry), with Regedit, I noticed a value, in two keys, that controls the touchpad's behavior at the beginning of the Windows session:

`DisableDeviceUntilSessionEnd`
in    
`HKEY_CURRENT_USER\SOFTWARE\Synaptics\SynTP\TouchPadPS2TM3163`  
`HKEY_CURRENT_USER\SOFTWARE\Synaptics\SynTP\TouchPadSMB2cTM3163`

Basically, when they are ```0``` the touchpad remembers its state at the moment of the last logout, and when ```1```, the touchpad will be enabled every login.

</br>
<center>
#### **Changing the values from ```1``` to  ```0```** was the solution, to keep the touchpad disable.
</center>
</br>

In case you're want to the same re-enabling behaviour in the touchpad, edit the above-mentioned values in the Registry. You can learn the basics on editing the Windows Registry here: [Learn How to Use the Windows Registry Editor (Regedit) in One Easy Lesson](http://www.techsupportalert.com/content/learn-how-use-windows-registry-editor-regedit-one-easy-lesson.htm).
