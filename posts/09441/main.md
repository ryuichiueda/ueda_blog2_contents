---
Keywords:プログラミング,GlueLang
Copyright: (C) 2017 Ryuichi Ueda
---

# GlueLangのwhere句の実装
　<a href="https://ryuichiueda.github.io/GlueLangDoc_ja/">GlueLang</a>は、その場で使うファイルを次のような書き方で作れます。Haskellから拝借しました。bashの$()がコマンドの引数にあると綺麗に見えないので、whereの中にそういう細かい処理は押し込んでしまおうという意図です。<br />
<br />
[bash]<br />
import PATH<br />
<br />
#passwdファイルの一番下のユーザの名前でpasswdファイルをgrepする<br />
grep re '/etc/passwd'<br />
 where<br />
 str re = tail -n 1 '/etc/passwd' &gt;&gt;= awk '-F:' '{print $1}'<br />
[/bash]<br />
<br />
bashだとこうなります。<br />
<br />
[bash]<br />
grep $( tail -n 1 '/etc/passwd' | awk '-F:' '{print $1}' ) '/etc/passwd'<br />
[/bash]<br />
<br />
　これの実装をするにはスコープを真面目に設計・実装する必要がありますが、GlueLangはシェルなので、基本「スコープはforkしたときに持っていた情報の範囲」で良く、whereのためだけにスコープを作ることになります。これがこれまでグダグダだったので、昨夜遅くコソコソと直してました。具体的には、<br />
<br />
<ul><br />
	<li>変数に、どのジョブに属するのかIDをつける	</li><br />
	<li>各要素が解釈されたときに、要素のインスタンスにこれまで分岐してきたジョブのリストを渡す</li><br />
	<li>変数を探すときに、そのリストの逆向きたどる</li><br />
<br />
</ul><br />
<br />
という処理を加えました。リストを解釈された要素全部に渡すので無駄なのと、ジョブが消えても変数が残ったままになっているという状況ですが、あとから改善します。<br />
<br />

