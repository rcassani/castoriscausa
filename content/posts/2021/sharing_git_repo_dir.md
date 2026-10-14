Title: Sharing a Git repository directory between Linux and Windows
Date: 2021-05-09 17:40
Tags: Windows, Linux, Git, GitHub  
Author: Raymundo Cassani
Slug: sharing-git-repo-dir
Thumbnail: git_dir_linux_windows.png

<center>
![Alt](/images/git_dir_linux_windows.png)  
</center>  

**Situation**: The setup is the following: my laptop has dual-boot setup with Linux and Windows, and a disk (NTFS) is shared between systems. I wanted to have a directory for a Git repository (in the shared disk) in such a way that:

1. It is possible to `pull` and `push` from it regarding the OS

2. The difference in the end-of-line characters (**CRLF** in Windows and **LF** in Linux) do not cause problems.

## The solution
To share the same repository folder with Windows and Linux, it's necessary to configure Git to properly handle the end-of-line characters.

* In Windows use:  
 `$ git config --global core.autocrlf auto`

* In Linux use:  
 `$ git config --global core.autocrlf input`

With this configuration when a file is added to the index in Windows, the `auto` configuration makes that all the CRLF are converted to LF, and that when the files are checked LF are converted to CRLF. As the repository directory is shared between OSs, when a file is edited in Windows (thus has CRLF) but is added to the index in Linux, the `input` configuration makes that the CRLF are converted into LF, but when the files are checked, the LF are **not** converted to CRLF. More info on Git configuration [here](https://git-scm.com/book/en/v2/Customizing-Git-Git-Configuration#_formatting_and_whitespace).
