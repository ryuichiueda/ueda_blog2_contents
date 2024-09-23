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


### 20240924_1

　こちらもシェルを使う例を挙げておきます．平均値は[20240921_1](#20240921_1)のものを使用。1列目が分散、2列目が標準偏差です。

```bash
$ cat a | awk '{a+=($4-209.7371329762)**2}END{print a/(NR-1), sqrt(a/(NR-1))}'
23.4081 4.83819
### 別解 ###
$ cat a | tr ' ' '\t' | datamash svar 4 sstdev 4
23.408106598555	4.8381924929207
```
