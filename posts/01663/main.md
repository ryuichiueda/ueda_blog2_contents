---
Keywords: ワンライナー,プログラミング,楽しいお昼休み,シェル芸
Copyright: (C) 2017 Ryuichi Ueda
---

# Rubyでどう書く？：連続した数列を範囲形式にまとめたい．いや，Rubyで書かない．
<a href="http://builder.japan.zdnet.com/script/sp_ruby-doukaku-panel/20369264/" target="_blank">http://builder.japan.zdnet.com/script/sp_ruby-doukaku-panel/20369264/</a>から．

<a href="http://d.hatena.ne.jp/zariganitosh/20131127/succession_hyphen_number" target="_blank">shでの回答</a>もあったので，どうせならもっと強力なワンライナーで．

環境はMac．たぶんもうちょっと短くなる．

```bash
$ echo 1 2 3 5 7 8 | tr ' ' '\\n' |\\
awk '{if(a==$1-1){printf(&quot; %d&quot;,$1)}else{printf(&quot;\\n%d&quot;,$1)}a=$1}' |\\
awk 'NF&gt;1{print $1&quot;-&quot;$NF}NF<=1{print $1}' | tr '\\n' ',' | gsed 's/,$/\\n/g'
1-3,5,7-8
```

gsedはLinuxだとsedでやります．

仕事仕事．
