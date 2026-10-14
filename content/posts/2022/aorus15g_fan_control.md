Title: Fan speed control for AORUS15G
Date: 2022-06-25 09:39
Tags: Bash, Linux, hack
Author: Raymundo Cassani
Slug: aorus15g-fan-control
Thumbnail: fan_modes_curves.png

More a side project than a need, I wanted to control in Linux the [**fan modes**](https://github.com/rcassani/p37-ec-aorus15g#fan-modes) (the relationship between temperature and fan speed) in my [2020 Gigabyte AORUS 15G KB](https://github.com/rcassani/p37-ec-aorus15g/blob/master), it should apply to similar models. The code for this project can be found in: [https://github.com/rcassani/p37-ec-aorus15g](https://github.com/rcassani/p37-ec-aorus15g).

Fortunately, I did not have to start the project from scratch as there was previous work done for other Gigabyte laptops: [P37Xv5 and P37Wv5](https://github.com/jertel/p37-ec), and [Aero14](https://github.com/christiansteinert/p37-ec-aero-14) and [Aero15](https://github.com/tangalbert919/p37-ec-aero-15).   

The first step was to install [RWEverything](http://rweverything.com/) to be able to monitor the changes in the embedded controller (EC) registers while changing the fan modes. There are **six** fan modes available in the [AOURUS Control Center](https://download.gigabyte.com/FileList/Manual/ControlCenter_QSG_Manual_v1.1.pdf). Three are hard coded: **Normal**, **Quiet** and **Gaming**, and the other three can be configured: **AutoMax**, **Fix** and **Deep control**. All these modes seem to be controlled by different combinations of five single bits (`0x08.6`,`0x06.4`,`0x0D.0`,`0x0D.7` and `0x0C.4`), following the behaviour in this table:

| Fan mode \ `Bits`:: |`0x08.6`--|`0x06.4`--|`0x0D.0`--|`0x0D.7`--|`0x0C.4`--|
| ---               |  ---   |  ---   |  ---   |  ---   |  ---   |
| **Normal**        |   0    |   0    |   0    |   0    |   0    |
| **Quiet**         |   1    |   X    |   X    |   X    |   X    |
| **Fix** \*        |   0    |   1    |   X    |   X    |   X    |
| **AutoMax** ^     |   0    |   0    |   1    |   X    |   X    |
| **Deep control**  |   0    |   0    |   0    |   1    |   X    |
| **Gaming**        |   0    |   0    |   0    |   0    |   1    |


\* For **Fix** mode, define the fan speed %s in registers `0xB0` and `0xB1`  
^ For **AutoMax** mode, define the maximum fan speed %s in registers `0xB0` and `0xB1`

<center>
[<img src="/images/fan_modes_curves.png" style="width: 90%;"/>](/images/fan_modes_curves.png)  
Fan modes: Normal, Gaming and Quiet
</center>

Lastly, the `set-fan-mode` bash script was wrote to facilitate setting the EC registers according with the desired fan mode:

```
$ set-fan-mode --help                                                   ✘ 1
Usage: set-fan-mode fan-mode [fan-speed]
  fan-mode  : <Fan mode to set>
  fan-speed : <Fan speed in % for "fix" and "automax" modes>

Fan modes: normal | quiet | gaming | deepcontrol | fix | automax
See: https://github.com/rcassani/p37-ec-aorus15g
```
