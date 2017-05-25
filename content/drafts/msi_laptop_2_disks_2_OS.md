Title: asdasd
Date: 2017-01-31
Category: Blog
Tag: Blog
Slug: slug-slug
Author: Ray Cassani

If you computer has two Disk Drives, and you want to try two operative systems, one option will be install them in the same disk, alternatively, it's possible to install each one in it's own Drive, with this there is no need of boot managers as Grub or Grub2. By having OS in differnt Drives
change either in BIOS or some mother boards allows to change the boot order on-the-flight

There are easy ways to do this, for example:

* Disconnect physically one Drive, and install Linux in the desired Drive
* If the BIOS allows, it disable one Drive, then proceed to install Linux in the desired Drive

However, if you don't want to open the laptop to disconnect physically the disk, as this voids warranty, and The BIOS does not allows to disable one Disk
You can follow the process presented in this post

## Overview of the Process
1. Make a full installation of your desired Linux distro in a USB, make sure it boots in UEFI, a (4 - 16GB) will be perfect
2. Create some space for Linux in the target disk
3. Copy the partions from the USB to the Disk
4. Resize the Linux partitions in the Target Disk to take advantage of all the available space.

## Requirements
* USB 1 (For full linux)
* USB 2 (For live linux)
* HDD 1 (Where Windows 10 lives)
* HDD 2 (Usually for data, but here we'll install linux)

## Process

### 1. Full intallation of Linux in USB
You can do this following the instructions provided in this post:
[http://post.com]

### 2. Create space for Linux and Copy partitions
1. Create a live linux USB
with LinuxLive Creator
Ask Joao M about his Ubuntu
2. Boot with the live USB, resize the current partitions in DD desired
3. Plug in the USB1
4. Copy the partitions EFI, xx and Swap in the empty space
5. Resize the xx partition
6. Apply changes




This post is about creating a UEFI-bootable full Linux installation in a USB Flash Drive or External HDD. For sake of simplicity, I'll refer to a **USB Flash Drive** or a **USB External HDD** as **USB-disk**. This procedure is performed in a computer running Windows without installing Linux in the HDD, therefore there is no modification (nor mess) in the Windows EFI partition. Here a nice [explanation on how UEFI boot works](https://www.happyassassin.net/2014/01/25/uefi-boot-how-does-that-actually-work-then/).

First of all, if you're looking for **Live-USB** with or without **Persistence** with both **Legacy** and **UEFI** boot, a nice option in Windows is [LinuxLive USB Creator](http://www.linuxliveusb.com/en/home). These are the [differences between Live-USB with Persistence and a USB Full Install](https://www.maketecheasier.com/persistent-live-usb-vs-full-install-usb/).

### Process Big Picture
The procedure comprehends three main parts:  

1. Creating UEFI-booting Virtual Machine, without (virtual) HHD
2. Installing Linux in the USB-disk
3. Modifying the EFI partition in the USB-disk

### Requirements
* [**VMware**](http://www.vmware.com/products/player/playerpro-evaluation.html) installed  
  The *Workstation Player* version is free for non-commercial use
* **USB-disk**, USB3 if your computer supports it
  I've tried the procedure with both USB Flash Drive and External HDD
* **ISO image** of your favorite Linux distribution

For the following steps an ISO image of [**Linux Mint**](https://www.linuxmint.com/) **18.1 64-bit** was used, similar instructions should apply for other distributions.

### Procedure:
#### 1. Creating UEFI-booting Virtual Machine, without (virtual) HHD
  1. Open **VMware** and **Create a New Virtual Machine**
    <center>
    <img src="../images/uefi_usb_1_1.png" style="width: 500px;"/>
    </br>  
    </center>
  2. Select the **I will install the operative system later** option. Click on **Next**
    <center>
    <img src="../images/uefi_usb_1_2.png" style="width: 500px;"/>
    </br>  
    </center>
  3. Set **Guest Operating System** to Linux, select your version or the closest one, in my case the closest to **Mint 64-bit** is **Ubuntu 64-bit**. Click on **Next**
    <center>
    <img src="../images/uefi_usb_1_3.png" style="width: 500px;"/>
    </br>  
    </center>
  4. Assign a name and location to the Virtual Machine. Click on **Next**  
    <center>
    <img src="../images/uefi_usb_1_4.png" style="width: 500px;"/>
    </br>  
    </center>
  5. **Disk Capacity**, default parameters (this HDD will not be used). Click **Next**
    <center>
    <img src="../images/uefi_usb_1_5.png" style="width: 500px;"/>
    </br>  
    </center>
  6. Click on **Customize Hardware**
    1. For the **New CD/DVD (SATA)**, Select **Use ISO image file** and browe for your Linux ISO image
      <center>
      <img src="../images/uefi_usb_1_6a.png" style="width: 500px;"/>
      </br>  
      </center>
	  2. For the **USB Controller**, Select **USB 3.0** (if supported), **[X]Automatically ..., [ ]Show all... and [ ]Share Bluetooth...**
      <center>
      <img src="../images/uefi_usb_1_6b.png" style="width: 500px;"/>
      </br>  
      </center>
  7. Before completing the wizard, identify the **Location** of the Virtual Machine. Click on **Finish**. Do not power ON the Virtual Machine yet.
  8. Go to the Virtual Machine **Location**, and with help of a text editor (e.g. Notepad), open the file **```VMname.vmx```** and add the line **```firmware = "efi"```** at the end of the file
  9. In **VMware**, open the **settings** of your brand new Virtual Machine and **remove the HDD**
    <center>
    <img src="../images/uefi_usb_1_9.png" style="width: 500px;"/>
    </br>  
    </center>  

#### 2. Installing Linux in USB-disk
  In the step, the Virtual Machine will boot in UEFI using the Linux ISO image, from there it'll possible to install Linux in the USB-disk.
  1. In **VMware**, Power ON the Virtual Machine. When booting on UEFI, it should look as below (at least for **Mint 64-bit**). Select **Start Linux Mint 18 Cinnamon 64-bit**
    <center>
    <img src="../images/uefi_usb_2_1.png" style="width: 700px;"/>
    </br>  
    </center>
  2. Once the Linux session is started, connect (physically) your USB-disk, and be sure it's connected to the Virtual Machine  
    <center>
    <img src="../images/uefi_usb_2_3.png" style="width: 700px;"/>
    </br>  
    </center>
  3. To start the procedure with a blank USB-disk. In the Virtual Machine, Open **GParted** (hopefully is installed). Then select your device at the upper right corner (remember its **sdx**), then go to **Device > Create Partition Table**, select the type **gtp**. Close GParted.  

  4. Click on the **Install Linux** (Mint) icon on Desktop.
    1. Select your language.
    2. Leave unchecked the option **Install third-party software...**
    3. In **Installation type** select **Erase disk and install Linux Mint**
  5. One the installation is done, select **Continue Testing**

</br>
#### 3. Modifying the EFI partition in the USB-disk
  Still in the Linux session (Virtual Machine without HDD booted with Live-CD) from the previous section, the remaining part is to prepare the EFI partition on the USB-disk to make it UEFI-bootable  

  1. Create a folder ```/mnt/efi/```
        :::powershell
        $ sudo mkdir /mnt/efi/

  2. Mount the EFI partition in the recently created folder. Change **sdx** for the corresponding to your USB-disk (step 4 in previous section)

        :::powershell
        $ sudo mount /dev/sdx1 /mnt/efi
        $ cd /mnt/efi/EFI

  3. Copy the **ubuntu** folder to the same location with the name **BOOT**

        :::powershell
        $ sudo cp -r ./ubuntu/ ./BOOT/

  4. Finally, copy the file **```BOOTx64.EFI```** from to the **Linux ISO image**  to the **BOOT** folder in **EFI** partition of the USB-disk

        :::powershell
        $ sudo cp /media/cdrom/EFI/BOOT/BOOTx64.EFI ./BOOT/

  5. Shut down the Virtual Machine properly.

</br>
<center>
### **Congratulations, now your USB-disk should be UEFI-bootable**
</center>
</br>

Finally, reboot your computer, and select the USB-disk (Partition 1) for UEFI boot.

I've try this method using an [external SSD via USB](https://www.amazon.ca/Kingston-Upgrade-2-5-Inch-SH103S3B-120G/dp/B007R9M6PO/ref=sr_1_5?s=electronics&ie=UTF8&qid=1486057544&sr=1-5&keywords=kingston+hyperx+120) and a [Lexar USB flash drive](https://www.amazon.ca/Lexar-JumpDrive-128GB-Flash-Drive/dp/B012PKV7RC/ref=sr_1_11?s=pc&ie=UTF8&qid=1486057469&sr=1-11) without issues.
