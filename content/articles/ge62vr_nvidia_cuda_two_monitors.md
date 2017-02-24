Title: Mint18 + GE62VR + GTX1060 + CUDA
Date: 2017-02-21 19:00
Category: Blog
Tag: linux, gpu, nvidia, cuda
Slug: ge62vr-mint-gtx1060
Author: Ray Cassani

There are several posts with the instructions for properly installing NVIDIA drivers in Linux; unfortunately, sometimes they're outdated, moreover it's not possible to cover the inmensity of system configurations. After searching, reading and destilating some of that information, I came down to this guide for my system (**Mint18** in **MSI-GE62VR**)`*`. The guide consists of two parts:

1. Install NVIDIA drivers
2. Install and test CUDA drivers.

`* Similar steps should apply for other dual monitor setups in Ubuntu and Ubuntu-based distributions.`

## System: [MSI GE62VR](https://www.msi.com/Laptop/GE62VR-6RF-Apache-Pro.html)
#### Operative System
* [Linux Mint 18](https://www.linuxmint.com/) 64-bit (Cinnamon)

#### Hardware
* [GTX 1060](https://www.nvidia.com/en-us/geforce/products/10series/laptops/#specs)
* [Intel HD Graphiocs 530 (integrated GPU)](https://en.wikipedia.org/wiki/Intel_HD_and_Iris_Graphics#Skylake)

## 1 Install NVIDIA driver


If the laptop's screen and external screen are working properly go to the CUDA section.

It seems that common problems at installing NVIDIA drivers in Mint (and Ubuntu) are: the laptop's monitor is disabled when a external monitor is connected; or Cinnamon crashes in "fallback mode" when the system boots without external the monitor.

So far the solution that worked for me, is to change to novoue drivers, purge and perform a clean NVIDIA installation

* Change the drivers to nouveou. Open the **Driver Manager**, and verify that the utilized drivers are the **Nouveau display driver** (change fron NVIDIA to it if necessary)

* Once in nouvou driver, purge the NVIDIA drivers

		:::bash
		$ sudo apt-get purge nvidia*
		$ sudo apt-get update
		$ sudo apt-get upgrade

* Unplug the DigitalDisplay adapter
* Open the **Driver Manager** select the recommened **NVIDIA bianry driver** (nvidia-367 at 08/feb/2017)
* Restart
* Everything should work normal
* Connectthe DigitalDisplay adapter
* Now you can open XNVDIA to configure the monitor

A problem I've found is that, booting the system with external monitor connectedn , makes it primary and it's not possible that configuration from 'Screens'

## 2 Install and Test CUDA drivers
Once the NVIDIA drivers are properly installed, it's time to install the CUDA drivers. If you're not sure what's the CUDA driver check this link.

* Download the CUDA drivers. [Link](https://developer.nvidia.com/cuda-downloads)
Linux / x86_64 / Ubuntu / 16.04 / runfile(local)
[image]

* Change the downloaded file to exectable and execute it

		:::bash
		$ chmod +x cuda_8.0.61_375.26_linux.run
		$ sudo sh cuda_8.0.61_375.26_linux.run --override


* Installation parameters, according to your *desire*? Select NO when the CUDA installer ask to install **NVIDIA Accelerated Graphics Driver for Linux** as the NVIDIA driver is already installed.

Screenshot of the installation


* Prepare the CUDA environment, add the following 3 lines to your .bashrc file

		:::bash
		export CUDA_HOME=/usr/local/cuda    
		export LD_LIBRARY_PATH=/usr/local/cuda/lib64:$LD_LIBRARY_PATH
		export PATH=/usr/local/cuda/bin:$PATH

* And source it

		:::bash
		$ source ~/.bashrc

<!---
An alternavive for CUDA environment is:
Create the file `/etc/profile.d/cuda.sh` with the line
export PATH=$PATH:/usr/local/cuda/bin
Create the file `/etc/ld.so.conf.d/cuda.conf` with the line
/usr/local/cuda/lib64
$ sudo ldconfig
-->

* Verify Cuda Compiler driver

		:::bash
		$ nvcc --version

		nvcc: NVIDIA (R) Cuda compiler driver
		Copyright (c) 2005-2016 NVIDIA Corporation
		Built on Tue_Jan_10_13:22:03_CST_2017
		Cuda compilation tools, release 8.0, V8.0.61

* Install g++ (If you haven't)

		:::bash
		$ sudo apt-get install g++
		$ sudo apt-get install build-essential
		$ sudo apt-get install make

* Optional, from NVIDIA Guide. Install additional libraries to be able to build most of the samples:

		:::bash
		$ sudo apt-get install freeglut3-dev build-essential libx11-dev libxmu-dev libxi-dev libgl1-mesa-glx libglu1-mesa libglu1-mesa-dev

</br>
**Building the samples.** Several of the samples requiere GL libraries, to find the correct path for those libraries, the file `fingllib.mk` is used. As Mint is not an officially supported distribution a slight change is necessary in the `fingllib.mk` file. To avoid editing all instances of this file, the multiple instances will be replaced a symbolic link.

* Move to common folder in the samples path

		:::bash
		$ cd /usr/local/cuda/samples/common

* Open `fingllib.mk` and, in the line 62 change `ubuntu` for `'ubuntu\|linuxmint'`

* Search for all the instances of `fingllib.mk` outside of /common/ and replace them with a symbolic link to `/common/fingllib.mk`.

		:::bash
		$ cd /usr/local/cuda/samples/common
		$ sudo find .. ! -path "*/common*" -name findgllib.mk -exec ln -sf /usr/local/cuda/samples/common/findgllib.mk {} ';'

* Run the commnad `make`

		:::bash
		$ cd /usr/local/cuda/samples
		$ sudo make

* Running Sample binaries

		:::bash
		$ cd /usr/local/cuda/samples/bin/x86_64/linux/release
 Verify that your CUDA Capable device is found

		:::bash
		$ ./deviceQuery

		./deviceQuery Starting...

 		CUDA Device Query (Runtime API) version (CUDART static linking)

		Detected 1 CUDA Capable device(s)

		Device 0: "GeForce GTX 1060"
  		CUDA Driver Version / Runtime Version          8.0 / 8.0
  		CUDA Capability Major/Minor version number:    6.1
  		...

	Sample `fluidsGL`

		:::bash
		$ ./fluidsGL

Use CUDA drivers from python

####References

http://blog.csdn.net/kernlen/article/details/53882490

http://blog.csdn.net/wopawn/article/details/52302164

http://blog.csdn.net/lee_j_r/article/details/52693724

http://www.voidcn.com/blog/u010696366/article/p-3712151.html
http://stackoverflow.com/questions/34617236/cuda-missing-libgl-so-libglu-so-and-libx11-so

https://www.pugetsystems.com/labs/hpc/NVIDIA-CUDA-with-Ubuntu-16-04-beta-on-a-laptop-if-you-just-cannot-wait-775/

http://docs.nvidia.com/cuda/cuda-installation-guide-linux/#axzz4Y9Whzcjf

https://devtalk.nvidia.com/default/topic/936429/-solved-tensorflow-with-gpu-in-anaconda-env-ubuntu-16-04-cuda-7-5-cudnn-/

http://developer.download.nvidia.com/compute/cuda/6_5/rel/docs/CUDA_Getting_Started_Linux.pdf

https://forums.linuxmint.com/viewtopic.php?t=226145

[_](123.com)

conda env list | awk 'NR==6{print $1}'
