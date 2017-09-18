---
Keywords:Python,ROS
Copyright: (C) 2017 Ryuichi Ueda
---

# 【やっつけ】CGIHTTPServer.test()でウェブサーバを立ち上げるROSのノードを作る
もっと簡単な方法があれば教えてくださーい<br />
<br />
<h2>やりたいこと</h2><br />
roslaunchでウェブサーバを立ち上げたい。roslaunchを終わらせたらウェブサーバを落としたい。<br />
<br />
<h2>やり方</h2><br />
<br />
次のようなスクリプトwebserver.pyを書いて、scriptsディレクトリに置く。<br />
<br />
[python]<br />
#!/usr/bin/env python<br />
import rospy, os<br />
import CGIHTTPServer<br />
<br />
def kill():<br />
 os.system(&quot;kill -KILL &quot; + str(os.getpid()))<br />
<br />
os.chdir(os.path.dirname(__file__))<br />
rospy.init_node(&quot;webserver&quot;)<br />
rospy.on_shutdown(kill)<br />
CGIHTTPServer.test()<br />
[/python]<br />
<br />
<br />
launchファイルにノードを次のように書く。<br />
<br />
[html]<br />
&lt;launch&gt;<br />
 &lt;node pkg=&quot;hoge_webserver&quot; name=&quot;webserver&quot; type=&quot;webserver.py&quot; required=&quot;true&quot; args=&quot;8080&quot; /&gt;<br />
&lt;/launch&gt;<br />
[/html]<br />
<br />
<br />
<h2>解説</h2><br />
<br />
スクリプト中のkillは、自分自身のプロセスをぶっ殺す関数で、CGIHTTPServer.test()もろともシステムから消し去ります。これがないと、CGIHTTPServer.test()のスレッド（？）が死にません。<br />
<br />
また、roslaunchからこのノードを立ち上げると、システムのディレクトリがドキュメントルートになるので、8行目でディレクトリをscriptsに変更しています。<br />
<br />
また、roslaunchからwebserver.pyを立ち上げると引数に余計なものが入るので、ローンチファイルでwebserver.pyに指定する引数をargs="8080"と明示的に指定しています。<br />
<br />
<br />
<br />
以上。
