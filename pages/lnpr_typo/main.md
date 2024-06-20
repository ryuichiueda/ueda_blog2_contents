---
Keywords: 詳解確率ロボティクス
Copyright: (C) Ryuichi Ueda
---

# 詳解確率ロボティクスの訂正・コードのアップデート

## コードのアップデート

Pythonやライブラリ、Jupyterなどの仕様変更によるコードの修正です。こちらはGitHubのコードに随時反映しています。本の内容については、もし第2版が出たらそのときにアップデートします。アップデート前のコードについては、横にコメントアウトして残してあるので、もし動かないときは、そちらのコードを試してみてください。

### 2024年6月更新分

* [section_kalman_filter/kf3.ipynb](https://github.com/ryuichiueda/LNPR_BOOK_CODES/blob/master/section_kalman_filter/kf3.ipynb) 
* [section_kalman_filter/kf4.ipynb](https://github.com/ryuichiueda/LNPR_BOOK_CODES/blob/master/section_kalman_filter/kf4.ipynb) 
    * どのバージョンからかは調べてませんが、`scipy.stats.multivariate_normal`の`cov`を直接書き換えられなくなりました。`kf3.ipynb`で書き直した`motion_update`、`kf4.ipynb`で書き直した`observation_update`を掲載します。

```python
    def motion_update(self, nu, omega, time): #追加
        if abs(omega) < 1e-5: omega = 1e-5 #値が0になるとゼロ割りになって計算ができないのでわずかに値を持たせる

        M = matM(nu, omega, time, self.motion_noise_stds)
        A = matA(nu, omega, time, self.belief.mean[2])
        F = matF(nu, omega, time, self.belief.mean[2])
        cov = F.dot(self.belief.cov).dot(F.T) + A.dot(M).dot(A.T)             #旧バージョンではself.belef.covに直接代入
        mean = IdealRobot.state_transition(nu, omega, time, self.belief.mean) #旧バージョンではself.belef.meanに直接代入
        self.belief = multivariate_normal(mean=mean, cov=cov)                 #旧バージョンではこの行なし
        self.pose = self.belief.mean #他のクラスで使う

    def observation_update(self, observation):  #追加
        mean, cov = self.belief.mean, self.belief.cov #旧バージョンではこの行なし
        for d in observation:
            z = d[0]
            obs_id = d[1]
            
            H = matH(mean, self.map.landmarks[obs_id].pos)
            estimated_z = IdealCamera.observation_function(mean, self.map.landmarks[obs_id].pos)
            Q = matQ(estimated_z[0]*self.distance_dev_rate, self.direction_dev)
            K = cov.dot(H.T).dot(np.linalg.inv(Q + H.dot(cov).dot(H.T)))
            mean += K.dot(z - estimated_z)          #旧バージョンではself.belief.meanを直接更新
            cov = (np.eye(3) - K.dot(H)).dot(cov)  #旧バージョンではself.belief.covを直接更新 
            
        self.belief = multivariate_normal(mean=mean, cov=cov) #旧バージョンではこの行なし
        self.pose = self.belief.mean
```

### 2023年4月更新分

情報提供いただきました。ありがとうございます。

<blockquote class="twitter-tweet" data-conversation="none" data-cards="hidden" data-partner="tweetdeck"><p lang="ja" dir="ltr">lidar_200.ipynbの9のfreq[“lidar”]で失敗します。<br>8のDataframeを作る際にvalue_countからの返り値を渡してますが、これにcountという名前がつくようになったためっぽいです。</p>&mdash; 女児 (@YuK_Ota) <a href="https://twitter.com/YuK_Ota/status/1652485372444803072?ref_src=twsrc%5Etfw">April 30, 2023</a></blockquote>
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>


* [section_sensor/lidar_200.ipynb](https://github.com/ryuichiueda/LNPR_BOOK_CODES/blob/master/section_sensor/lidar_200.ipynb)セル[9]: Pandas 2.x系で、前のセルの`value_count`が集計した列に`count`と名前をつけるようになったことに対するコードの修正。

```python

freqs["probs"] = freqs["count"]/len(freqs["count"]) # 古いバージョン: freqs["probs"] = freqs["lidar"]/len(data["lidar"]) ###addprobs###
freqs.transpose()
```



* [section_sensor/lidar_600.ipynb](https://github.com/ryuichiueda/LNPR_BOOK_CODES/blob/master/section_sensor/lidar_600.ipynb)セル[11]
* [section_sensor/lidar_600.ipynb](https://github.com/ryuichiueda/LNPR_BOOK_CODES/blob/master/section_sensor/lidar_600.ipynb)セル[13]
    * pandas（2.x）でデータが自動でソートされなくなったことへの対応。`sort_values`をくっつけました。

```python

### lidar_600.ipynbセル[11] ###
p_z = pd.DataFrame(probs.transpose().sum()).sort_values("lidar")  #行と列を転置して各列を合計 #旧バージョン: p_z = pd.DataFrame(probs.transpose().sum())
p_z.plot()
p_z.transpose()
### lidar_600.ipynbセル[13] ###
cond_z_t = (probs/p_t[0]).sort_values("lidar")  #列（時間）ごとにP(t)で割るとP(x|t)となる   ###lidar600cond #旧バージョン: cond_z_t = probs/p_t[0]
cond_z_t
```

* [section_sensor/lidar_600.ipynb](https://github.com/ryuichiueda/LNPR_BOOK_CODES/blob/master/section_sensor/lidar_600.ipynb)セル[8]
* [section_sensor/multi_gauss1.ipynb](https://github.com/ryuichiueda/LNPR_BOOK_CODES/blob/master/section_sensor/multi_gauss1.ipynb)セル[1]最後から2行目
* [section_sensor/multi_gauss2.ipynb](https://github.com/ryuichiueda/LNPR_BOOK_CODES/blob/master/section_sensor/multi_gauss2.ipynb)セル[2]
    * seaborn（0.12以降？）の`jointplot`の引数が変わったことへの対応。このコードで動かない場合は、`matplotlib`もアップデートが必要。

```python

### lidar_600.ipynb ###
sns.jointplot(data, x="hour", y="lidar", kind="kde") #古いバージョン: sns.jointplot(data["hour"], data["lidar"], data, kind="kde")
plt.show()

### multi_gauss1.ipynb ###
sns.jointplot(d, x="ir", y="lidar", kind="kde") #旧バージョン: sns.jointplot(d["ir"], d["lidar"], d, kind="kde")
plt.show()

### multi_gauss2.ipynb ###
sns.jointplot(d, x="ir", y="lidar", kind="kde") #度数分布を描画 #旧バージョン: sns.jointplot(d["ir"], d["lidar"], d, kind="kde")
d.cov()
```

## 訂正事項

|場所|訂正事項|発見者|一言|
|:---|:-----|------|:-----|
|p.143 式(6.15)の真ん中の行列の2行目|\\( \omega \Longrightarrow \omega_t \\)|<blockquote class="twitter-tweet" data-partner="tweetdeck"><p lang="ja" dir="ltr"><a href="https://twitter.com/ryuichiueda?ref_src=twsrc%5Etfw">@ryuichiueda</a><br>上田先生，突然のリプライすみません．読み進めるには支障がない些細なことですが，詳解確率ロボティクス(第5刷)p.143の式(6.15)で添字のtが1カ所抜けていました． <a href="https://t.co/XkSqBuvN7E">pic.twitter.com/XkSqBuvN7E</a></p>&mdash; Camellia-W (@MT20107) <a href="https://twitter.com/MT20107/status/1633085389186682880?ref_src=twsrc%5Etfw">March 7, 2023</a></blockquote>|見落としてました・・・|
|p.254 コード2行目のコメント|KfAgent \\(\Longrightarrow\\) EstimationAgent|上田|コメントなので油断しました。|
|p.262 2行目|角度と角速度 \\(\Longrightarrow\\) 速度と角速度|<blockquote class="twitter-tweet"><p lang="ja" dir="ltr">写真の10.3.2のヒートマップの後の３行目の文章で「制御指令値の角度と角速度を足す」も「〜速度と角速度を足す」ですかね？（kindle版なんでページ数はわかりません） <a href="https://t.co/ZEgTCJsHWl">pic.twitter.com/ZEgTCJsHWl</a></p>&mdash; sumeragiagito (@sumeragiagito) <a href="https://twitter.com/sumeragiagito/status/1798003548325888370?ref_src=twsrc%5Etfw">June 4, 2024</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>|第5刷で訂正したp.91のと同じです🙏|
|p.321 amdp6.ipynbの102行目| dp.obs_... \\(\Longrightarrow\\) self.obs_... | https://github.com/ryuichiueda/LNPR_BOOK_CODES/issues/6 |一応これでも動きますが、申し訳ないっ！|
|p.325 amdp7.ipynbの116行目| dp.obs_... \\(\Longrightarrow\\) self.obs_... | https://github.com/ryuichiueda/LNPR_BOOK_CODES/issues/6 |同上|
|p.334 セル[8]の2行目| beta_0 \\(  \Longrightarrow \\) zeta_0 | https://github.com/ryuichiueda/LNPR/issues/1 |すみません！下の計算結果は、運の良いことにわずかに違うだけになります。|

## 第6刷で訂正済み


|場所|訂正事項|発見者|一言|
|:---|:-----|------|:-----|
|p.247 12行目|消費電力量を0からマイナスしたものに-1をかけたものを \\( \Longrightarrow \\)消費電力量に-1をかけたものを|<blockquote class="twitter-tweet" data-partner="tweetdeck"><p lang="ja" dir="ltr"><a href="https://twitter.com/ryuichiueda?ref_src=twsrc%5Etfw">@ryuichiueda</a> 様、<br> 『詳解確率ロボティクス』(第1刷)について質問です。<br><br>第10章 p.247 の赤線部分（写真）。ここは、<br>「消費電力量を0からマイナスしたものを r に使うと」<br>もしくは、<br>「消費電力量に-1をかけたものを r に使うと」<br>の間違いではないでしょうか？<br><br> <a href="https://twitter.com/hashtag/%E8%A9%B3%E8%A7%A3%E7%A2%BA%E7%8E%87%E3%83%AD%E3%83%9C%E3%83%86%E3%82%A3%E3%82%AF%E3%82%B9?src=hash&amp;ref_src=twsrc%5Etfw">#詳解確率ロボティクス</a> <a href="https://t.co/y7NnKGVg6p">pic.twitter.com/y7NnKGVg6p</a></p>&mdash; Shuuji Kajita (@s_kajita) <a href="https://twitter.com/s_kajita/status/1485847884314537988?ref_src=twsrc%5Etfw">January 25, 2022</a></blockquote><script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>|いとこのいとこは自分だみたいな文になってますね・・・|

### 第5刷で訂正済み

|場所|訂正事項|発見者|一言|
|:---|:-----|------|:-----|
|p.8 14行目|一般的 \\( \Longrightarrow \\) 一般化  | <blockquote class="twitter-tweet" data-partner="tweetdeck"><p lang="ja" dir="ltr"><a href="https://twitter.com/ryuichiueda?ref_src=twsrc%5Etfw">@ryuichiueda</a> 突然のリプライ失礼いたします。『詳解確率ロボティクス』(Kindle版)で誤字と思われる箇所があったためご連絡します。既知でしたらすみません。<br><br>第1章1.2の「・第二次世界大戦前後」の後ろから2文目「これらの方程式は制御を究極的に一般的したものであり，〜．」の「一般的した」です。</p>&mdash; smalltech (@smalltech_bw) <a href="https://twitter.com/smalltech_bw/status/1380757036833501185?ref_src=twsrc%5Etfw">April 10, 2021</a></blockquote> | 変換ミスです・・・|
|p.20 下から2行目|頻度が大きい \\( \Longrightarrow \\) 頻度が高い  | 上田 | 頻度は「高い」「低い」です。 |
|p.91 1、3行目|角度、角速度\\( \Longrightarrow \\)速度、角速度|<blockquote class="twitter-tweet" data-partner="tweetdeck"><p lang="ja" dir="ltr"><a href="https://twitter.com/ryuichiueda?ref_src=twsrc%5Etfw">@ryuichiueda</a> p.91の1行目、3行目の「角度、角速度」は「速度、角速度」ですかね。<a href="https://twitter.com/hashtag/%E8%A9%B3%E8%A7%A3%E7%A2%BA%E7%8E%87%E3%83%AD%E3%83%9C%E3%83%86%E3%82%A3%E3%82%AF%E3%82%B9?src=hash&amp;ref_src=twsrc%5Etfw">#詳解確率ロボティクス</a></p>&mdash; Usk Tamura (@slx01) <a href="https://twitter.com/slx01/status/1300707440611139584?ref_src=twsrc%5Etfw">September 1, 2020</a></blockquote>|1箇所ならともかくコピペで2箇所間違えました。|
|p.96 `noise_simulation7` `.ipynb [3]` 19行目、p.97 `noise_simulation8` `.ipynb [3]` 26行目、p.98 `noise_simulation9` `.ipynb [3]` 31、38行目、p.99 `noise_simulation10` `.ipynb [3]` 47行目、p.127 `mcl11.ipynb [2]` 19行目| `relative_polar_pos` $$\longrightarrow$$ `observation_function`|<blockquote class="twitter-tweet"><p lang="ja" dir="ltr">p.96: noise_simulation7.ipynb [3] 19行目、p.97: noise_simulation8.ipynb [3] 26行目、p.98: noise_simulation9.ipynb [3] 31行目, 38行目、p.99: noise_simulation10.ipynb [3] 47行目、p.100: noise_simulation11.ipynb [3] 55行目。</p>&mdash; Usk Tamura (@slx01) <a href="https://twitter.com/slx01/status/1300956652661665792?ref_src=twsrc%5Etfw">September 2, 2020</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>|コードの差し替えミスでした。|
|p.173 式(7.33)、式(7.35)|\\( (1-\tilde{N})/N \\) \\( \Longrightarrow \\)  \\( (N-\tilde{N})/N \\)|<blockquote class="twitter-tweet" data-partner="tweetdeck"><p lang="ja" dir="ltr">詳解確率ロボティクスのp173のP(Υ=1)とP(Υ=0)の和が1にならないのはなんでや…<br>誰か有能な方教えてください</p>&mdash; M (@p_x9) <a href="https://twitter.com/p_x9/status/1303375562061176833?ref_src=twsrc%5Etfw">September 8, 2020</a></blockquote>|算数は苦手です。|

### 第4刷で訂正済み

|場所|訂正事項|発見者|一言|
|:---|:-----|------|:-----|
|p.56 式(2.94)|積分は不要|上田|\\( \boldsymbol{x}\\)で積分したら\\(p_3\\)が\\( \boldsymbol{x} \\)の関数にならないじゃないか・・・|
|p.62|section_sentor \\( \Longrightarrow \\) section_sensor|<blockquote class="twitter-tweet" data-conversation="none" data-cards="hidden" data-partner="tweetdeck"><p lang="ja" dir="ltr">たびたびすみません。P62の3.2.1に「コーディングは、section_sentorのとなり」と記載されていますが、section_sensorの誤記でしょうか？<br>（粗探しや間違い探しなどしてません！偶然見つかりました😭）</p>&mdash; と雷 (@chmod_x_akasit) <a href="https://twitter.com/chmod_x_akasit/status/1272394146536321024?ref_src=twsrc%5Etfw">June 15, 2020</a></blockquote>|sentorとは。|
|p.80 `ideal_robot10.ipynb [7]` 21行目| `relative_polar_pos` $$\longrightarrow$$ `observation_function`|[@maskot1977](https://twitter.com/maskot1977)さん|コードの差し替えミスでした。|
|p.186 ページ上にある式番号を振っていない3行の式|1行目から2行目のイコールまでが不要。2行目の「右の分布から不要な・・・」という補足も不要。つまり、2行目と3行目をイコールでつないだ式が書いてあれば十分。|上田|式(8.10)と比べると余計な記述をしていると思いました。|
|p.191 式(8.33)の最後の行列|右上の要素の\\( \ell^2\_{\hat{\boldsymbol{m}}\_{t-1}} \\)と左下の要素の\\( \ell\_{\hat{\boldsymbol{m}}\_{t-1}} \\)を入れ替え|<blockquote class="twitter-tweet"><p lang="ja" dir="ltr">詳解確率ロボティクスp.191 式(8.33)，2段目から3段目への変形で1行2列目の要素と2行1列目の要素の分母が置き換わるところで次数が変わってるのはなんでなんだろう...<br>1行目の要素の分母の次数は1乗で2行目は2乗になるんじゃないのかな</p>&mdash; Kohta (@fjnkt98) <a href="https://twitter.com/fjnkt98/status/1255825300656582656?ref\_src=twsrc%5Etfw">April 30, 2020</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>|コピペミスです・・・。|
|p.196 式(8.54)|\\( \lt N(m) \gt_m \\) \\( \Longrightarrow \\) \\( [[ N(m) ]]_m \\)|上田|凡ミスです。|
|p.233 式(9.65)|\\( \Omega_{j,t} = R_{j,t}Q_{j,t}R_{j,t}^\top \\) \\( \Longrightarrow \\) \\( \Omega_{j,t} = (R_{j,t}Q_{j,t}R_{j,t}^\top)^{-1} \\)|[hotsuyukiさん](https://github.com/ryuichiueda/LNPR_BOOK_CODES/issues/4)|気を抜いておりました・・・|
|p.233 式(9.65)の下の行|写像した共分散行列です。\\( \Longrightarrow \\)写像して得られる精度行列です。|[hotsuyukiさん](https://github.com/ryuichiueda/LNPR_BOOK_CODES/issues/4)|上の訂正に伴う訂正です|
|p.233 セルの24行目、p.237 セルの16行目|右辺の行列を`np.linalg.inv(` `R.dot(Q1).dot(R.T))`と逆行列に訂正|[hotsuyukiさん](https://github.com/ryuichiueda/LNPR_BOOK_CODES/issues/4)|上の訂正に伴う訂正です|
|p.234 図9.12(c)|[この図に差し替え](https://b.ueda.tech/pages/lnpr/9.12c.png)|[hotsuyukiさん](https://github.com/ryuichiueda/LNPR_BOOK_CODES/issues/4)|上の訂正に伴う訂正です|
|p.234 最終行|方向に星印が移動\\( \Longrightarrow \\)方向に、わずかに星印が移動|[hotsuyukiさん](https://github.com/ryuichiueda/LNPR_BOOK_CODES/issues/4)|上の訂正に伴う訂正です|
|p.364 脚注2|共分散行列 \\( \Longrightarrow \\) 半正定値対称行列|<blockquote class="twitter-tweet" data-partner="tweetdeck"><p lang="ja" dir="ltr"><a href="https://twitter.com/ryuichiueda?ref_src=twsrc%5Etfw">@ryuichiueda</a>  唐突なツイート失礼します詳解確率ロボティクスの内容について質問です。<br>P364の注2に「B.1.5項の結果から共分散行列と解釈できます」と記載されてますが、半正定値対称行列ではないでしょうか？<br>そうなるとΨが対称行列になるので納得します。</p>&mdash; と雷 (@chmod_x_akasit) <a href="https://twitter.com/chmod_x_akasit/status/1272103493101223936?ref_src=twsrc%5Etfw">June 14, 2020</a></blockquote>|もう少し補足すると共分散行列ではなくて精度行列です。|


### 第3刷で訂正済み

|場所|訂正事項|発見者|一言|
|:---|:-----|------|:-----|
|p.16 本文下から2行目|とうてい受け入れにくい$$\longrightarrow$$とうてい受け入れがたい|上田|「難い」をひらがなに直すときに手違いがありました。|
|p.8 「冷戦期」の下の文|Roudolf$$\longrightarrow$$Rudolf||大変失礼いたしました。|
|p.8 下から10行目|ネリ・ゴードン（Neli ...$$\longrightarrow$$ニール・ゴードン（Neil ...||ずーっと間違えて覚えてました。名前間違えるのは最悪です。すんません・・・|
|p.19 本文9行目|こと分かります。$$\longrightarrow$$ことが分かります。|||
|p.56 数式も含めて10行目|足し合わせもの$$\longrightarrow$$足し合わせたもの|||
|p.121 5.3.4の表題の下の行|$$\delta_{\omega\omega} = 0.2\ \delta_{\nu\omega} = 0$$$$\longrightarrow$$$$\delta_{\omega\omega} = 0.2, \delta_{\nu\omega} = 0$$|||
|p.125 式も含めて下から10行目|は，はそれぞれ$$\longrightarrow$$はそれぞれ|||
|p.147 式(6.26)| $$\hat{\mu}_x - m_y$$ $$\longrightarrow$$ $$\hat{\mu}_y - m_y$$|<blockquote class="twitter-tweet" data-partner="tweetdeck"><p lang="ja" dir="ltr"><a href="https://twitter.com/ryuichiueda?ref_src=twsrc%5Etfw">@ryuichiueda</a> <br>突然のリプライで申し訳ありません。確率ロボティクスの本のP147式6.26ですがy側の信念分布の中心点の係数がxになっている理由を教えていただけないでしょうか。<br>距離計測なのでy成分だと思っていました。</p>&mdash; Acky_F (@AckyF1) <a href="https://twitter.com/AckyF1/status/1216181205361520640?ref_src=twsrc%5Etfw">January 12, 2020</a></blockquote>|校正から漏れました|
|p.156 式も含めて6行目|N個ぶ$$\longrightarrow$$N個選ぶ|||
|p.239 6行目|graphbased_slam..._sensor2$$\longrightarrow$$graphbased_slam...sensor2.ipynb|||
|p.259 本文6行目|区関数$$\longrightarrow$$区間数|||
|p.285 下から3行目|ようにをつけて$$\longrightarrow$$ように値をつけて|||
|p.313 12.4.1の表題の2行上|この方法には$$\longrightarrow$$この方法は|||
|p.315 1行目|越えることに$$\longrightarrow$$越えるごとに|||
|p.327 下から4行目|作ること相当し$$\longrightarrow$$作ることに相当し|||
|p.345 中央|負担率（responsibilty）$$\longrightarrow$$負担率（responsibility）||愛が足りない。|
|p.375 本文下から2行目|リポリトリ$$\longrightarrow$$リポジトリ|||
|p.379 [Gordon 1993]|Neli$$\longrightarrow$$Neil||上に同じ。大変すみません。|
|p.380 [Igl 2018]|Leanring$$\longrightarrow$$Learning||勢いでタイプしてそのままになってました。|
|p.380 [Kalman 1960]|Roudolf$$\longrightarrow$$Rudolf||すみません！|
|p.382 [Sutton 1996]|Advannces$$\longrightarrow$$Advances||Macのキーボードが・・・|

### 第2刷で訂正済み

|場所|訂正事項|発見者|一言  |
|:---|:-----|------|:-----|
|p.75 ideal_robot7.ipynb [6]の6行目 | landmark_id = len(self.landmarks) + 1 $$\longrightarrow$$ landmark_id = len(self.landmarks) | <blockquote class="twitter-tweet"><p lang="ja" dir="ltr"><a href="https://twitter.com/ryuichiueda?ref_src=twsrc%5Etfw">@ryuichiueda</a>「確率ロボティクス」p. 76の図3.9との整合性を取るのであれば，p.75のIn[6]の6行目の最後の部分，”+1&quot;が不要のようです．ご確認ください．</p>&mdash; Kaz Sato (@kankarara) <a href="https://twitter.com/kankarara/status/1188724503632736256?ref_src=twsrc%5Etfw">October 28, 2019</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script> |リポジトリのコードも直しておきました。|
|p.94 4.3節の5行目|次の4種類 $$\longrightarrow$$  次の5種類|<blockquote class="twitter-tweet" data-partner="tweetdeck"><p lang="ja" dir="ltr"><a href="https://twitter.com/ryuichiueda?ref_src=twsrc%5Etfw">@ryuichiueda</a> 「詳解確率ロボティクス」の訂正箇所<br>p. 94：4.3節の初めから5行目「次の4種類」$$\longrightarrow$$ 「次の5種類」<br>p. 99, 100：occulusion $$\longrightarrow$$ occlusion（3箇所）<br>p. 100：cell内の8, 45, 46, 57もocclusionに修正（githubでは修正済み）</p>&mdash; Kaz Sato (@kankarara) <a href="https://twitter.com/kankarara/status/1194058048429445120?ref_src=twsrc%5Etfw">November 12, 2019</a></blockquote>|修正漏れです|
|p.99 下から2,3行目、p.100のコードと1行目|occulusion $$\longrightarrow$$ occlusion |<blockquote class="twitter-tweet" data-partner="tweetdeck"><p lang="ja" dir="ltr"><a href="https://twitter.com/ryuichiueda?ref_src=twsrc%5Etfw">@ryuichiueda</a> 「詳解確率ロボティクス」の訂正箇所<br>p. 94：4.3節の初めから5行目「次の4種類」→「次の5種類」<br>p. 99, 100：occulusion → occlusion（3箇所）<br>p. 100：cell内の8, 45, 46, 57もocclusionに修正（githubでは修正済み）</p>&mdash; Kaz Sato (@kankarara) <a href="https://twitter.com/kankarara/status/1194058048429445120?ref_src=twsrc%5Etfw">November 12, 2019</a></blockquote>|よくやるタイプミス&修正漏れですすみません・・・|
<script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script> |
|p.364 式(B.20)の右辺 | $$-\frac{1}{2}\boldsymbol{x}^\top (G^\top \Sigma_2^{-1} G - \Sigma_1^{-1})\boldsymbol{x}$$ $$\longrightarrow$$ $$-\frac{1}{2}\boldsymbol{x}^\top (G^\top \Sigma_2^{-1} G + \Sigma_1^{-1})\boldsymbol{x}$$|<blockquote class="twitter-tweet" data-conversation="none" data-cards="hidden" data-partner="tweetdeck"><p lang="ja" dir="ltr">唐突なリプすいません。自分も読んでいて、ひとつ気づいたので。。。<br>詳細確率ロボティクス p364 (B.20) Ψ^(-1)に相当する( )中の真ん中の符号、－ではなくて+ではないでしょうか？</p>&mdash; ma2 (@m_ma2) <a href="https://twitter.com/m_ma2/status/1189531321397202944?ref_src=twsrc%5Etfw">October 30, 2019</a></blockquote> |すみません・・・| 



