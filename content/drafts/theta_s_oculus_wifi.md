Title: Theta S
Date: 2017-05-06 10:00
Category: Blog
Tag:
Slug: wifi-richoh-theta-s-oculus-unity
Author: Ray Cassani
Summary: Las spikes

This is report of the things I tried to stream (using wifi) video from the
RICOH THETA-S to the Oculus using DK2, latest SDK in Window10 64bits.

The final result can be found here:
http://ray_repo

## Preview
The THETA-S has [USB and HDMI streaming](), however it streams video from the two fish-eye cameras as shown in the picture. The device is recognized as a webcam.

By using the THETA-S UVC Blender software it's supposed to convert the USB-HDMI streamed video in Equirectangular (in the host side). However, I tried it and it does not work for me.

NOTE: To turn on the THETA-S camera in Live-Streaming mode, with the camera off, press the Power button and the Photo/Video button at the same time, the camera will go on, wit the Live indicator as indicated

There is a detailed guide in THETA-S live streaming here: http://theta360.guide/community-document/live-streaming.html

The key point is in the section 10:  
*"The THETA can live stream a 640x320 MotionJPEG at 10fps over WiFi. This is intended to preview a picture prior to taking the picture. It’s not intended for headset navigation. The community has built some solutions to stream this low-res, low fps video to mobile phones, primarily using Unity."*

## Approaches
From what I've read there are these options for wireless streaming:

http://lists.theta360.guide/t/theta-refuses-to-live-stream-via-usb-error-theta-uvc-blender-status-0x800705aa/54/5
another question if you have any guidance, the latency going through the UVC blender is pretty high, about 3-4 seconds. Do you know if there's any way to cut that down? maybe encode at a lower resolution or frame rate?


* PC + USB +THETA-S + UVC Blender --> [Youtube / local conference ] --> PC + Oculus
https://gist.github.com/visnup/e651059b091537fd257eb215035ca7df
http://theta360.guide/community-document/live-streaming.html
  * seems that this option adds a 3-4 second delay)
  *

* PC + USB + THETA + Manual stitching (in Unity or Browser) + Oculus
seems to be faster

* WiFi THETA-S --> Manual stitching (in Unity) + Oculus

## Ray
I'll go with the third option

There are some steps that need to be solved:
* Get the wiFi stream in Unity
https://github.com/theta360developers/ThetaWifiStreaming

* Add the Oculus support
https://www.youtube.com/watch?v=_gBI0SN044o
http://lists.theta360.guide/t/tutorial-live-ricoh-theta-s-dual-fish-eye-for-steamvr-in-unity/938?u=codetricity

Stiching in Unity:
https://github.com/theta360developers/unity-streaming

### 1. Get the wiFi stream in Unity
https://github.com/theta360developers/ThetaWifiStreaming
works out of the box, just select the provided scene

### 2. Add the Oculus support

#### Setup Unity environment and Toy Example:

[Oculus Unity Utilities](https://developer3.oculus.com/documentation/game-engines/latest/concepts/book-unity/)

[Oculus Rift Downloads](https://developer.oculus.com/downloads/unity/)

[Unity VR Overview](https://unity3d.com/learn/tutorials/topics/virtual-reality/vr-overview)

Setup Oculus (that is able to run the Oculus App in Windows)

1. Download and unzip Oculus Utilities for Unity (second link)

2. Create Unity project, default settings, 3D project
(Image)
Unity 5 has a build it support for VR, the Oculus Utilities will override that default support, it's possible to go back, if needed
https://developer.oculus.com/downloads/package/oculus-utilities-for-unity-5/
Right click in assets and Import package > Custom package , go to the package downloaded in step one

(Image for import)

It may ask you to Update Oculus Utilities Plugin, Accept
You may need to reestar Unity

3. Got ot Edit > Project ettings, Player in the Inspector go to Other Settings and check Virtual Reality Supported
(image)

4. Trivial example:
  1. Create a Scene, add game objects around (cubes differentplaces)
  2. From OVR\Prefab add to the Scene OVRPlayerController
  3. Add a Plane
  4. Click on Play

Note: The Oculus App should be running in the background

#### Adding Oculus for Sphere

# Process

# For Oculus DK2

1. Get the wiFi stream in Unity
https://github.com/theta360developers/ThetaWifiStreaming
works out of the box, just select the provided scene

2. Forked, renamed and clone the new repo

1. Download and unzip Oculus Utilities for Unity (second link)
[Oculus Rift Downloads](https://developer.oculus.com/downloads/unity/)

3. Created a new folder for the Oculus Scene
add a script explicit for Adjusting the Scene for the Oculus

4. Add VR support to Unity project

# Use
Run Oculus program, run unity scene oculus
Space to recenter view

# Similar should be for Cardboard

1. Download Unity 5.6
2. Download Android SDK https://developer.android.com/studio/index.html
3. Google VR SDK for Unity https://developers.google.com/vr/unity/download

1. Isntall Unity with "Android Build Support" component is selected during installation

2. Install Android SDK
android-studio-bundle-162.3934792-windows.exe

3. Setup Unity to use Android SDK
https://docs.unity3d.com/Manual/android-sdksetup.html
Unity > Preferences > External Tools.

JDK
http://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html
Win x86
4. Import Unity package GoogleVR
Import ALL

5.


















1








There is this App for the Oculus Gear VR, but it needs beside the headset, a Samsumg Galaxy phone. *"taking 360° photos and viewing them all from within your Gear VR"*, it seems it does not stream
https://www.oculus.com/experiences/gear-vr/1191734024175398/
