---
Keywords: Rasberry Pi Mouse,Raspberry Pi
Copyright: (C) 2018 Ryuichi Ueda
---

# making Raspberry Pi Mouse 3 B+ with Ubuntu 16.04 work on Raspberry Pi Mouse

It (including Wi-Fi) works with the following procedure.

## 1. preparing microSD

* download the following image
    * ubuntu-16.04.4-preinstalled-server-armhf+raspi2+upgraded+ros-preinstalled+kernel-compiled-20180805.img.xz (MD5: 7a83369cd9d981906b3ed8312457dadd)  linked on https://www.asrobot.me/entry/2018/07/11/001603
* write it to a 16GB microSD card
* enlarge the main partition (partition 2) 
    * [My book](https://amzn.to/2MVqrHA) may help you if you have no idea. 

## 2. preparing the device driver

```
cd
git clone https://github.com/rt-net/RaspberryPiMouse 
cd RaspberryPiMouse/utils
./build_install.raspbian.bash  ###(not build_install.ubuntu14.bash)###
cd 
git clone https://github.com/ryuichiueda/pimouse_setup
cd pimouse_setup
sudo make install
```



## 3. installing ROS

Let's install as in the past. 

