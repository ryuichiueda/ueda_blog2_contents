---
Keywords: プログラミング,GlueLang
Copyright: (C) 2017 Ryuichi Ueda
---

# GlueLangのwhere句の実装
　<a href="https://ryuichiueda.github.io/GlueLangDoc_ja/">GlueLang</a>は、その場で使うファイルを次のような書き方で作れます。Haskellから拝借しました。bashの$()がコマンドの引数にあると綺麗に見えないので、whereの中にそういう細かい処理は押し込んでしまおうという意図です。

```bash
import PATH

#passwdファイルの一番下のユーザの名前でpasswdファイルをgrepする
grep re '/etc/passwd'
 where
 str re = tail -n 1 '/etc/passwd' &gt;&gt;= awk '-F:' '{print $1}'
```

bashだとこうなります。

```bash
grep $( tail -n 1 '/etc/passwd' | awk '-F:' '{print $1}' ) '/etc/passwd'
```

　これの実装をするにはスコープを真面目に設計・実装する必要がありますが、GlueLangはシェルなので、基本「スコープはforkしたときに持っていた情報の範囲」で良く、whereのためだけにスコープを作ることになります。これがこれまでグダグダだったので、昨夜遅くコソコソと直してました。具体的には、

<ul>
	<li>変数に、どのジョブに属するのかIDをつける	</li>
	<li>各要素が解釈されたときに、要素のインスタンスにこれまで分岐してきたジョブのリストを渡す</li>
	<li>変数を探すときに、そのリストの逆向きたどる</li>

</ul>

という処理を加えました。リストを解釈された要素全部に渡すので無駄なのと、ジョブが消えても変数が残ったままになっているという状況ですが、あとから改善します。


