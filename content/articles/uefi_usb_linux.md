Title: UEFI USB
Date: 2017-01-31
Category: Blog
Tag: Blog
Slug: linux-usb-uefi
Author: Ray Cassani

How to perform a **UEFI-bootable full installation of Linux in a USB (Flash Drive / External HDD)**, it is more trickier than expected.

Note. For sake of simplicity, I'll refer to a USB(Flash Drive / External HDD) as **USB disk**

This post is about creating a USB disk with Linux, capable of booting in UEFI. The procedure is performed in a computer running Windows without installing Linux in the HDD, nor modifying (messing with) the Windows EFI partition. Here a nice [explanation on UEFI boot](https://www.happyassassin.net/2014/01/25/uefi-boot-how-does-that-actually-work-then/).

First of all, if you're looking for Live-USB with or with Persistence, Legacy- and UEFI-bootable a nice option in Windows is [LinuxLive USB Creator](http://www.linuxliveusb.com/en/home). These are the [differences between Live-USB with Persistence and a USB Full Install](https://www.maketecheasier.com/persistent-live-usb-vs-full-install-usb/)

### Process Big Picture
The procedure comprehends three main parts:
1. Creating UEFI-booting Virtual Machine, without (virtual) HHD
2. Installing Linux in USB disk
3. Modifying the EFI partition in the USB disk

### Requirements
* [**VMware**](http://www.vmware.com/products/player/playerpro-evaluation.html) installed  
  The Workstation Player version is free for non-commercial use
* **USB disk**, USB3 if your computer supports it
  I've tried the procedure with both USB Flash Drive and External HDD
* **ISO image** of your favorite Linux distribution
  I used [Linux Mint](https://www.linuxmint.com/) 18.1 64-bit

### Procedure:
#### 1. Creating UEFI-booting Virtual Machine, without (virtual) HHD
  1. Open VMware and Create a New Virtual Machine
  2. Select "I will install the operative system later" option. Click Next.  
  [Image]()
  3. The Guest Operating System can be any, I'll select Linux, Ubuntu 64-bit.   Click Next.
  [image]()
  4. Virtual Machine name, Mint 64-bit. Click Next.  
  [image]()
  5. Disk Capacity, you can use the default parameters (this HDD will not be used).   Click Next.
  6. Click on Customize Hardware
    1. For the New CD/DVD (SATA), Select "Use ISO image file" and select you Linux ISO
	  2. For the USB Controller, Select USB 3.0, [X]Automatically ..., [ ]Show all... and [ ]Share Bluetooth...  
    Images2()
  7. Identify the Location of the Virtual Machine. Click on Finish
  8. Open the Virtual Machine location, open the file ```VMname.vmx``` with a text editor and add the line ```firmware = "efi"```
  9. On VMware, open your Virtual Machine settings and remove the HDD  
    [image]()

</br>
#### 2. Installing Linux in USB disk
  1. Power ON, VM, EFi was good it will look like this (at least for Mint)   
  [image]()
  2. Select Start Linux ...  
  [image]()
  3. Once Linux session is started, connect your USB-drive, and be sure, it's connected to the Virtual Machine  
  [image]()
  4. To start the procedure with a blank USB-drive, Openg Gparted. Select your device (remember which sdX it is) and Device/Create Partition Table, of the type ```gtp```. Close Gparted.  
  [image]()
  4. Click on the Install Linux (Mint) icon on Desktop.
    1. Select your language.
    2. Leave unchecked the option "Install the 3rd party drivers.."
    3. In "Installation type" select "Erase disk and install Linux Mint"
  5. One the installation is done, select "Continue Testing"

</br>
#### 3. Modifying the EFI partition in the USB disk
  1. Create a folder

        :::powershell
        $ sudo mkdir /mnt/efi/

  2. Mount the EFI partition

        :::powershell
        $ sudo mount /dev/sdX1 /mnt/efi
        $ cd /mnt/efi/EFI

  3. Copy the ubuntu folder to the same location with the name BOOT

        :::powershell
        $ sudo cp -r ./ubuntu/ ./BOOT/
        
  4. Copy the file X from to Y and Z

        :::powershell
        $ sudo cp /media/cdrom/EFI/BOOT/BOOTx64.EFI ./BOOT/

After this steps your boo UEFI from USB

I've try this method using a SSD connected via USB and a Lexa memory

Future work:
Steps to mount your USB-system in a virtual machine (this is not efficient, but can be useful to retrieve important information)

Multi-boot
