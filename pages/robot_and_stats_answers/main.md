---
Copyright: (C) Ryuichi Ueda
---

# ロボットの確率・統計問題集（問題）

## 1章

### 20240527_1

　順位が常に入れ替わっていても筆者が1位になった瞬間だけSNSにアップしているとずっと1位になっているように見えるので，それを勘違いしないように受け取らないといけません．

[（戻る）](/?page=robot_and_stats_questions#20240527_1)

### 20240921_1

　シェルを使う例を挙げておきます．答えは`209.7`です．

```bash
$ curl https://raw.githubusercontent.com/ryuichiueda/LNPR_BOOK_CODES/refs/heads/master/sensor_data/sensor_data_200.txt > a
$ cat a | awk '{a+=$4}END{print a/NR}'
209.737
### 別解（コマンドは各自インストールを）###
$ cat a | tr ' ' '\t' | datamash mean 4
209.7371329762
```

[（戻る）](/?page=robot_and_stats_questions#20240921_1)


### 20240924_1

　こちらもシェルを使う例を挙げておきます．平均値は[20240921_1](#20240921_1)のものを使用。1列目が分散、2列目が標準偏差です。

```bash
$ cat a | awk '{a+=($4-209.7371329762)**2}END{print a/(NR-1), sqrt(a/(NR-1))}'
23.4081 4.83819
### 別解 ###
$ cat a | tr ' ' '\t' | datamash svar 4 sstdev 4
23.408106598555	4.8381924929207
```

[（戻る）](/?page=robot_and_stats_questions#20240924_1)

### 20240927_1

\\(\sigma^2\\)を不偏分散とすると、

$$\sigma^2 = \frac{1}{N-1}\sum_{i=1}^N (x_i - \bar{x})^2$$

となります。ここで

$$\bar{x} = \frac{1}{N}\sum_{i=1}^N x_i $$

です。

[（戻る）](/?page=robot_and_stats_questions#20240927_1)

### 20240924_3

例です．（問題にも書きましたが代表値は万能ではないので，必ず異議が生じることを考慮する必要があります．）

* 平均値が計算できると，何人かのテスト結果を比較して1人選抜しなければならない場合，欠席等でテストを受けた回数が違っても，互いの成績を比較することができる．

[（戻る）](/?page=robot_and_stats_questions#20240924_3)


## 2章

### 20241004_3

$$P(X, Y, Z) = P(X, Y | Z)$$
$$P(Y, Z | X) = P(Y , Z| X)$$

## 3章

### 20241005_2

\begin{align}
\langle f \rangle_p &= \langle ax + b \rangle_{p(x)} \\\\
&= a \langle x  \rangle_{p(x)} + b \quad (\because \text{期待値の線型性}) \\\\ 
&= a \mu + b \quad (\because \mu = \langle x \rangle_{p(x)}) 
\end{align}

[（戻る）](/?page=robot_and_stats_questions#20241005_2)

### 20241005_1

\begin{eqnarray}
\sigma^2 &=& \langle (x - \mu)^2 \rangle_{p(x)} \\\\
&=& \langle x^2 -2 x\mu -\mu^2 \rangle_{p(x)} \\\\
&=& \langle x^2 \rangle_{p(x)} -2\mu\langle x \rangle_{p(x)} + \mu^2 \\\\
&=& \langle x^2 \rangle_{p(x)} -2\mu^2 + \mu^2  \quad (\because \mu = \langle x \rangle_{p(x)}) \\\\
&=& \langle x^2 \rangle_{p(x)} - \mu^2
\end{eqnarray}

[（戻る）](/?page=robot_and_stats_questions#20241005_1)

## 4章

### 20240927_2

$$p(x | \mu, \sigma^2 ) = \frac{1}{\sqrt{2\pi\sigma^2}} e^{ - \frac{(x - \mu)^2}{2\sigma^2}}$$

となります。ここで\\(\mu\\)は\\(x\\)の平均値、\\(\sigma^2\\)は分散です。

[（戻る）](/?page=robot_and_stats_questions#20240927_2)

### 20240924_2

* 例（ちょっとごまかしがあるかもしれませんが）

　\\(x\\)が連続的な値をとるとき、確率は「発生する\\(x\\)の値のうち，\\(x\\)がある範囲に入る割合」として定義される．1つの任意の\\(x\\)の値に対してこの範囲を狭めていくと確率は0に近づいていく．一方で，\\(p\\)の数値はとり得る任意の\\(x\\)に対しては0より大きい固定値で，0には近づかない．したがって\\(p\\)から得られる値は確率ではない．

[（戻る）](/?page=robot_and_stats_questions#20240924_2)
