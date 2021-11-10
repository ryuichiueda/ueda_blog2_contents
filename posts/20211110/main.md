---
Keywords: 日記, CUDA
Copyright: (C) 2021 Ryuichi Ueda
---

# 日記（2021年11月10日）

　本日はリモート講義のあと共同研究で企業の方とミーティング。学科の催事の日程調整等。ミーティング、朝の時点では把握してたけど直前にあるのを忘れていて慌てた。


## はじめてのCUDAプログラミング


　昔から速いコードを書くことを活路としてきたのにGPUを使えないままでいるのはロートル一直線だという後ろ向きな理由で、今日から始めることにしました。幸い、仕事で使っているLinuxの環境が、


```
$ nvidia-smi
Wed Nov 10 21:10:27 2021
+-----------------------------------------------------------------------------+
| NVIDIA-SMI 460.91.03    Driver Version: 460.91.03    CUDA Version: 11.2     |
|-------------------------------+----------------------+----------------------+
| GPU  Name        Persistence-M| Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp  Perf  Pwr:Usage/Cap|         Memory-Usage | GPU-Util  Compute M. |
|                               |                      |               MIG M. |
|===============================+======================+======================|
|   0  Quadro T2000 wi...  Off  | 00000000:01:00.0 Off |                  N/A |
| N/A   50C    P8     5W /  N/A |   1378MiB /  3911MiB |      0%      Default |
|                               |                      |                  N/A |
+-------------------------------+----------------------+----------------------+

+-----------------------------------------------------------------------------+
| Processes:                                                                  |
|  GPU   GI   CI        PID   Type   Process name                  GPU Memory |
|        ID   ID                                                   Usage      |
|=============================================================================|
|    0   N/A  N/A      1282      G   /usr/lib/xorg/Xorg                141MiB |
|    0   N/A  N/A      2616      G   /usr/lib/xorg/Xorg                527MiB |
|    0   N/A  N/A      2804      G   /usr/bin/gnome-shell              167MiB |
|    0   N/A  N/A    180293      G   ...AAAAAAAAA= --shared-files      142MiB |
|    0   N/A  N/A    201049      G   ...AAAAAAAAA= --shared-files       92MiB |
|    0   N/A  N/A    201075      G   ...AAAAAAAAA= --shared-files      287MiB |
+-----------------------------------------------------------------------------+
```


という感じで整っていたので、あとは

```
$ sudo apt install nvidia-cuda-*
```

して、コードを書いてコンパイルすれば動くという状況から開始できました。

### コンパイルの方法

　で、「コードを書いてコンパイル」をどうすりゃいいんだと調べたら、どうやら`nvcc`というコマンドを使うらしいと判明。これでCで書いてもC++で書いてもよしなにコンパイルしてくれるとのこと。


### コード

　次に何か簡単なコードを書いて実行してみようということになり、C++の例を探したところ、公式のドキュメントで発見。


<blockquote class="twitter-tweet"><p lang="ja" dir="ltr">まずここらへん読まんとあかんっぽい。はらへった。<a href="https://t.co/ILe9pfonQ3">https://t.co/ILe9pfonQ3</a></p>&mdash; 上田 隆一 (@ryuichiueda) <a href="https://twitter.com/ryuichiueda/status/1458338511707582464?ref_src=twsrc%5Etfw">November 10, 2021</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>


ただ、見ると分かるんですけどGPUに処理をさせる前後のコードが省略されており（なんで省略するんだろ？）、予想して書かないといけません。で、https://qiita.com/wazakkyd/items/8a5694e7a001465b6025 の
C言語での実装を参考にして前後を付け足し、次のようなコードを書きました。



<script src="https://gist-it.appspot.com/ryuichiueda/my_cuda_practice/blob/master/hoge.cu"></script>



