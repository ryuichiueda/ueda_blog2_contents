---
Keywords: ROS 2
Copyright: (C) 2024 Ryuichi Ueda
---

# C++で作ったROS 1のパッケージをROS 2に移植するときのつまづきポイント ―その2

　https://github.com/ryuichiueda/value_iteration
を
https://github.com/ryuichiueda/value_iteration2
に移植中です。[前回](/?post=20240423)に引き続き、困った点についてメモします。今回はlaunchファイルです。たぶんこういうのはアドホックにやらずにちゃんとマニュアル読んだほうがいいんですが、そういうタイプの人間じゃないのでごめんなしゃい。

## launchファイルの書き方

　launchファイルもちょっと面倒です。
XMLでもyamlでもいいということになっていますが、
基本はPythonでノードの実行方法や手順を書いていくことになります。
（それは講義でPythonのパッケージを作っていたので知ってた。）

　とりあえずひとつのノードをparams.yamlファイルに書いた
パラメータを読み込んで立ち上げるlaunchファイルのコードを置いておきます。
あとから書きますが、書いただけでは使えません。
いろいろ探しましたが、[こちら](https://roboticsbackend.com/ros2-yaml-params/)が参考になりました。

```python

import launch, os
from ament_index_python.packages import get_package_share_directory
from launch_ros.actions import Node


def generate_launch_description():
    config = os.path.join(
      get_package_share_directory('value_iteration2'),
      'config',
      'params.yaml'
    )

    vi_node = Node(
            package='value_iteration2',
            namespace='value_iteration2', #namespaceはたぶんC++のコードで使ってないといけない
            executable='vi_node',
            name='vi_node',
            parameters=[config], #上で作ったconfigオブジェクトをリストに入れて指定
        )

    return launch.LaunchDescription([vi_node])
```

　あと、`yaml`ファイルでノードの名前の指定を細かくチェックされるので、前回の書き方ではダメなようです。とりあえず次のように「ノードの名前なんでもいいよ」というガバガバ設定にしておきます。

```yaml
### config/params.yaml ###
/**:       #ここをとりあえず/**（ガバ設定）にしておく
  ros__parameters:
    global_thread_num: 2
    local_thread_num: 1
    online: true
・・・
```

## launchファイルの使い方

　で、使い方なんですが、launchファイルもパラメータのyamlファイルも、CMakeLists.txtに設定を書いて、installディレクトリにうつさないといけないっぽいです。

```cmake
# CMakeLists.txt内
install(TARGETS vi_node DESTINATION lib/${PROJECT_NAME})   #vi_nodeはlibへ
install(DIRECTORY launch DESTINATION share/${PROJECT_NAME}) #launchファイルはshareへ
install(DIRECTORY config DESTINATION share/${PROJECT_NAME}) #config内のyamlファイルもshareへ
```

↑のように`CMakeLists.txt`に書いて`colcon build`すると、次のようにファイルがワークスペース下の`install`ディレクトリ内に移動します。

```bash
$ find ~/ros_ws/install/ | grep share | grep -e yaml\$ -e launch\$
/home/ueda/ros_ws/install/value_iteration2/share/value_iteration2/launch
/home/ueda/ros_ws/install/value_iteration2/share/value_iteration2/config/params.yaml
```

　これで次のように`ros2 launch`すると、ノードが立ち上がってパラメータが読み込まれます。

```bash
$ ros2 launch value_iteration2 turtle.launch.py
[INFO] [launch]: All log files can be found below /home/ueda/.ros/log/2024-04-26-09-59-41-519021-uedaP1g6-95608
[INFO] [launch]: Default logging verbosity is set to INFO
[INFO] [vi_node-1]: process started with pid [95609]
[vi_node-1] [INFO] [1714093181.556916371] [value_iteration2.vi_node]: Global thread num: 2 #params.yamlに書いた値が入っている
[vi_node-1] [INFO] [1714093181.556967865] [value_iteration2.vi_node]: Online: true   #同上
[vi_node-1] [INFO] [1714093181.557845827] [value_iteration2.vi_node]: Hell world!
[vi_node-1] [INFO] [1714093181.658053916] [value_iteration2.vi_node]: Hell world!
```

現場からは以上です。
