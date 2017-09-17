# 今日のGlueLang開発日誌（シグナル処理、whereでの条件指定等）
今週末も時間をやりくりしながらGlueLangの開発を進めました。<a href="http://blog.ueda.asia/?p=4960" title="GlueLangでとうとうwhereが使えるように" target="_blank">昨日</a>の作業に加え、今日はシグナル処理を改善して、中間ファイルと作業ディレクトリが残らないようにしました。ただ、何でちゃんと動くのか分からないという有様なので、dashのコードを読んでちゃんと勉強せんといかんなあと思います。<br />
<br />
<br />
あと、2月末にとうとうお披露目のプレゼンをするかもしれないので、次のような機能をデモ程度に実装しました。<br />
<br />
<!--more--><br />
<br />
<script src="https://gist.github.com/ryuichiueda/94bd4c96775289b2f807.js"></script><br />
<br />
stringにaaaaaaaaaaaaaaaa...という文字列を代入するというコードですが、whereに「この変数hogeには10文字以上の文字列を入れてはいけない」という条件を書いています。<br />
<br />
このコード、次の実行結果のようになります。今のところ。<br />
<br />
<script src="https://gist.github.com/ryuichiueda/a87002775622f2bdf3a6.js"></script><br />
<br />
とにかく業務用のコードを書くとチェックのコードだらけになってコードの本筋が見えなくなるので、whereの下に押し込んでしまえという試みです。<br />
<br />
 「cond hoge : length < 10」という書き方も洗練されていなければ、「length <」以外の条件もまだ使えないのですが、コンセプトとしてどうでしょうか？<br />
<br />
しかし、チェックはコマンド等でも行えるので、どうやって住み分けするか、という課題はあるかもしれません。<br />
<br />
それではまた来週末。<br />
<br />
<br />
寝る。
