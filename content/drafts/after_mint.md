Title: After Mint
Date: 2016-12-06 19:00
Category: Blog
Tag: Template
Slug: template
Author: Ray Cassani
Lang: spa

This happens after following my steps ii Castoris Causa
Mint 18 in GE62VR

-------------
Lid behaviour
-------------
System Settings / Power

-----------------------------
Add getdeb as Software Source
------------------------------
http://www.getdeb.net/updates/ubuntu/16.10/

	$ sudo apt-get update

---------------------------
To Mint that the hardware (BIOS) clock is set to 'local' time
--------------------------------------------------------------
	$ timedatectl set-local-rtc 1

-------------------
Update and Upgrade
-------------------
	$ sudo apt-get update
	$ sudo apt-get upgrade

----------
KeePassX
-----------
	$ sudo apt-get install keepassx
------------------------------------------------------
Remmina (remote desktop) with RDP (Remote Desktop Protocol) Windows
-------------------------------------------------------
Install V 1.2

  $ sudo add-apt-repository ppa:remmina-ppa-team/remmina-next
	$ sudo apt-get update
	$ sudo apt-get install remmina remmina-plugin-rdp libfreerdp-plugins-standard

---------------------------------
Add seconds layout to keyboard
--------------------------------
	English (US, international with dead keys)
	Any WinKey + Space to change layout (same as in windows)

---------------
NVIDIA Setup
http://blog.csdn.net/kernlen/article/details/53882490
-----------------

Unplug the DigitalDisplay adapter
Open Driver Manager (367  08/feb/2017), select the recommened for NVIDIA
Restart
Everything should work normal
Connectthe DigitalDisplay adapter

CUDA
https://www.pugetsystems.com/labs/hpc/NVIDIA-CUDA-with-Ubuntu-16-04-beta-on-a-laptop-if-you-just-cannot-wait-775/
http://docs.nvidia.com/cuda/cuda-installation-guide-linux/#axzz4Y9Whzcjf
https://devtalk.nvidia.com/default/topic/936429/-solved-tensorflow-with-gpu-in-anaconda-env-ubuntu-16-04-cuda-7-5-cudnn-/
http://developer.download.nvidia.com/compute/cuda/6_5/rel/docs/CUDA_Getting_Started_Linux.pdf

Download CUDA drivers
https://developer.nvidia.com/cuda-downloads
Linux / x86_64 / Ubuntu / 16.04 / runfile(local)
	$ chmod +x cuda_8.0.61_375.26_linux.run
	$ sudo sh cuda_8.0.61_375.26_linux.run --override
Accept EULA
You are attempting to install on an unsupported configuration. Do you wish to continue? (y)
Install NVIDIA Accelerated Graphics Driver for Linux-x86_64 375.26? (n)
IMAGE

Set up ~/.bashrc
$ sudo nano ~/.bashrc
export CUDA_HOME=/usr/local/cuda    
export LD_LIBRARY_PATH=/usr/local/cuda/lib64:$LD_LIBRARY_PATH
export PATH=/usr/local/cuda/bin:$PATH

Environment Variables:

$ sudo nano /etc/profile.d/cuda.sh
export PATH=$PATH:/usr/local/cuda/bin

$ sudo nano /etc/ld.so.conf.d/cuda.conf
/usr/local/cuda/lib64

$ sudo ldconfig
$ source ~/.bashrc

Verify Cuda Compiler driver
$ nvcc --version

Install g++
$ sudo apt-get install g++
$ sudo apt-get install build-essential
$ sudo apt-get install make

Optional Libraries to build all the samples:
$ sudo apt-get install freeglut3-dev build-essential libx11-dev libxmu-dev
 libxi-dev libgl1-mesa-glx libglu1-mesa libglu1-mesa-dev

Build samples
$ cd /usr/local/cuda/samples
$ sudo make

Run binaries
$ cd /usr/local/cuda/samples/bin/x86_64/linux/release
 Verify that your CUDA Capable device is found
 $ ./deviceQuery

 bandwidthTest
 $ ./bandwidthTest

------------
Atom
------------
Download and install Atom
Configuring Atom

$ apm install script
https://github.com/rgbkrk/atom-script

For python synthaxis, this should be done for each environment
$ apm install linter
$ pip install flake8
$ pip install flake8-docstrings
$ apm install linter-flake8

Preferences (Settings) / Install / search for packages:

Minimap
File icons


-----------
Anaconda or Miniconda
-----------
With these changes:

- By defualt the system will use python/python2 and python3 located at usr/bin/
- This location will be used when installing new software requires python
- you can check which python is being used with which python, and all the python versions available with type -a python

Download Anaconda(3) or Miniconda(3) for Linux 64-bit version

Install Anaconda3 or Miniconda3
	$ bash Anaconda3-4.3.0-Linux-x86_64.sh
	or
	$ bash Miniconda3-latest-Linux-x86_64.sh

Do NOT add the Anaconda / Miniconda directory to the PATH in .bashrc file

Go to Anaconda3 / Miniconda3 bin directory and create an empty environment
	$ cd /home/cassani/miniconda3/bin
	$ ./conda create --name empty-env

You may want to create a symbolic link in ~/miniconda3/envs/empty-env/bin for conda-env
	$ ln -s /home/cassani/miniconda3/bin/conda-env conda-en

Open your .bashrc file (located at /home/user)
	export PATH="/home/cassani/miniconda3/envs/empty-env/bin":$PATH

In Anaconda3 clone the root environment as anaconda3
	$ conda create --name anaconda3 --clone root

In Miniconda3 you can create an anaconda3 environment
	$ conda create --name anaconda3 python=3 anaconda

In order to use your anaconda environment it's necessary to activate it
	$ source activate anaconda35

To return to the system pythons deactivate any environment

Note that if you do $ source activate root, the Anaconda /Miniconda path will be prepended to $PATH and python will the the one there



Ref:
https://groups.google.com/a/continuum.io/forum/#!topic/anaconda/opMLiGnjymE
https://conda.io/docs/using/envs.html#share-an-environment
https://github.com/conda/conda/issues/1022


----------
QTodoTxt
----------
Download it from the GitHub repository
https://github.com/QTodoTxt/QTodoTxt

In terminal run
sudo apt-get update
sudo gebi

Install .deb package qtodotxt_package.deb
The version 1.6.11 is missing does not mention the dependecy python3-dateutil, to install it:

sudo apt-get -y install python3-dateutil

-------------------
Git, GitHub and git-posh
-------------------
Install (update) Git
	$ sudo apt-get install git
Configure username and email, quotes are required
  	$ git config --global user.name "user_name"
  	$ git config --global user.email "email_id"
Optional, create a GitHub directory in /home/user
	$ mkdir /home/cassani/GitHub
Run the following line to clone the GitHub repository in a directory with the same name
	$ git clone https://github.com/rcassani/project_euler.git

To get Git poshbash
Download poshbash.sh in ~
	$ wget https://raw.githubusercontent.com/lyze/posh-git-sh/master/git-prompt.sh
	$ mv git-prompt.sh .git-prompt.sh
In ~/.bashrc file, add:
	source ~/.git-prompt.sh    
	PROMPT_COMMAND='__posh_git_ps1 "\u@\h:\w" "\\\$ ";'$PROMPT_COMMAND
	or
	PROMPT_COMMAND='__posh_git_ps1 "\[\033[01;32m\]\u@\h\[\033[00m\] \[\033[01;34m\]\w\[\033[00m\]" "\[\033[01;34m\] \$\[\033[00m\] ";'$PROMPT_COMMAND
The second version of PROMPT_COMMAND keeps the color used in Mint, these colors can be found in the same ~/.bashrc file
See post about modifications


-------------------
AIMP and Wine
-------------------
1. Install the newst version of Wine (1.8 @ 16 Feb 2017)
$ sudo add-apt-repository ppa:ubuntu-wine/ppa
$ sudo apt-get update
$ sudo apt-get install wine1.8

2 In the Menu, open Configure Wine
Install what is requiered: Mono and Gecko

3. Download the installer for AIMP4 ( AIMP v4.13, build 1886)
Right click on it and Open With -> Wine Windows Program Loader
Follow the instalation instructions, don't select the portable version

A AIMP icon will apperar on Desktop

-------------
VPN INRS
-------------
1. In Network, create a new VPN, PPTP
Gateway = server IP
2. Go to Advanced...
Select "Use Point-to-point encryption (MPPE)"
