---
Keywords: ROS 2
Copyright: (C) 2024 Ryuichi Ueda
---

# C++で作ったROS 1のパッケージをROS 2に移植するときのつまづきポイント ―その1（2があるかどうかは不明）

　https://github.com/ryuichiueda/value_iteration
を
https://github.com/ryuichiueda/value_iteration2
に移植中です。[前回](/?post=20240419)に引き続き、困った点についてメモ。


## CMakeLists.txt どうやって書くの？

　上田研の有志一同がROS 2に移植したemcl2（https://github.com/CIT-Autonomous-Robot-Lab/emcl2_ros2 ）
の[CMakeLists.txt](https://github.com/CIT-Autonomous-Robot-Lab/emcl2_ros2/blob/main/CMakeLists.txt)
が参考になりました。無茶振りして知見だけもらって申し訳ないですありがとうございます。
転載してコメントいれさせてもらいます。これ見てたらメシ代請求してください。

```cmake

cmake_minimum_required(VERSION 3.8)
project(emcl2)

if(NOT CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 17)   #この前後3行はいらないかも
endif()

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-O3 -Wall -Wextra -Wpedantic)  #Clangかg++に渡すオプション
endif()

find_package(ament_cmake_auto REQUIRED) #ament_cmake_autoというパッケージを
                                        #使うとpackage.xmlに書いたパッケージを
ament_auto_find_build_dependencies()    #探してくれるっぽい

ament_auto_add_executable(emcl2_node
  src/Mcl.cpp                           #.cppファイルをここに並べる
  src/ExpResetMcl2.cpp
  （中略）
  src/emcl2_node.cpp
)

if(BUILD_TESTING)                          #あとはたぶんデフォルト
（以下略）
```

ヘッダファイルを探す命令も書いていませんが、
`include/<パッケージ名>/`に入れておけば探してくれる模様です。


## パブリッシャ、サブスクライバの型

　こんなふうに変わるみたいです。なげーよ。
ROS 2のほうの`Subsription`を`Subscriber`にして10分くらい死んでました。
Rustみたいにuse（using）を多用しないといけないのかもしれません。

```cpp

/* ROS 1 */
ros::Publisher pub_cmd_vel_;     //パブリッシャ
ros::Subscriber sub_laser_scan_; //サブスクライバ
/* ROS 2 */
rclcpp::Publisher<geometry_msgs::msg::Twist>::SharedPtr pub_cmd_vel_;         //パブリッシャ
rclcpp::Subscription<sensor_msgs::msg::LaserScan>::SharedPtr sub_laser_scan_; //サブスクライバ
```


## ConstSharedPtr

　`ConstPtr`がdeprecatedだと叱られました。
次のように`ConstSharedPtr`を使えとのことです。
・・・なげーよ。

```cpp

/* ROS 1 */
void scanReceived(const sensor_msgs::LaserScan::ConstPtr &msg);
/* ROS 2 */
void scanReceived(const sensor_msgs::msg::LaserScan::ConstSharedPtr msg);
```

事情は[ここらへん](https://design.ros2.org/articles/generated_interfaces_cpp.html)
にちょろっとだけ書いてあります。

### std_msgsのヘッダファイル

　`std_msgs/UInt32MultiArray.h`は`std_msgs/msg/uint32_multi_array.hpp`
になるんだろうなーと思ったけどビルドが通らず、
そこそこ時間を消耗しました。`u`のうしろにもアンダースコアがいりました。
死にました。[ここらへん](https://docs.ros.org/en/ros2_packages/rolling/api/io_context/generated/program_listing_file__tmp_ws_src_transport_drivers_io_context_include_msg_converters_std_msgs.hpp.html) が参考になります。
ていうかおじさんが学生のころはhppという拡張子を見たことがなったんですが、
いつごろみんな使い始めたんでしょう？

```cpp

/* ROS 1 */
#include "std_msgs/UInt32MultiArray.h"
#include "std_msgs/Float32MultiArray.h"
/* ROS 2 */
#include <std_msgs/msg/u_int32_multi_array.hpp>
#include <std_msgs/msg/float32_multi_array.hpp>
```
