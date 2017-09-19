---
Keywords: C++,C/C++,Linux,Raspberry
Copyright: (C) 2017 Ryuichi Ueda
---

# Raspberry Pi MouseをC++で動かすとどうなるか（けっこう楽だった）
誰か（たぶんNさん）に書けと言われたような気がするので・・・

日経Linuxで連載中の「<a href="http://itpro.nikkeibp.co.jp/atcl/mag/14/236750/063000018/" target="_blank">Raspberry Piで始めるかんたんロボット製作</a>」では、シェルスクリプトでロボットを動かしています。

<iframe src="https://rcm-fe.amazon-adsystem.com/e/cm?lt1=_blank&bc1=000000&IS2=1&bg1=FFFFFF&fc1=000000&lc1=0000FF&t=ryuichiueda-22&o=9&p=8&l=as4&m=amazon&f=ifr&ref=ss_til&asins=B00ZD9E15S" style="width:120px;height:240px;" scrolling="no" marginwidth="0" marginheight="0" frameborder="0"></iframe>

まだ連載はモータを動かしたりブザーを鳴らしたりと要素の動作確認の段階ですが、8月発売の号（9月号）からロボットが走ります。こんなふうに・・・地味に・・・

<iframe width="420" height="315" src="https://www.youtube.com/embed/-rArYTg6UNQ" frameborder="0" allowfullscreen></iframe>

シェルスクリプトで作るのは個人的な特性もありますが、ちゃんとした理由もあります。こんな感じです。
<ul>
	<li>行数が短くて説明しやすいこと</li>
	<li>プロセスを複数使うことが簡単なこと</li>
	<li>良かれ悪かれ誰でもUNIX系のOSをイジる場合、シェルスクリプトを使わなければならないので変にシャレオツな言語を使うよりは無駄にならないこと</li>
</ul>
といったところです。

また、ロボットは私が無理言ってデバイスファイルで動かすことにしたので、字を読み書きするにはリダイレクトだけで済むようにしました。これもシェルスクリプトだと簡単です。普通の言語だとファイル開いたり閉じたり面倒です。


<h2>と言いつつC++</h2>

連載はそんな感じでシェルスクリプトでやってますが、限界もあります。

Raspberry Pi Mouseをちょっと本職に使ってみようということで、今度の<a href="http://www.icra2016.org/" target="_blank">ICRAという学会</a>（ロボット屋にとって一番重要な学会）の実験をやってみました。選んだのはシェルスクリプトでなくC++です。シェルスクリプトを使わない理由で一番大きいのは
<ul>
	<li>ロボットの内部状態を表現できない</li>
</ul>
ことです。複雑なタスクをするロボットのプログラムを書くときは、ロボットが何を考えているかを変数で表現し、その値をコロコロ変えるという方法をとるのが一般的です。しかし、シェルスクリプトを使うとシェルの変数（機能が貧弱極まりない）に書くか、遅いファイル（Raspberry Piの場合はキャッシュがそんなに効かないしファイルはフラッシュメモリ上に書かないといけないので特に遅い）に書くかしないといけないのでちょっと苦しくなります。内部状態を保持してHTTPサーバのようにレスポンスしてくれるサーバのようなコマンドがあればシェルスクリプトから呼び出して使えて便利ですが、わざわざそんなもん作りたくありません。

こうなるとシェルスクリプトで書く旨味は全くないので、何か自分の知っている別の言語を使うことになります。内部状態を表現するということでオブジェクト指向言語を使うということになりますが、遅い言語だと実験がモッサリしたり、計算時間を論文に書く時にえらく損をするので、C++を選びました。

・・・と、いかにも熟慮したかのように書きましたが、ほぼノータイムでC++で、他はありません。こういうときにPython選んで「遅い遅い」言っている研究者が結構いるので、ちゃんと勉強しようよ思いつつ、人のことなので黙っております。

<h2>fstreamを使うとそんなに面倒でない</h2>

で、上で説明した「普通の言語を使うとファイルに書き込むのが面倒」ですが、C++にはfstreamという強力で素敵なサムシングがあります。例えば、以下は実験用のソース（まだまだ非公開。もちろん自分で書いた。）から、ステップモータにデバイスファイルを通じて周波数を指定するメソッドを抜粋したものです。

[c language="++"]
void Mouse::putMotorHz(int lvalue,int rvalue)
{
 ofstream r_motor(&quot;/dev/rtmotor_raw_r0&quot;);
 ofstream l_motor(&quot;/dev/rtmotor_raw_l0&quot;);
 r_motor &lt;&lt; rvalue;
 l_motor &lt;&lt; lvalue;
 r_motor.close();
 l_motor.close();
}
```

ファイル開けて値を書いて閉じるというのはやはりシェルでリダイレクトするより手間ですが、int型の数字をそのまま文字列に変換して「&lt;&lt;」でぶち込んでくれます。（上のメソッド、本当は値のチェックをしないといけないのですがね・・・）

今度は読み込みの例です。距離センサ（値をスペース区切りで4個出力）を読んでいます。これもデバイスファイル（/dev/rtlightsensor0）から読み出した値をintの配列sv（実は厳密にはvector&lt;int&gt;）に直接代入しています。
[c language="++"]
ifstream ifs(&quot;/dev/rtlightsensor0&quot;);
if(ifs.bad()){
 ifs.close();
 continue;
}

ifs &gt;&gt; sv[0] &gt;&gt; sv[1] &gt;&gt; sv[2] &gt;&gt; sv[3];
ifs.close();
```

比較実験はしませんが、FILE型を使うよりはかなり楽で、確か3,4倍くらいFILE型を使うより遅くて済むというくらいのトレードオフだったと記憶しています。また、ファイル処理以外はC言語と比べて最悪でも2倍くらいの減速で済みます。


あと、並列化が必要なら、<a href="http://blog.ueda.asia/?p=3640">新しいC++だとPOSIXスレッドがけっこう簡単に使える</a>ので、それも変に凝った言語を使うより（慣れていれば）C++で十分だよなあと思います。たぶん、Raspberry Piのデフォルトのg++は古いので、<a href="https://solarianprogrammer.com/2015/01/13/raspberry-pi-raspbian-install-gcc-compile-cpp-14-programs/" target="_blank">ココ</a>等を参考に新しいバージョンのgccをインストールして使いましょう。

もちろん、<a href="https://github.com/ryuichiueda/RPiM/blob/master/201507/bz_auto.py" target="_blank">Pythonの例もGitHubに置いている</a>ように、特にシェルスクリプトにこだわる必要はなく、研究用の実験をしないならC++にこだわる必要もありません。むしろ言語を選べるように「デバイスファイルで字を読み書きする」という仕様にしましたので、みなさんもいろんな言語でロボットを動かしてみていただければと。個人的にはHaskell希望です。

ところでC++で動かしたロボットの動画はないのかというところですが、実験結果は論文が採択されるまで公表できません。また、どんな言語で動かしてもロボットの動きは一緒ですので、割愛ということで・・・


現場からは以上です。

<iframe src="http://rcm-fe.amazon-adsystem.com/e/cm?lt1=_blank&bc1=000000&IS2=1&bg1=FFFFFF&fc1=000000&lc1=0000FF&t=ryuichiueda-22&o=9&p=8&l=as4&m=amazon&f=ifr&ref=ss_til&asins=4797375957" style="width:120px;height:240px;" scrolling="no" marginwidth="0" marginheight="0" frameborder="0"></iframe>



