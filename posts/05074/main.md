---
Keywords: バックグラウンドジョブ,バックグラウンドプロセス,glue,GlueLang,グルー言語を作る
Copyright: (C) 2017 Ryuichi Ueda
---

# GlueLangにバックグラウンドジョブの機能を追加
今日の作業でGlueLangにシェルの「&」に相当する部分を追加しました。&を>>や>>=でつながっているコマンド達（ジョブ）の後ろにくっつけると、Glueはそいつらを起動してすぐに次の行に制御を移します。

<!--more-->

次の例では、3行目の3つのコマンドが起動したらすぐに4行目に制御が移ります。

<script src="https://gist.github.com/ryuichiueda/7948f1df952cd12b3be0.js"></script>

したがって、実行すると次のように4行目のbのあとに3行目のcbaが出てきます。

<script src="https://gist.github.com/ryuichiueda/e5d97e9df0ad12354444.js"></script>

普通のシェルと違うのは、上の例にもありますが、「&」の後ろに名前を書けるようにしたことです。

名前は当該のジョブをwaitするときに使います。次の例では、「a」というジョブをwaitしています。in.waitというのは「内部コマンドのwait」という意味です。今日は内部コマンドを起動する仕組みも作りましたが、これの説明はまた後日。

<script src="https://gist.github.com/ryuichiueda/b09ea22bbc66982baf0f.js"></script>

-vオプション付きで実行すると、ちゃんと待つことが分かります。18行目でwaitが終わってから、最後のecho 'b'が実行されています。

<script src="https://gist.github.com/ryuichiueda/f6cfc2bdf9e8d31dc7f0.js"></script>

また、一個のwaitで二つ以上のジョブも待てるようにしました。

<script src="https://gist.github.com/ryuichiueda/8342a14f3153e333aad0.js"></script>

個人的には便利かと。


寝る・・・と言いたいところですが、これから英語サイトの準備をしようかなと。
