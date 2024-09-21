---
Copyright: (C) Ryuichi Ueda
---

# ロボットの確率・統計問題集（問題）

## 1章

### 20240527_1

　順位が常に入れ替わっていても筆者が1位になった瞬間だけSNSにアップしているとずっと1位になっているように見えるので，それを勘違いしないように受け取らないといけません．

[（戻る）](/?page=robot_and_stats_questions#20240527_1)

### 20240921_1

　シェルを使う例を挙げておきます．答えは`209.7`です．

```bash
$ curl https://raw.githubusercontent.com/ryuichiueda/LNPR_BOOK_CODES/refs/heads/master/sensor_data/sensor_data_200.txt > a
$ cat a | awk '{a+=$4}END{print a/NR}'
209.737
### 別解（コマンドは各自インストールを）###
$ cat a | tr ' ' '\t' | datamash mean 4
209.7371329762
```

[（戻る）](/?page=robot_and_stats_questions#20240921_1)
