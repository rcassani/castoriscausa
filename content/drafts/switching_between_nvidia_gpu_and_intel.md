

Switching from NVIDIA GPU to intel worked perfectly:

sudo prime-select intel
then logout login

However the oppositve switch from Intel to NVIDIA caused my kernel to freeze
sudo prime-select nvidia\
works fine
then at loging out it freezes, same goes if restart, shutdown are intented

Use prime-select, simpler and out of the box compared with Bumblebee

Need to add `acpi_osi=! acpi_osi="Windows 2009"` to the kernel configuration

https://bugs.launchpad.net/lpbugreporter/+bug/752542/comments/793

https://github.com/Bumblebee-Project/Bumblebee/issues/764#issuecomment-234494238

now that everything is working you can install something as https://github.com/andrebrait/prime-indicator
to be able to change the GPU directly from the tray
