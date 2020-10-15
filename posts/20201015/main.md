---
Keywords: 日記
Copyright: (C) 2020 Ryuichi Ueda
---

# 日記（2020年10月15日）

締切地獄で全然日記書けんです。

## UbuntuでのVirtualBoxの設定（むずい）

　UEFIのセキュアーブートをenabledにしたままVirtualBoxを
インストールすると、仮想マシンが立ち上がらない問題に
出くわしてがちゃがちゃやったら動きました。

　まず、このサイトにしたがって、シェルスクリプトを
動かすところで頓挫しました。

* https://stackoverflow.com/questions/61248315/sign-virtual-box-modules-vboxdrv-vboxnetflt-vboxnetadp-vboxpci-centos-8

　次にここを見て、シェルスクリプト内のパス
を` /usr/src/kernels/$(uname -r)/scripts/sign-file`
から`/usr/src/linux-headers-$(uname -r)/scripts/sign-file`
に変更しました。もしかしたら、この2番目のサイトだけで
設定できるかもしれません。

* https://stegard.net/2016/10/virtualbox-secure-boot-ubuntu-fail/


以上
