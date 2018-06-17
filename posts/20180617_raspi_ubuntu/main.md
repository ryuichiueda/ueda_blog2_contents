---
Keywords: Raspberry Pi, Ubuntu, Raspberry Pi Mouse
Copyright: (C) 2018 Ryuichi Ueda
---

# Ubuntu 16.04 and 18.04 images for Raspberry Pi 3 and Raspberry Pi Mouse

I modified the unofficial images in https://wiki.ubuntu.com/ARM/RaspberryPi for ["Learning ROS robot programming with Raspberry Pi."](https://www.rt-shop.jp/index.php?main_page=product_info&cPath=1317&products_id=3655) 


## list of the modified images.

Please use a 16GB microSD (microSDXC) card though the image size is 8GB. You can 

| | image |  software  |
|-|----|----|
|1| [ubuntu-16.04-preinstalled-server-armhf+raspi3-8G-20180616.img.xz](http://file.ueda.tech/RPIM_BOOK/ubuntu-16.04-preinstalled-server-armhf+raspi3-8G-20180616.img.xz)   |  Ubuntu 16.04 for Raspberry Pi 3  |
|2|  [ubuntu-16.04-preinstalled-server-armhf+raspi3-ROS-20180616.img.xz](http://file.ueda.tech/RPIM_BOOK/ubuntu-16.04-preinstalled-server-armhf+raspi3-ROS-20180616.img.xz)  |  Ubuntu 16.04 + ROS for Raspberry Pi 3  |
|3| [ubuntu-16.04-raspimouse-20180616.img.xz](http://file.ueda.tech/RPIM_BOOK/ubuntu-16.04-raspimouse-20180616.img.xz) |  Ubuntu 16.04 + ROS + Raspberry Pi Mouse device driver for Raspberry Pi 3  |
|4|  [ubuntu-18.04-preinstalled-server-armhf+raspi3-20180616.img.xz](http://file.ueda.tech/RPIM_BOOK/ubuntu-18.04-preinstalled-server-armhf+raspi3-20180616.img.xz)  |  Ubuntu 18.04 for Raspberry Pi 3  |
|5|  [ubuntu-18.04-preinstalled-server-armhf+raspi3-ROS-20180616.img.xz](http://file.ueda.tech/RPIM_BOOK/ubuntu-18.04-preinstalled-server-armhf+raspi3-ROS-20180616.img.xz)  |  Ubuntu 18.04 + ROS for Raspberry Pi 3  |
|6|  [ubuntu-18.04-raspimouse-20180616.img.xz](http://file.ueda.tech/RPIM_BOOK/ubuntu-18.04-raspimouse-20180616.img.xz)  |  Ubuntu 18.04 + ROS + Raspberry Pi Mouse device driver for Raspberry Pi 3  |

## summary of the modification

* resizing the main partition (2GB -> 8GB): 1,2,3
* updating the WiFi firmware: 1-6
* installing ROS: 2,3,5,6
* installing the device driver for Raspberry Pi Mouse: 3,6
