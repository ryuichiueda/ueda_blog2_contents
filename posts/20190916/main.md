---
Keywords: opy
Copyright: (C) 2019 Ryuichi Ueda
---

# opyにjoin, dropjoinを実装

　シェル芸botで地味に活躍中の[opy](https://snapcraft.io/opy)に、特定の列（フィールド）を出力/削って出力する機能を実装しました。こんな感じです。（v1.8.0）

## 入力

　https://b.ueda.tech/?page=05649 にある「NASAのApacheログ」を例題にします。

```
$ head -n 3 access_log.nasa | iconv -c    # utf-8でないバイナリが混ざっているのでiconv -cしておきます
199.72.81.55 - - [01/Jul/1995:00:00:01 -0400] "GET /history/apollo/ HTTP/1.0" 200 6245
unicomp6.unicomp.net - - [01/Jul/1995:00:00:06 -0400] "GET /shuttle/countdown/ HTTP/1.0" 200 3985
199.120.110.21 - - [01/Jul/1995:00:00:09 -0400] "GET /shuttle/missions/sts-73/mission-sts-73.html HTTP/1.0" 200 4085
```

## 出力

### 例1: 1, 4, 5列目と最後から2列を出力

```
$ head -n 3 access_log.nasa | iconv -c | opy '[join(F,[1,4,5,NF-1,NF])]'
199.72.81.55 [01/Jul/1995:00:00:01 -0400] 200 6245
unicomp6.unicomp.net [01/Jul/1995:00:00:06 -0400] 200 3985
199.120.110.21 [01/Jul/1995:00:00:09 -0400] 200 4085
### これでもいいけど若干面倒 ###
$ head -n 3 access_log.nasa | iconv -c | opy '[F1, F4, F5, F[NF-1], F[NF]]'
（出力省略）
```

### 例2: 2列目を消す

`dropjoin(F,2)`で2列目を落として連結した文字列が返ってくるので、これをリストに包むと2列目が落とされて出力されます。

```
$ head -n 3 access_log.nasa | iconv -c | opy '[dropjoin(F,2)]'
199.72.81.55 - [01/Jul/1995:00:00:01 -0400] "GET /history/apollo/ HTTP/1.0" 200 6245
unicomp6.unicomp.net - [01/Jul/1995:00:00:06 -0400] "GET /shuttle/countdown/ HTTP/1.0" 200 3985
199.120.110.21 - [01/Jul/1995:00:00:09 -0400] "GET /shuttle/missions/sts-73/mission-sts-73.html HTTP/1.0" 200 4085
```

ちなみにAWKでやるとこうなります。スペースがひとつ余計につくので場合によっては`sed`が必要になります。（ただし、こちらの方がopyより処理は速いです。）

```
$ head -n 3 access_log.nasa | iconv -c | awk '{$2="";print}' | sed 's/  / /'
（出力省略）
```

### 例3: 2,3列目を消す

```
$ head -n 3 access_log.nasa | iconv -c | opy '[dropjoin(F,[2,3])]'
199.72.81.55 [01/Jul/1995:00:00:01 -0400] "GET /history/apollo/ HTTP/1.0" 200 6245
unicomp6.unicomp.net [01/Jul/1995:00:00:06 -0400] "GET /shuttle/countdown/ HTTP/1.0" 200 3985
199.120.110.21 [01/Jul/1995:00:00:09 -0400] "GET /shuttle/missions/sts-73/mission-sts-73.html HTTP/1.0" 200 4085
```

地味ですが、特に`dropjoin`の方が、たまにAWKで面倒になるのであると地味に便利です。
