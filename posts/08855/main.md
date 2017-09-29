---
Keywords: Python,ROS
Copyright: (C) 2017 Ryuichi Ueda
---

# 【やっつけ】CGIHTTPServer.test()でウェブサーバを立ち上げるROSのノードを作る
もっと簡単な方法があれば教えてくださーい

<h2>やりたいこと</h2>
roslaunchでウェブサーバを立ち上げたい。roslaunchを終わらせたらウェブサーバを落としたい。

<h2>やり方</h2>

次のようなスクリプトwebserver.pyを書いて、scriptsディレクトリに置く。

```python
#!/usr/bin/env python
import rospy, os
import CGIHTTPServer

def kill():
 os.system(&quot;kill -KILL &quot; + str(os.getpid()))

os.chdir(os.path.dirname(__file__))
rospy.init_node(&quot;webserver&quot;)
rospy.on_shutdown(kill)
CGIHTTPServer.test()
```


launchファイルにノードを次のように書く。

```html
<launch&gt;
 <node pkg=&quot;hoge_webserver&quot; name=&quot;webserver&quot; type=&quot;webserver.py&quot; required=&quot;true&quot; args=&quot;8080&quot; /&gt;
</launch&gt;
```


<h2>解説</h2>

スクリプト中のkillは、自分自身のプロセスをぶっ殺す関数で、CGIHTTPServer.test()もろともシステムから消し去ります。これがないと、CGIHTTPServer.test()のスレッド（？）が死にません。

また、roslaunchからこのノードを立ち上げると、システムのディレクトリがドキュメントルートになるので、8行目でディレクトリをscriptsに変更しています。

また、roslaunchからwebserver.pyを立ち上げると引数に余計なものが入るので、ローンチファイルでwebserver.pyに指定する引数をargs="8080"と明示的に指定しています。



以上。
