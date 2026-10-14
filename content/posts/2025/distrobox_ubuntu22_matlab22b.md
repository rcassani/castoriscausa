Title: Distrobox: Ubuntu container with Matlab
Date: 2025-08-12 13:15
Tags: Arch, Linux, Matlab, GPU, NVIDIA, tutorial
Author: Raymundo Cassani
Slug: distrobox-matlab22b-ubuntu22
Thumbnail: distrobox_ubuntu_matlab.png

[I use Arch (BTW)](https://knowyourmeme.com/memes/btw-i-use-arch), so my OS has up-to-date software and packages. Unfortunately, this also means that Matlab (which is not officially supported in [Arch Linux](https://archlinux.org/)) can be a real headache to install and run, especially older versions as they relied in "older" libraries.

In the last years, I tried debugging and fiddling endlessly with libraries and dependencies to get Matlab to work. Many times with help of the [ArchForums](https://bbs.archlinux.org/), this activity quickly became a huge time sink as often I needed different fixes for different Matlab versions. To be honest, I even considered switching permanently to [Ubuntu](https://ubuntu.com/) just to avoid these headaches. 

However, that migration will not be needed 😌, as recently [Distrobox](https://distrobox.it/) crossed my path and it completely changed the game.

In a nutshell, Distrobox creates a containerized environment based on an Ubuntu release that Matlab officially supports. Then, Matlab runs inside that container as if it were the native Ubuntu, but I still have seamless access to my home directory (and other files) because the container shares those with the host. On top of that, NVIDIA GPU support works out of the box with minimal fuss, so Matlab GPU-accelerated features run smoothly without complicated setup.

## Distrobox: Ubuntu 22.04 with Matlab 2022b
<BR>
### A. In the host
1. Install [distrobox](https://wiki.archlinux.org/title/Distrobox) and [podman](https://wiki.archlinux.org/title/Podman) (preferred, though Docker could be used):

        :::bash
        $ sudo pacman -S distrobox podman

2. Create the Ubuntu container with NVIDIA support (if needed):

        :::bash
        $ distrobox create --image ubuntu:22.04 --name ubuntu-2204-nvidia --nvidia

3. Enter the container:

        :::bash
        $ distrbox enter ubuntu-2204-nvidia

### B. In the container
1. Install additional Ubuntu packages that Matlab 2022b needs:

        :::bash
        $ sudo apt-get install libnss3 libatk-bridge2.0-0 libasound2 libxt6 libxft2 libsndfile1

    the list of required Ubuntu packages may grow depending on the Matlab features that are required.  
    I'll keep updating this list as I encounter missing packages.

4. Download the Matlab installer, unzip it and run the `install` script.  
    Use the default installation path: `/usr/local/MATLAB/R2022b`

        :::bash
        $ sudo ./install

5. Create a symbolic link (so the binary has a different name from `matlab`):

        :::bash
        $ sudo ln -s /usr/local/MATLAB/R2022b/bin/matlab /usr/local/bin/matlab22b

6. Once Matlab is installed in the Ubuntu container, it be exported to the host for easy execution:

        :::bash
        $ distrobox-export --bin /usr/local/bin/matlab22b --export-path ~/.local/bin

### C. On the host again
1. Just run

        :::bash
        $ matlab22b

    the Ubuntu container will be started and `matlab22b` will be executed on it.

## Conclusion
Distrobox for running Matlab versions on Arch is a simple and clean solution that avoids dependency issues and host system changes.

