---
Keywords: シェルスクリプト,UNIX/Linuxサーバ,小ネタ
Copyright: (C) 2017 Ryuichi Ueda
---

# sshで接続失敗したら別のssh接続を試すシェルスクリプト
小ネタも小ネタですが・・・。

うちはdynamic DNSでもらったドメイン名でssh接続できるようにしたサーバがあるんですが、
家の中からそのドメイン名で接続しようとするとできません。
ルータとか設定ファイルとかをいじればなんとかなるのかもしれませんが、
面倒なのでこういうシェルスクリプトを書いてしのいでます。

```bash
uedamac:SSH ueda$ cat UBUNTU_HOME 
ssh ueda.aho.example.com -p 12345 ||
ssh 192.168.0.101 -p 12345
```

これで、最初のssh接続が失敗したら次のssh接続が試行されます。
||と&&は便利ですね。


以上、何の捻りもありません。おしまい。
