---
Keywords: eachline,GlueLang,while,寝る,日記,グルー言語を作る
Copyright: (C) 2017 Ryuichi Ueda
---

# 日記（実験データ解析にGlueLang投入から慌ててwhileを実装）
昨日から実験データの解析をしており、締め切りが遠いことから<a href="https://github.com/ryuichiueda/GlueLang" target="_blank">GlueLang</a>を投入してみました。これが記念すべき最初のコードです。書きなぐりなので意味を追って読まないでください。

<!--more-->

```hs
#!/usr/local/bin/glue
import PATH

file size = '{
 vec_length = $1*$2*$3*$4;
 rep_vec_num = $5;
 table_size = 18*36*144*324/vec_length;
 bit_for_action = 2;
 bit_for_vector_choice = int(log(1.0*rep_vec_num)/log(2.0)+0.5);

 print bit_for_vector_choice*table_size + rep_vec_num * vec_length * bit_for_action,$0;
}'

find './results/'
>>= grep 'comp_'
>>= xargs 'grep' -H ''
>>= tr ':_' ' '
>>= self '2/6' 'NF' 8
>>= awk '$6~/suc|bro|tim/'
#18 1 144 1 32 success 24.88
>>= grep -v 'success 0$'
>>= awk '{if($6=="broken"){$7=100};print}'
>>= sm2 '+count' 1 5 7 7
#18 1 144 1 32 100 24.88
>>= sort
>>= sm2 1 5 6 7
>>= awk -f size
#274752 18 36 1 1 32 14167 193095.34
>>= awk '{avg = $8/$7;print $1,$2,$3,$4,$5,$6,avg}'
>>= sort '-k1,1n'
```

全部パイプなのでbashとたいして変わらんと言えば変わらんのですが、<span style="color:red;font-size:36px">自分の作った言語で実験のコード書くの楽しい</span>という自己満足に浸ることができました。

いや、行頭にパイプの記号を書く（bashでも確かできるけど「|」が目立たないのであまりやりたくない）ことができるということや、awkのコードを書く部分がちょっとbashより楽だったので、ちょっとはコードを早く書ける効能がありました。GlueLang作るのに相当時間を潰してますが・・・。

<h1>やっとwhileみたいなものを作る気になった。作った。</h1>

実はこれを書く前に細かいファイルを１つずつさばくコードを書こうとしましたが、どうしてもまだ実装していないwhileが必要になり、断念してbashを使ってしまいました。ということで、急遽今夜、1時間くらいでwhileみたいなものを実装しました。名前はeachlineで、前段のパイプから受けとった文字列を引数にしてコマンドに次々と渡します。まあ、xargsのようなものです。ていうかxargsです。ただ、コマンドの代わりに手続き（proc）に書いたコードを渡すことができるので、これでforとwhileの機能の大半は実現していることになります。

例を一個のっけておきます。（<span style="color:red">まだちょっと引数の受け渡しにバグがあるようで、このコードをちょっと変えたら変なファイル名のファイルができました。ファイルを作るときは安全なディレクトリで試してみてください。</span>）

```hs
uedambp:~ ueda$ cat hoge.glue 
#!/usr/local/bin/glue
import PATH

proc hoge =
	# eachlineで受け取った引数の1番目をhogeとともにひっくり返す
	file f = echo 'hoge' argv[1] >>= rev
	# 二番目の引数をファイル名にして中間ファイルfをカレントディレクトリにmv
	mv f argv[2]
	

seq 1 10
>>= xargs -n 2

# 1 2 \\n 3 4 \\n ...
>>= eachline this.hoge
```

動かしてみます。

```hs
###シバンにある通り/usr/local/bin/glueにインストールしたglueを使うのでスクリプトをそのまま実行###
uedambp:~ ueda$ ./hoge.glue 
###ファイルができる###
uedambp:~ ueda$ ls [0-9]*
10 2 4 6 8
###ファイルの中身###
uedambp:~ ueda$ cat 10
9 egoh
uedambp:~ ueda$ cat 2
1 egoh
```

もうかなりC++のコードが構造化されていたので実装は30分くらいで済みましたが、引数を渡すときにメモリの確保を忘れてバグを作ってしまい、そいつを取るのに30分かかってしまいました。メモリリーク怖いっす。


明日も仕事なので、寝る。
