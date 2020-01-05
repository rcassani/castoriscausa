Title: Linux freezes when changing GPU with prime-select [Solved]
Date: 2017-08-29 12:00
Category: Blog
Tags: Linux, GPU, NVIDIA
Slug: freezes-linux-gpu-acpi
Author: Raymundo Cassani

A frequent problem in dual-GPU systems is that the PC freezes ([kernel panic]()) when you try to logout, restart or shutdown after changing back from the **Intel** (integrated) to the **NVIDIA** (discrete) GPU in Linux. All of this when you're using the **NVIDIA drivers** (proprietary drivers).

When using the [NVIDIA drivers](http://www.castoriscausa.com/posts/ge62vr-mint-gtx1060) for Linux, it's possible to change the GPU in use with the `prime-select` command followed by logout.

Switching from **NVIDIA** to **Intel** GPU works perfectly:

    :::bash
    $ sudo prime-select intel

Then logout and login to see the changes. By changing to the discrete GPU power consumption drops almost by half, providing a decent battery life in laptops.

However, the **kernel panic** occurs when switching back from the **Intel** to **NVIDIA** GPU.

    :::bash
    $ sudo prime-select nvidia

After changing the GPU with `prime-select`, either logout, restart or shutdown will result in kernel panic.

## Solution
The problem is likely to be cause by [ACPI](https://en.wikipedia.org/wiki/Advanced_Configuration_and_Power_Interface) configuration in the kernel boot sequence. It can be **solved** by adding the following to the kernel boot sequence:

`acpi_osi=! acpi_osi="Windows 2009"`

This can be done by [editing the kernel boot parameters](https://www.howtoforge.com/tutorial/kernel-boot-parameter-edit/), or more convenient and easier with the help of  [GrubCustomizer](https://launchpad.net/grub-customizer).

<br>
After than change you should be able to logout correctly after changing from the **Intel** to the **NVIDIA** GPU.

### References

[https://bugs.launchpad.net/lpbugreporter/+bug/752542/comments/793](https://bugs.launchpad.net/lpbugreporter/+bug/752542/comments/793)

[https://github.com/Bumblebee-Project/Bumblebee/issues/764#issuecomment-234494238](https://github.com/Bumblebee-Project/Bumblebee/issues/764#issuecomment-234494238)
