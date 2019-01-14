Title: Streaming your desktop to browser with VLC
Date: 2017-12-04 19:00
Category: Blog
Tag: Fix
Slug: stream-desktop-to-browser
Author: Raymundo Cassani

Useful to share you screen in a LAN or over internet throug a VPN or thing as Hamachi / LogmeIn
Tutorials, video, stream to phone, etc.
HTML5

## 1 Install VLC
From this link []() follow the standard installation.

## Configure

Stream
Capture Device to Desktop

Source Next
Destination Setup: HTTP, add 'test'
Transcoding Options: Active Transcoding: Video -Theora + Vorbis (OGG)

should be:
:sout=#transcode{vcodec=theo,vb=800,scale=1,acodec=vorb,ab=128,channels=2,samplerate=44100}:http{mux=ogg,dst=:8080/test.ogg} :sout-keep

## HTML file
<!DOCTYPE html>
<html>
<head>
<title>HTML5 video test</title>
</head>
<body>
<h1>HTML5 video test</h1>
<video width="640" height="480" autoplay>
    <source src="http://192.26.211.117:8080/test" type="video/ogg" />
    HTML5 video not supported.
</video>
</body>
</html>
