---
Keywords: 日記
Copyright: (C) 2019 Ryuichi Ueda
---

# 日記（2019年5月24日）

　都内は暑かったらしいが自宅周辺は爽快そのもの。

## 仕事

　↓この本の付録B〜Dの校正。

<div class="card">
  <div class="row no-gutters">
    <div class="col-md-2">
      <a class="item url" href="https://www.amazon.co.jp/exec/obidos/ASIN/4048930699/ryuichiueda-22"><img src="https://images-fe.ssl-images-amazon.com/images/I/41tcU9fYKbL._SL160_.jpg" width="112" alt="photo"></a>
    </div>
    <div class="col-md-10">
      <div class="card-body">
        <dl class="fn">
          <dt><a href="https://www.amazon.co.jp/exec/obidos/ASIN/4048930699/ryuichiueda-22">フルスクラッチから1日でCMSを作る シェルスクリプト高速開発手法入門 改訂2版</a></dt>
          <dd>[上田 隆一 後藤 大地]</dd>
          <dd>KADOKAWA 2019-06-28 (Release 2019-06-28)</dd>
        </dl>
        <p class="powered-by" >(powered by <a href="https://github.com/spiegel-im-spiegel/amazon-item" >amazon-item</a> v0.2.1)</p>
      </div>
    </div>
  </div>
</div>

## このサイトのアフィリエイト

　Aamzonが今年に入って色々制限したので、[こちら](https://kaereba.com/)などのツールが使えなくて困っていたが、本日解決。↑のようにパーツを作れるようになった。[amazon-itemコマンド](https://github.com/spiegel-im-spiegel/amazon-item)のおかげです。小銭入らない&自著の宣伝できないという問題のよりも、このサイトの作り方を書いたのが↑の本なので、アフィリエイトできないと本で作るシステムの価値が下がるという問題があった。

　amazon-itemでパーツを作るにはテンプレートが必要で、これは次のようなものを使用。

```
{{ range .Items }}
<div class="card">
  <div class="row no-gutters">
    <div class="col-md-2">
      <a class="item url" href="{{ .URL }}"><img src="{{ .MediumImage.URL }}" width="{{ .MediumImage.Width }}" alt="photo"></a>
    </div>
    <div class="col-md-10">
      <div class="card-body">
        <dl class="fn" style="font-size:80%">
          <dt><a href="{{ .URL }}">{{ .ItemAttributes.Title }}</a></dt>
          {{ with .ItemAttributes.Author }}<dd>{{ . }}</dd>{{ end }}
          <dd>{{ .ItemAttributes.Publisher }}{{ with .ItemAttributes.PublicationDate }} {{ . }}{{ end }}{{ with .ItemAttributes.ReleaseDate }} (Release {{ . }}){{ end }}</dd>
        </dl>
        <p class="powered-by" >(powered by <a href="{{ $.AppURL }}" >{{ $.AppName }}</a> {{ $.AppVersion }})</p>
      </div>
    </div>
  </div>
</div>
{{ end }}
```

## その他

　Parallel DesktopでUbuntu 19.04を動かそうとしたがParallel Desktop側のユーティリティーがまだ未対応。長女が運動会。指を怪我しているのに色々参加させられそうになったが「無理を言えば帰宅する」と毅然とした態度が取れたそうで◎。先生たちを全体主義の呪縛から解くにはどうすれば良いか。インセンティブが働かないのでなかなか難しい。
