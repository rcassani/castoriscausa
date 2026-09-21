#!/bin/bash
# Return error if error in any step
set -euo pipefail

# Just run as sudo
[[ $EUID -eq 0 ]] || { echo "Run with sudo" >&2; exit 1; }

# Installation of Realtek driver
apt install --yes bzip2 build-essential
cd /tmp
wget "www.castoriscausa.com/files/r8125-9.018.00.tar.bz2"
tar -xjf r8125-9.018.00.tar.bz2
cd r8125-9.018.00
chmod +x autorun.sh
./autorun.sh

# Correct the installation by Realtek drivers
cd /lib/modules/$(uname -r)/kernel/drivers/net/ethernet/realtek/
mv r8169.zst.bak r8169.ko.zst 
echo "blacklist r8169" | sudo tee /etc/modprobe.d/blacklist-r8169.conf 
depmod -a
update-initramfs -u

# Get DHCP IP address
ip link set eno1 up
dhcpcd eno1
ip address
