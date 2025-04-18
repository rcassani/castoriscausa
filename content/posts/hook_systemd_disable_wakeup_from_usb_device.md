Title: Hook with systemd to disable wake-up from USB device
Date: 2020-03-09 17:32
Modified: 2022-05-18 14:00
Tags: Arch, Linux, systemd
Author: Raymundo Cassani
Slug: hook-systemd-disable-wakeup-from-usb-device
Thumbnail: systemd_cat.jpg

**Situation:** When my laptop is in suspension with the lid open, any update (movement or clicks) with the wireless mouse wakes-up the laptop. This post is about creating a `systemd` unit, and hook it to the start of the sleep unit, and disable the mouse as wake-up device. This approach should work for any Linux distribution using `systemd`, this post was written in a [Arch Linux](https://www.archlinux.org/) system.

<center>
![Alt](/images/systemd_cat.jpg)  
</center>  

First, the list of devices that can wake-up the computer can be find with:

	:::bash
	$ grep enabled cat /proc/acpi/wakeup

From this list, it can be seen that the culprit device is **XHC**, which is a USB 3.0 (XHC) chip. The listed devices can be toggled to `disabled` with the folliwing command:

	:::bash
	# echo XHC > /proc/acpi/wakeup

This has to be as root, if `sudo` does not work, use `sudo su` and run the command.

Unfortunately, any change performed in `/proc/acpi/wakeup` is reset at booting, and it depends of the BIOS, thus cannot be change permanently. Thus, one approach to avoid wake-up by this device, is to disable it every time the systems goes to suspension, and this can be done with a hook. This hook can be done in two ways:

1. Placing an executable in `/usr/lib/systemd/system-sleep`, all executables in this path will be run before suspending or hibernating the system.
2. Creating a `systemd` unit in `/etc/systemd/system` and hook it to the sleep unit.

The second method is preferred as `/etc/systemd/system` overrides any other units, and the path `/usr/lib/systemd/system` should be used only for units generated by the distribution package manager. More info in [**Here**](http://man7.org/linux/man-pages/man5/systemd.unit.5.html) and [**Here**](https://unix.stackexchange.com/questions/206315/whats-the-difference-between-usr-lib-systemd-system-and-etc-systemd-system).

These are the instructions for the 2nd way:

1. Identify the culprit device in `/proc/acpi/wakeup`

2. That device will be disabled from the wake-up list each time the computers goes to suspension

3. Create a file `suspend-usb-fix.service` in `/etc/systemd/system` with this content:

		:::bash
		[Unit]
		Description=Disables wake-up from device XHC
		# the service runs before the computer goes to sleep
		Before=sleep.target     

		[Service]
		Type=simple
		# check XHC is enabled, if so, toggle it to disabled
		ExecStart=/usr/bin/bash -c "if [[ $(cat /proc/acpi/wakeup|grep XHC | awk '{print substr($3,2); }') == enabled ]]; then echo XHC|tee /proc/acpi/wakeup; fi"

		[Install]
		# this does the hook to sleep.target
		WantedBy=sleep.target   


    Some important points:  

    * services run `root` unless a `User` is indicated in the `[Service]` section

    * services files are not shells, thus the syntax `ExecStart`


4. Change the permissions of the service file

		:::bash
		# chmod 664 /etc/systemd/system/suspend-usb-fix.service

5. Enable the service:

		:::bash
		systemctl enable suspend-usb-fix.service

6. If there any update in the service file, run ```$ systemctl daemon-reload``` after modifying it

7. Lastly, the status and last calls of the service are obtained with `$ systemctl status suspend-usb-fix.service`. And this information can be also found with `$ journalctl`
