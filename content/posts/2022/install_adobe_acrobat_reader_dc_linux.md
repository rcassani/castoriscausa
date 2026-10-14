Title: Install Adobe Acrobat Reader DC Linux
Date: 2022-05-03 18:00
Tags: Arch, Linux, hack
Author: Raymundo Cassani
Slug: install-adobe-acrobat-reader-dc-linux
Thumbnail: aardc.png

After many tries, I finally found a good set of steps to install [Adobe Acrobat Reader DC](https://www.adobe.com/ca/acrobat/pdf-reader.html) in my Linux computer.

| **Status** &nbsp; | **Features** &nbsp;|
| -- | -- |
| &nbsp; &nbsp; ✅ | Form filling |
| &nbsp; &nbsp; ✅ | Comment tools |
| &nbsp; &nbsp; ✅ | Sticky notes |
| &nbsp; &nbsp; ✅ | Printing |
| &nbsp; &nbsp; ❌ | Signature |
<BR>

### Setup
- Arch Linux (up to May 2022)*
- Wine-stable 7.0

*The same configuration for __Wine__, __winetricks__ and __fonts__ should work in other Linux distributions.

### 1. Install wine-stable
Install [Wine](https://www.winehq.org/), the [stable version](https://aur.archlinux.org/packages/wine-stable) with either an [AUR helper](https://wiki.archlinux.org/title/AUR_helpers) or directly as below. Installation time ~25 minutes.
```
$ git clone https://aur.archlinux.org/wine-stable.git
$ cd wine-stable
$ makepkg -si
```
Once **Wine** is installed, run:
```
$ winecfg
```
set the **Windows Version** to `Windows 10`, leave all the other features with their default values.

### 2. Install winetricks
Install [winetricks](https://wiki.winehq.org/Winetricks) with all these "verbs". Installation time ~10 minutes.
```
# pacman -S winetricks
$ winetricks atmlib riched20 wsh57 mspatcha allfonts msftedit
```

### 3. Installing fonts
Fonts seem to be one of the major troubles to make AARDC workable with Wine.

* Add all the `.ttf` and `.otf` fonts to Wine:

    ```
    $ cd ${WINEPREFIX:-~/.wine}/drive_c/windows/Fonts && for i in /usr/share/fonts/**/*.{ttf,otf}; do ln -s "$i" ; done
    ```

* Add Microsoft Core fonts, download `EUupdate.EXE` from [https://sourceforge.net/projects/mscorefonts2/files/cabs/EUupdate.EXE/download](https://sourceforge.net/projects/mscorefonts2/files/cabs/EUupdate.EXE/download), and place it in `/home/USER/.cache/winetricks/eufonts`.

* Get the Windows 7 fonts, especially the __sego* fonts__ from [https://www.w7df.com/7/download.html](https://www.w7df.com/7/download.html). Copy the extracted files in `~/.fonts`, if it does not exist, create it. Update the font cache with:
```
# fc-cache -vf
```
and reboot

### 4. Installing Adobe Acrobat Reader DC
Download the installer for Windows 10 (I'm using the installer `AcroRdrDC1801120058_en_US.exe`)

* [http://get.adobe.com/uk/reader/otherversions/](http://get.adobe.com/uk/reader/otherversions/) or
* [ftp://ftp.adobe.com/pub/adobe/reader/win](ftp://ftp.adobe.com/pub/adobe/reader/win)

Proceed with the installation, but **DO NOT OPEN THE READER IT YET!**

Two keys in the [Wine registry](https://wiki.winehq.org/Regedit) have to be modified to avoid automatic updates in AAR-DC, run `$ wine regedit` and change the value of these two keys:

1. In `HKEY_LOCAL_MACHINE\Software\Wow6432Node\Adobe\Adobe ARM\Legacy\Reader\{AC76BA86-7AD7-1033-7B44-AC0F074E4100}` change the value of **Mode** to `0`.  

2. In `HKEY_LOCAL_MACHINE\Software\Wow6432Node\Adobe\Adobe ARM\1.0\ARM` change the value of **iCheckReader** to `0`.

Here, I have noticed that I need to **reboot** my computer, not sure why.

Now, open the Reader with the link created in the desktop or in the terminal with:
```
$ wine AcroRd32.exe
```
and select: *"Always open with Protected Mode Disabled"*

<HR>
This should be enough to have a working **Adobe Acrobat Reader DC in Linux**.
<center>
[<img src="/images/aardc.png" style="width: 800px;"/>](/images/aardc.png)  
</center>
