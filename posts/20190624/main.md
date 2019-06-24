---
Keywords: 日記
Copyright: (C) 2019 Ryuichi Ueda
---

# 日記（2019年6月24日） 

## ラズパイいじり

　某外部講師の先で講義に使うラズパイをセットアップ（Raspberry Pi 3B+にUbuntu 18.04をインストールして使うソフトをセットアップ）していたがWiFiの設定で撃沈。自分のNetplanの設定がおかしいかWiFiのデバイスドライバがぶっ壊れていたかどっちかで18時になってしまい時間切れ。その後19時前に研究室に戻って慣れた環境でおさらい。研究室ではうまく設定できた。Netplanというのは今までのネットワーク設定の代わりに使うもので、Ubuntu 18.04からデフォルト。まだ解説ができないので、代わりに自分の書いた設定ファイルを晒す。パスフレーズ等はunkoに変更済み。

```
ubuntu@ubuntu:~$ cat /etc/netplan/50-cloud-init.yaml
# This file is generated from information provided by
# the datasource.  Changes to it will not persist across an instance.
# To disable cloud-init's network configuration capabilities, write a file
# /etc/cloud/cloud.cfg.d/99-disable-network-config.cfg with the following:
# network: {config: disabled}
network:
    version: 2
    ethernets:
        eth0:
            dhcp4: no
            addresses: [192.168.2.123/24]
            gateway4: 192.168.2.1
            nameservers:
                addresses: [8.8.8.8,8.8.4.4]
            optional: true
    wifis:
        wlan0:
            addresses: [192.168.2.124/24]
            gateway4: 192.168.2.1
            dhcp4: no
            optional: true
            nameservers:
                addresses: [8.8.8.8,8.8.4.4]
            access-points:
                "unko_x":
                    password: unkosuperunko
```

