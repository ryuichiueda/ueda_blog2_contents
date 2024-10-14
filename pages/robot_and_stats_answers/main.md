---
Copyright: (C) Ryuichi Ueda
---

# ロボットの確率・統計問題集（答え）

$$\newcommand{\indep}{\mathop{\perp\\!\\!\\!\perp}}$$

## 1章

### 統計のリテラシー

　順位が常に入れ替わっていても筆者が1位になった瞬間だけSNSにアップしているとずっと1位になっているように見えるので，それを勘違いしないように受け取らないといけません．

[（戻る）](/?page=robot_and_stats_questions#統計のリテラシー)

### 大量データの平均値

　シェルを使う例を挙げておきます．答えは`209.7`です．

```bash
$ curl https://raw.githubusercontent.com/ryuichiueda/LNPR_BOOK_CODES/refs/heads/master/sensor_data/sensor_data_200.txt > a
$ cat a | awk '{a+=$4}END{print a/NR}'
209.737
### 別解（コマンドは各自インストールを）###
$ cat a | tr ' ' '\t' | datamash mean 4
209.7371329762
```

[（戻る）](/?page=robot_and_stats_questions#大量データの平均値)


### 大量データのばらつき

　こちらもシェルを使う例を挙げておきます．平均値は[大量データの平均値](#大量データの平均値)のものを使用。1列目が分散、2列目が標準偏差です。

```bash
$ cat a | awk '{a+=($4-209.7371329762)**2}END{print a/(NR-1), sqrt(a/(NR-1))}'
23.4081 4.83819
### 別解 ###
$ cat a | tr ' ' '\t' | datamash svar 4 sstdev 4
23.408106598555	4.8381924929207
```

[（戻る）](/?page=robot_and_stats_questions#大量データのばらつき)

### 不偏分散の定義

\\(\sigma^2\\)を不偏分散とすると、

$$\sigma^2 = \frac{1}{N-1}\sum_{i=1}^N (x_i - \bar{x})^2$$

となります。ここで

$$\bar{x} = \frac{1}{N}\sum_{i=1}^N x_i $$

です。

[（戻る）](/?page=robot_and_stats_questions#不偏分散の定義)

### 代表値の活用

例です．（問題にも書きましたが代表値は万能ではないので，必ず異議が生じることを考慮する必要があります．）

* 平均値が計算できると，何人かのテスト結果を比較して1人選抜しなければならない場合，欠席等でテストを受けた回数が違っても，互いの成績を比較することができる．

[（戻る）](/?page=robot_and_stats_questions#代表値の活用)


## 2章

### 同時確率と条件付き確率

\begin{align}
P(偶数) &= \sum_{X=A,B} P(偶数, X) \\\\
&= \sum_{X=A,B} P(偶数| X)P(X)  \\\\
&= P(偶数| A)P(A) + P(偶数| B)P(B) \\\\ 
&= 1/2 \cdot 2/3 + 1/3 \cdot 1/3 \\\\ 
&= 1/3 + 1/9 \\\\ 
&= 4/9 
\end{align}

[（戻る）](/?page=robot_and_stats_questions#同時確率と条件付き確率)

### 条件つきの乗法定理

\\(X,Y\\)をまとめて\\(P(X, Y, Z)\\)に乗法定理を適用すると、
$$P(X, Y, Z) = P(X, Y | Z)P(Z) ・・・(1)$$
が得られる。また、\\(X,Z\\)をまとめて\\(P(X, Y, Z)\\)に乗法定理を適用すると、
\begin{align}
P(X, Y, Z) &= P(Y | X, Z)P(X, Z) \\\\
&= P(Y|X,Z)P(X|Z)P(Z) ・・・(2)
\end{align}
が得られる。

(1)と(2)の右辺をイコールでつなぐと、
$$P(X, Y | Z)P(Z) = P(Y|X,Z)P(X|Z)P(Z)$$
となる。\\(P(Z) \neq 0 \\)の場合を考えているので、両辺が\\(P(Z)\\)で割れて、
$$P(X, Y | Z) = P(Y|X,Z)P(X|Z)$$
が得られる。

[（戻る）](/?page=robot_and_stats_questions#条件つきの乗法定理)

### 独立

\begin{align}
&\text{Pr} \\{ (x_1 + x_2) \equiv 0 \ (\text{mod} 2) \\} \\\\
&= \sum_{y=0}^1 \text{Pr} \\{ (x_1 + x_2) \equiv 0 \ (\text{mod} 2) \cap x_2  \equiv y \ (\text{mod} 2) \\} \\\\
&= \sum_{y=0}^1 \text{Pr} \\{ (x_1 + x_2) \equiv 0 \ (\text{mod} 2) | x_2  \equiv y \ (\text{mod} 2) \\} \text{Pr} \\{ x_2  \equiv y \ (\text{mod} 2) \\} \\\\
&= \sum_{y=0}^1 \text{Pr} \\{ x_1  \equiv y \ (\text{mod} 2) |  x_2  \equiv y \ (\text{mod} 2) \\} \text{Pr} \\{ x_2  \equiv y \ (\text{mod} 2) \\} \\\\
&= \sum_{y=0}^1 \text{Pr} \\{ x_1  \equiv y \ (\text{mod} 2) \\} \text{Pr} \\{ x_2  \equiv y \ (\text{mod} 2) \\} \qquad (\because x_1 \indep x_2) \\\\
&= \text{Pr} \\{ x_1  \equiv 0 \ (\text{mod} 2) \\} \text{Pr} \\{ x_2  \equiv 0 \ (\text{mod} 2) \\} + \text{Pr} \\{ x_1  \equiv 1 \ (\text{mod} 2) \\} \text{Pr} \\{ x_2  \equiv 1 \ (\text{mod} 2) \\}  \\\\
&= 1/4 + 1/4 = 1/2
\end{align}

[（戻る）](/?page=robot_and_stats_questions#独立)

## 3章


### 賭け事と期待値

\begin{align}
-3700 &+ 1000\cdot(1/6) + 1000\cdot(2/6) + 1000\cdot(3/6) \\\\
&+ 1000\cdot(4/6) + 1000\cdot(5/6) + 1000\cdot(6/6) \\\\
= -3700 &+ 1000\cdot 3.5 = -200円
\end{align}

[（戻る）](/?page=robot_and_stats_questions#賭け事と期待値)


### 期待値の式

\begin{align}
&-a + bP(1) + bP(2) + \dots + bP(6)  \\\\
=& - a + \sum_{i=1}^6 bP(i) \\\\ 
=& - a + b\sum_{i=1}^6 P(i)
\end{align}

[（戻る）](/?page=robot_and_stats_questions#期待値の式)

### 期待値の線形性

\begin{align}
\langle f \rangle_p &= \langle ax + b \rangle_{p(x)} \\\\
&= a \langle x  \rangle_{p(x)} + b \quad (\because \text{期待値の線型性}) \\\\ 
&= a \mu + b \quad (\because \mu = \langle x \rangle_{p(x)}) 
\end{align}

[（戻る）](/?page=robot_and_stats_questions#期待値の線形性)

### 分散の性質と期待値

\begin{eqnarray}
\sigma^2 &=& \langle (x - \mu)^2 \rangle_{p(x)} \\\\
&=& \langle x^2 -2 x\mu -\mu^2 \rangle_{p(x)} \\\\
&=& \langle x^2 \rangle_{p(x)} -2\mu\langle x \rangle_{p(x)} + \mu^2 \\\\
&=& \langle x^2 \rangle_{p(x)} -2\mu^2 + \mu^2  \quad (\because \mu = \langle x \rangle_{p(x)}) \\\\
&=& \langle x^2 \rangle_{p(x)} - \mu^2
\end{eqnarray}

[（戻る）](/?page=robot_and_stats_questions#分散の性質と期待値)

### 独立した変数の和の分散

\\(\mu_x, \mu_y\\)を、それぞれ\\(x,y\\)の平均値とすると、

\begin{eqnarray}
\langle z^2 - \mu_z \rangle_{p(z)} &= \langle x + y - \mu_x - \mu_y \rangle_{p(x,y)} \\\\ 
\langle z \rangle_{p(z)} &= \langle (x-\mu_x)^2 + (y-\mu_y)^2 + 2(x-\mu_x)(y-\mu_y) \rangle_{p(x,y)} \\\\ 
&=
\end{eqnarray}

[（答え）](/?page=robot_and_stats_questions#独立した変数の和の分散)


## 4章

### ガウス分布の式

$$p(x | \mu, \sigma^2 ) = \frac{1}{\sqrt{2\pi\sigma^2}} e^{ - \frac{(x - \mu)^2}{2\sigma^2}}$$

となります。ここで\\(\mu\\)は\\(x\\)の平均値、\\(\sigma^2\\)は分散です。

[（戻る）](/?page=robot_and_stats_questions#ガウス分布の式)

### 連続値と確率

* 例（ちょっとごまかしがあるかもしれませんが）

　\\(x\\)が連続的な値をとるとき、確率は「発生する\\(x\\)の値のうち，\\(x\\)がある範囲に入る割合」として定義される．1つの任意の\\(x\\)の値に対してこの範囲を狭めていくと確率は0に近づいていく．一方で，\\(p\\)の数値はとり得る任意の\\(x\\)に対しては0より大きい固定値で，0には近づかない．したがって\\(p\\)から得られる値は確率ではない．

[（戻る）](/?page=robot_and_stats_questions#連続値と確率)
