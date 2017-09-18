---
Keywords:シェルスクリプト,UNIX/Linuxサーバ,小ネタ
Copyright: (C) 2017 Ryuichi Ueda
---

# sshで接続失敗したら別のssh接続を試すシェルスクリプト
小ネタも小ネタですが・・・。<br />
<br />
うちはdynamic DNSでもらったドメイン名でssh接続できるようにしたサーバがあるんですが、<br />
家の中からそのドメイン名で接続しようとするとできません。<br />
ルータとか設定ファイルとかをいじればなんとかなるのかもしれませんが、<br />
面倒なのでこういうシェルスクリプトを書いてしのいでます。<br />
<br />
[bash]<br />
uedamac:SSH ueda$ cat UBUNTU_HOME <br />
ssh ueda.aho.example.com -p 12345 ||<br />
ssh 192.168.0.101 -p 12345<br />
[/bash]<br />
<br />
これで、最初のssh接続が失敗したら次のssh接続が試行されます。<br />
||と&&は便利ですね。<br />
<br />
<br />
以上、何の捻りもありません。おしまい。
