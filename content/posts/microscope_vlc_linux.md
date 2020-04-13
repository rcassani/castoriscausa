Title: USB microscope and VLC
Date: 2020-04-06 20:37
Category: Projects
Tags: Linux, photos
Author: Raymundo Cassani
Slug: microscope-vlc-linux
Thumbnail: fish_1.png

This post is to show the type of images that can be obtained with an affordable USB microscope, similar to [this one](https://www.amazon.ca/axGear-50-500X-Microscope-Endoscope-Magnifier/dp/B01996WOEU). The output image is 640 x 480 pixels, and the optical zoom is supposed to go from 50x to 500x. As the microscope has not adjustment for focus, for most of the samples I was able to focus them in unknown magnification settings, let's call them low- and high-zoom.

In the technical side, as the microscope is detected as a standard webcam, it is possible to use [VLC](https://www.videolan.org/vlc/index.html) to capture the images and video, see further instructions [here](https://www.laptopmag.com/articles/record-webcam-video-vlc). In Linux, VLC relies on [Video4Linux](https://en.wikipedia.org/wiki/Video4Linux) which is part of the kernel since 2.5.x. Note, the V4L2 module in VLC requires [ZVBI](http://zapping.sourceforge.net/ZVBI/), thus you may need also to install this library.

Without further delay, these are the pictures from different objects at home:   

### Surface-mount device (SMD) LED
The real size is 3 mm by 1.5 mm

| [<img src="/images/smd_1.png" style="width: 450px;"/>](/images/smd_1.png)| <img src="/images/square_500_clear.png" style="width: 32px;"/> |[<img src="/images/smd_2.png" style="width: 450px;"/>](/images/smd_2.png)|
|:-:|:-:|:-:|
|Low zoom|    |High zoom|
<br>  

### The 1-mm mark in a vernier caliper
For the low-zoom pic, there are 154 pixels between the center of the marks, a rough resolution of 6.5 &mu;m per pixel. And for the high-zoom pic, there are 570 pixels, thus around 1.8 &mu;m per pixel.

| [<img src="/images/1mm_1.png" style="width: 450px;"/>](/images/1mm_1.png)| <img src="/images/square_500_clear.png" style="width: 32px;"/> |[<img src="/images/1mm_2.png" style="width: 450px;"/>](/images/1mm_2.png)   |
|:-:|:-:|:-:|
|Low zoom|    |High zoom|
<br>  

### Fish fossil
It's common have a fossil of a fish at home, right?. The pictures correspond to the area near to the tail.  

<center>
[<img src="/images/fish_0.jpg" style="width: 500px;"/>](/images/fish_0.jpg)
</center>

| [<img src="/images/fish_1.png" style="width: 450px;"/>](/images/fish_1.png)| <img src="/images/square_500_clear.png" style="width: 32px;"/> |[<img src="/images/fish_2.png" style="width: 450px;"/>](/images/fish_2.png)   |
|:-:|:-:|:-:|
|Low zoom|    |High zoom|
<br>  

### Display AMOLED (from Pixel 2)
The "1" was around 2-mm tall on the display.

| [<img src="/images/led_1.png" style="width: 450px;"/>](/images/led_1.png)| <img src="/images/square_500_clear.png" style="width: 32px;"/> |[<img src="/images/led_2.png" style="width: 450px;"/>](/images/led_2.png)   |
|:-:|:-:|:-:|
|Low zoom|    |High zoom|
</br>  

### Escape mechanism
Lastly, a close-up video of the escape mechanism in a watch.
<center>
<video controls="" autoplay="" loop>
 <source src="/images/out.webm" type="video/webm">
</video>
</center>
