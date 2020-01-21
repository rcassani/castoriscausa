Title: Universal Shortcut
Date: 2017-07-25 19:00
Category: Programming
Tags: Linux, Windows, Bash, Batch
Slug: universal-shortcuts
Author: Raymundo Cassani


This project started from the "need" of having a compatible way to point to files indifferently if on Windows or Linux. While both operative systems can handle symbolic links, when the target file is an executable, certain scripts and programs present [problems when executed through a symbolic link](https://askubuntu.com/questions/541317/link-to-exe-doesnt-launch-wine), as the working directory is expected to be the directory containing the executable  and not the directory with the symbolic link.

For that reason, a different approach was taken. To create an hybrid script with **Bash** and **Batch** code to point to the desired files or program. This kind of script is possible by using the commenting format of [Batch files to ignore the Bash commands](https://stackoverflow.com/questions/17510688/single-script-to-run-in-both-windows-batch-and-linux-bash). In this sense such files can are **universal shortcuts**. As the paths utilized in this universal shortcut file, are relative, it works perfectly with portable media, if and only if, the filesystem supports file permissions. Note: FAT32 does not support them.

The universal shortcuts consist of an executable script file with Bash and Batch code. When executed in Windows the Bash part is ignored and when executed in Linux the Batch part is ignored. Thus, the same script can be executed in both systems and performs the same action.

The scripts in bash and batch are equivalent and they do:  

1. Change the current directory to the directory where the target file is

2. Open the target file in a similar way as when the user double clicks it, this operation [depends on the Desktop Environment utilized](https://github.com/alexeevdv/dename/blob/master/dename.sh)

3. Exit

The universal shortcut is created by a Python 3 script that can be found in this repository:

[https://github.com/rcassani/universal-shortcuts](https://github.com/rcassani/universal-shortcuts)

### Usage

    :::bash
    $ python3 mk_unishortcut.py <targetpath>

the `<targetpath>` can be absolute or relative, and can be a file or directory

When the Python script is executed in Linux it will automatically change the file permissions of the shortcut file to be executable. If the Python script is run in Windows, it is needed to change the file permissions to executable in Linux.  

Despite the fact these universal shortcuts may not be extremely useful, this project was an interesting experience in writing hybrid Bash-Batch scripts.


## References:
1. Symbolic links fail to run executable files when they need to run in their folder  
  [https://askubuntu.com/questions/541317/link-to-exe-doesnt-launch-wine](https://askubuntu.com/questions/541317/link-to-exe-doesnt-launch-wine)

2. Hybrid Windows-bash and Linux-bash scripting  
  [https://stackoverflow.com/questions/17510688/single-script-to-run-in-both-windows-batch-and-linux-bash](https://stackoverflow.com/questions/17510688/single-script-to-run-in-both-windows-batch-and-linux-bash)

1. Identify Linux Desktop Environment  
  [https://github.com/alexeevdv/dename/blob/master/dename.sh](https://github.com/alexeevdv/dename/blob/master/dename.sh)   

4. `start` command in Windows  
  [https://technet.microsoft.com/en-us/library/cc770297(v=ws.11).aspx](https://renewablepcs.wordpress.com/about-linux/kde-gnome-or-xfce/)

5. Link with different Desktop Environments  
  [https://renewablepcs.wordpress.com/about-linux/kde-gnome-or-xfce/](https://renewablepcs.wordpress.com/about-linux/kde-gnome-or-xfce/)
