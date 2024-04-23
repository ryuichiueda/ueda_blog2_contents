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
  src/Particle.cpp
  src/OdomModel.cpp
  src/Pose.cpp
  src/Scan.cpp
  src/LikelihoodFieldMap.cpp
  src/emcl2_node.cpp
)

if(BUILD_TESTING)                          #あとはたぶんデフォルト
  find_package(ament_lint_auto REQUIRED)
  set(ament_cmake_copyright_FOUND TRUE)
  set(ament_cmake_cpplint_FOUND TRUE)
  ament_lint_auto_find_test_dependencies()
endif()

install(PROGRAMS
  test/test.bash
  test/test_gui.bash
  DESTINATION lib/${PROJECT_NAME}
)

ament_auto_package(
  INSTALL_TO_SHARE
  config
  launch
  test
)
```

