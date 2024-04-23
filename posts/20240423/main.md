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




