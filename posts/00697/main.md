# pmat version 0.001
この前のこの件（<a href="http://blog.ueda.asia/?p=674" title="こういう行列計算コマンドを考えついた">こういう行列計算コマンドを考えついた</a>）、とりあえずは行動ということで、まだかけ算しかできないもののコードを晒してみました。<br />
<br />
<a target="_blank" href="https://github.com/ryuichiueda/PMAT/blob/a56e77cf8416da50b0f75a9bfddcfe1e48989c1d/pmat.hs" title="pmat.hs">GitHubに晒したコード。荒削り風味。</a><br />
<br />
hmatrixというライブラリを入れるのに一苦労。使いこなすのに一苦労。<br />
<br />
これから数式のパーサをゴリゴリ書く予定デス。<br />
<br />
[bash]<br />
ueda\@ubuntuonmac:~/GIT/PMAT$ cat data<br />
A 1 2 3<br />
A 1 2 3<br />
B -1 2 3.0<br />
B 1 -2 3.1<br />
B 1 2 -3.2<br />
ueda\@ubuntuonmac:~/GIT/PMAT$ cat data | ./pmat &quot;式はまだパースしないよーん&quot;<br />
A 1 2 3<br />
A 1 2 3<br />
B -1 2 3.0<br />
B 1 -2 3.1<br />
B 1 2 -3.2<br />
A*B 4.0 4.0 -0.40000000000000213<br />
A*B 4.0 4.0 -0.40000000000000213<br />
[/bash]<br />
<br />
コードをダウンロードしてもコンパイルまで辿り着ける人は皆無と思われるので、ある程度動くようになったらコンパイル済みのバイナリをGitHubに置く事にします。
