Title: poshbash in Windows bash
Date: 2016-10-26 22:00
Category: Blog
Tags: Windows, Git
Slug: poshbash-windows-bash
Author: Raymundo Cassani
Thumbnail: posh_bash_win.png

The [**posh-git-bash**](https://github.com/dahlbyk/posh-git) prompt, for [Git](https://git-scm.com/), is a useful tool that shows information about the current status of a local Git repository respect to local and remote (e.g. [GitHub](https://github.com/)) repositories; in this way, it's easy to see if the repository is ahead or behind, has uncommitted changes, is up-to-date, etc.

<center>
![Alt](/images/posh_bash_win.png)  
Git-Posh example
</center>  

The **posh-git-bash** prompt is included in the [PowerShell](https://msdn.microsoft.com/en-us/powershell/mt173057.aspx) installed with [GitHub Desktop](https://desktop.github.com/) software for Windows. This post describes how add the **posh-git-bash** prompt functionality into the [Bash on Windows10](https://msdn.microsoft.com/en-us/commandline/wsl/about#).

If **Bash on Windows** is not already installed, this is the [installation guide](https://msdn.microsoft.com/commandline/wsl/install_guide).

---
##### **Note**: Enable Copy/Paste in Bash
1. Right click in the Window Title bar &gt; Properties
2. Enable Quick Edit Mode
3. Copy is **Ctrl-C** and Paste is **Right-click**

---

### **Adding posh-git-bash** prompt to Bash on Windows

1. Run Bash and go to HOME directory in bash

        :::bash
        $ cd ~

2. Download the file ```git-prompt.sh``` from [this repository](https://github.com/lyze/posh-git-sh.git), and rename it as ```.git-prompt.sh```  

        :::bash
        ~$ wget https://raw.githubusercontent.com/lyze/posh-git-sh/master/git-prompt.sh -O .git-prompt.sh

3. Now you need to edit your the file ```~/.bashrc```
Add the following 2 lines at the beginning of ```~/.bashrc file```, you can use the text editors [nano](https://www.nano-editor.org/) or [vim](http://www.vim.org/) for this.

        :::bash
        source ~/.git-prompt.sh
        PROMPT_COMMAND='__posh_git_ps1 "\u@\h:\w" "\\\$ ";'$PROMPT_COMMAND

4. Restart Bash

<!-- Reference links https://msdn.microsoft.com/en-us/commandline/wsl/about https://msdn.microsoft.com/en-us/commandline/wsl/reference https://msdn.microsoft.com/en-us/commandline/wsl/user_support https://msdn.microsoft.com/en-us/commandline/wsl/faq https://msdn.microsoft.com/commandline/wsl/install_guide http://www.digitalcitizen.life/how-get-linux-bash-windows-10-3-steps https://twitter.com/richturn_ms https://twitter.com/hashtag/bashonubuntuonwindows?src=hash https://blogs.windows.com/buildingapps/2016/07/22/fun-with-the-windows-subsystem-for-linux/ https://en.support.wordpress.com/markdown-quick-reference/ -->
