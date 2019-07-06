---
Keywords: 日記,ROS
Copyright: (C) 2019 Ryuichi Ueda
---

# 日記（2019年7月6日）

## Cartographerいじり

　Cartographerをロボットで実行して、終わりに`map_saver`を実行し、軌跡をtsvファイルに保存するまでを、一つのローンチファイルを立ち上げたあと、PCを途中で触らないで実行できるようにした。SLAMが終わった後に`map_saver`を呼び出すというのがlaunchファイルでは表現できず、C++の中で`system`を使ってコマンドをそのまま与えた。ちゃんと動いた。

