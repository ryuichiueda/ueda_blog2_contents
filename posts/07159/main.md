---
Keywords: Linux,Raspberry,WiringPi
Copyright: (C) 2017 Ryuichi Ueda
---

# 考えたくない人向けWiringPi2導入手順（Raspberry Pi2 Model B, 2015年11月6日現在）
少しずつ情報が古くて一発で行かなかったので。gpioコマンドを使いたくても、Pythonもろともインストールしてしまった方が手っ取り早いようです。

しかしこの情報も、そのうち古くなるのでしょう・・・

2015年11月6日現在です。

```bash
$ sudo apt-get install python-dev python-setuptools
$ git clone https://github.com/Gadgetoid/WiringPi2-Python.git
$ cd WiringPi2-Python/
$ sudo python setup.py install
$ cd WiringPi/
$ ./build 
```

<a href="https://github.com/ryuichiueda/NikkeiRaspiMouse/blob/master/util/install_wiring_pi2_python.bash">GitHubにもおきました。</a>

一応、連載の関係もあるので、しばらくは不具合の対応をいたします。

