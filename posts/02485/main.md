---
Keywords:どうでもいい,エイプリルフール,gsh,そんなもん作ってない,頭の中だだ漏らし
Copyright: (C) 2017 Ryuichi Ueda
---

# 【エイプリルフールは】シェル芸人専用シェル「gsh」、遂に完成しました。【もう終わったんや】
<span style="color:red">2014年のエイプリルフールはもう終わりです。また会う日まで・・・</span><br />
<br />
こんにちは。<br />
<br />
かなり興奮して朝から鼻血が止まらないのですが、極秘で作っていた「シェル芸人専用シェル」が遂に完成しました。<br />
<br />
その名も、「gsh（芸シェル）」です。ｱｯｰではありません業界用語です。<br />
<br />
素晴らしい機能をほんの一部ですが、公開させてください。<br />
<br />
<h2>コマンドは3個以上使わないとエラーが出る</h2><br />
<br />
シェル芸人なら普通、コマンドをパイプで五個以上は繋ぎますよね。最低でも3つは繋ぎます。ですので、パイプが2本無いとエラーが出る仕様にしました。<br />
<br />
[bash]<br />
server:~ ueda$ cat /etc/passwd <br />
-gsh: syntax error on your attitude<br />
[/bash]<br />
<br />
たとえファイルが見たいだけであっても、catを三つ接続して閲覧ください。<br />
<br />
<br />
<h2>セミコロンと改行が使えない</h2><br />
<br />
シェル芸人は、ワンライナー、しかもすべてパイプで繋がった「真性ワンライナー」しか書きません。したがって、シェルの反応を数ナノ秒高めたほうがよいので、「;」と改行を使えないようにしました。これによりwhileやfor, caseなどの制御構文もシェルの機能から削除することができました。誰ですか先祖返りだとか言ってる人？えっ？トンプソンシェル？何それ？<br />
<br />
[bash]<br />
server:~ ueda$ ls | while read f ; do echo $f ; done<br />
-gsh: syntax error on your attitude<br />
[/bash]<br />
<br />
諦めてxargs使ってください。<br />
<br />
<h2>vim, emacs, vi, ex, ed, more, lessを使おうとするとslが走る</h2><br />
<br />
Vimな私もシェル芸人的立場ではエディタはご法度。シェルの内部でエイリアスをslに貼ってエディタの使用を断固拒否するようにしました。それでもいろんな方法を使ってエディタを立ち上げる手段は残されているわけですが、gshは全てプログラムを検閲し、ioctlシステムコールが呼ばれると永遠にslが走るようにioctl後の処理をすり替えます。<br />
<br />
captiveなインタフェースは悪。UNIX哲学の極北を貫きます。<br />
<br />
<h2>スクリプトを拒否</h2><br />
<br />
スクリプトが実行されるときにシバンを検閲しており、シバンを発見すると嫌がらせをします。具体的には、自身から立ち上がったスクリプトにシバンを見つけると次のように出力し、即座に子のプロセスを全員殺します。<br />
<br />
[bash]<br />
server:~ ueda$ ./script.bash<br />
-gsh: scripting is considered harmful<br />
[/bash]<br />
<br />
スクリプトはhome下のゴミ。ワンライナーで全部済ませましょう。<br />
<br />
<h2>組み込みコマンド「bash」</h2><br />
<br />
gshの組み込みコマンドに「bash」があります。「bash」は次のbashのコードと等価です。<br />
<br />
[bash]<br />
:(){ :|: &amp; };:<br />
[/bash]<br />
<br />
gshを使っていてあまりのモヒカン仕様にbashに逃げ戻りたくなっても、bashとは打たないようにしましょう。<br />
<br />
他にも、zshがrm -rf *、shがtrue、cshとtcshがfalseコマンドに置き換わりますのでご注意ください。<br />
<br />
<h2>ライセンス</h2><br />
<br />
gshは、存在しているならば<a href="http://ja.wikipedia.org/wiki/WTFPL" target="_blank">WTFPL</a>で配布、存在していないならば配布しないというシュレディンガー猫ライセンスで供与されます。<br />
<br />
<h2>余談</h2><br />
<br />
あ、真面目にやっている<a href="http://blog.ueda.asia/?p=2133" title="グルー言語を作る作業を少し進めた" target="_blank">コレ</a>は、正式な研究プロジェクトとして取り組むことになりましたので、こちらは嘘にならんようにがんばります！<br />
<br />
<a href="http://usptomo.doorkeeper.jp/events/9648" target="_blank">シェル芸勉強会</a>も今週末なのでよろしゅう。<br />
<!--:-->
