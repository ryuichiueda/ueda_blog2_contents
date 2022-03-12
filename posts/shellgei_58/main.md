---
Keywords: プログラミング,勉強会,シェル芸,シェル芸勉強会
Copyright: (C) 2022 Ryuichi Ueda
---

# 【問題と解答】jus共催 第58回シェル芸勉強会

* 問題で使われているデータファイルは[GitHub](https://github.com/ryuichiueda/ShellGeiData/tree/master/vol.58)にあります。クローンは以下のようにお願いします。

```bash
$ git clone https://github.com/ryuichiueda/ShellGeiData.git
```

* 環境: 解答例はUbuntu 20.04 LTSで作成。Macの場合はcoreutilsをインストールすると、GNUのコマンドが使えます。BSD系の人は玄人なので各自対応のこと。


## Q1

次のファイル`memo`について、

```
メモ: 2022年3月5日

* 2日後: ワクチン接種
* 6日後: 国際ロボット展
* 7日後: シェル芸勉強会
```

次のような出力を得てください。1行目の日付が違っても機能するワンライナーを考えてください。

```
* 2022年3月7日 ワクチン接種
* 2022年3月11日 国際ロボット展
* 2022年3月12日 シェル芸勉強会
```

### 解答例

```
$ cat memo | awk 'NR==1{d=$2}NR>1{gsub(/日後:/," "d,$2);print}' |
awk 'NF{print "echo","$(date -d \""$3,$2"days\")",$4}' | sed 'y/年月日/-- /'  |
bash | awk '{print "*",$1$2$3,$7}'
* 2022年3月7日 ワクチン接種
* 2022年3月11日 国際ロボット展
* 2022年3月12日 シェル芸勉強会
```

## Q2

数字を直接打ち込むことなく、`date`に`2022年02月22日 2 22:22:22`と出力させてください。二列目の`2`は週番号です。

### 解答例

```
$ a=$(($$/$$<<$$/$$));b=$(($$-$$));echo $a$b$a$a$b$a$a$a $a$a:$a$a:$a$a | date -f- "+%x %w %T"
2022年02月22日 2 22:22:22
```

## Q3

https://file.ueda.tech/eki/p/13.json のJSON形式のデータを、次のようなYAML形式に変換してください。

```
line:
  - line_cd: "11301"
    line_name: JR東海道本線(東京～熱海)
  - line_cd: "11302"
・・・
```

### 解答例

```
$ cat 13.json | yq -o xml | yq -p xml -o yaml
```

## Q4

次のような出力を得てください。

![](unko_move.mp4)


### 解答例

```
yes 💩💩💩💩💩💩💩 | awk '{print 7-(NR-1)%7,int((NR-1)/7),$0}' |
awk '{print $2,substr($3,1,$1),substr($3,$1+1)}' |
awk '{for(i=1;i<=$1;i++)printf " ";printf("%s %s",$2,$3);system("sleep 0.1;printf \\\\r")}'
```


## Q5

次のファイル`putin`から、プーチンと読めるものの行番号を表示してください。一般解は不要ですが、行番号は直接指定しないでください。


```
プ-ﾁﾝ
ﾌﾟ‐チン
プーチン
ﾌﾟ‑ﾁﾝ
ﾌ‑ﾃﾝ
フﾟ−チｿ
タ−ﾁｬﾝ
プチン
フﾟ−チン
プ–ﾁン
プｰチン
プﾁｬｰﾁﾝ
プ―チン
ﾎﾟ―チン
プｰｻﾝ
ﾌﾟｯﾁﾝ
ﾌﾟﾁ-ﾝ
プ—チン
```

### 解答例

いきあたりばったりですが、一度半角になおして全角に戻すと見通しがよくなります。

```
$ nl putin | nkf | nkf -Z4 | nkf | grep プ | grep チン | grep -v ッ | grep -v プチ
     1	プ-チン
     2	プ‐チン
     3	プーチン
     4	プ‑チン
     9	プ-チン
    10	プ–チン
    11	プーチン
    13	プ-チン
    18	プ-チン
```


## Q6 

次のふたつのファイルについて、

```
$ cat file1
バンコ
クラルンプール
ャカルタ
プノンン
$ cat file2
プンペン
アラルンプール
ンコク
ジャカタ
```

次の出力を得てください。行の順番は任意とします。また、完璧でなくてもよいのでなるべく一般的な解を作ってください。

```
バンコ ンコク
クラルンプール アラルンプール
ャカルタ ジャカタ
プノンン プンペン
```

### 解答例

```
$ join -j9 file* |
awk -F "" '{for(i=1;i<NF;i++)a[$i$(i+1)]++;for(k in a)if(a[k]>1){b++};print $0,b;delete(a);b=0}' |
awk '$3>0{print $1,$2}'
バンコ ンコク
クラルンプール アラルンプール
ャカルタ ジャカタ
プノンン プンペン
```

## Q7

`nums.gz`（`https://github.com/ryuichiueda/ShellGeiData/raw/master/vol.58/nums.gz`）内の数字を全て足してください。


### 解答例

```
$ (zgrep -v '^[0-9]*$' nums.gz | zen_to_i ; zgrep '^[0-9]*$' nums.gz ) | awk '{a+=$1}END{print a}'
50000224232066
### AWKで桁落ちするとき ###
$ (zgrep -v '^[0-9]*$' nums.gz | zen_to_i ; zgrep '^[0-9]*$' nums.gz ) | paste -d+ - - - - - - - - - - | bc | paste -d+ - - - - - - - - - - | bc | paste -d+ - - - - - - - - - - | bc | paste -d+ - - - - - - - - - - |bc | paste -d+ - - - - - - - - - - |bc| paste -d+ - - - - - - - - - - |bc| paste -d+ - - - - - - - - - - |bc| paste -d+ - - - - - - - - - - |bc
50000224232066
### dcを使う例（少し遅いです。）
$ (zgrep -v '^[0-9]*$' nums.gz | zen_to_i ; zgrep '^[0-9]*$' nums.gz ) | sed '2,$s/$/+/' | sed '$s/$/\np/' | dc
50000224232066
```

* zen_to_i: https://github.com/yoshitsugu/zen_to_i


