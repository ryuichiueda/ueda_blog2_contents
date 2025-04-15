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

### 確率の雑多な問題1

各サイコロの目を$a, b, c$とおきましょう。加法定理より

\begin{align}
$$\text{Pr} ( a=b \text{or} b=c \text{or} c=a ) + \text{Pr} ( a=b \text{or} b=c \text{or} c=a ) = 1$$
\begin{end}

$$\text{Pr} \{ a=b \text{ or } b=c \text{ or } c=a \}$$
$$=1 - \text{Pr} \{ a \neq b \text{ and } b \neq c \text{ and } c \neq a \}$$
$$=1 - \text{Pr} \{ b \neq c \text{ and } c \neq a | a \neq b \}\text{Pr}(a \neq b)$$
$$=1 - 4/6 \cdot 5/6$$
$$= 16/36 = 4/9$$



[（戻る）](/?page=robot_and_stats_questions#確率の雑多な問題1)

## 3章


### 賭け事と期待値

\begin{align}
-3700 &+ 1000\cdot(1/6) + 1000\cdot(2/6) + 1000\cdot(3/6) \\\\
&+ 1000\cdot(4/6) + 1000\cdot(5/6) + 1000\cdot(6/6) \\\\
= -3700 &+ 1000\cdot 3.5 = -200円
\end{align}

[（戻る）](/?page=robot_and_stats_questions#賭け事と期待値)

### 賭け事と期待値2

コインの表が出る確率が1/2とすると、儲けの期待値は、
\begin{align}
-100 + 100,000,000 (1/2)^{100} = -100 + \dfrac{1000^2 \cdot 100}{1024^{10}} \approx -100 + \dfrac{100}{1024^8}
\end{align}
となります。つまり、期待値で考えると、ほぼ見返りがないということになります。$100$円払って夢を見るにしても、もう少し金額が大きいか、コインの枚数が少なくなければなりません。


[（戻る）](/?page=robot_and_stats_questions#賭け事と期待値2)

### 宝くじ

法令で「その発売総額の五割に相当する額（加算型当せん金付証票にあつては、その額に加算金（第2条第2項の加算金をいう。以下同じ。）の額を加えた額）をこえてはならない。」とあるので、加算金（いわゆるキャリーオーバー）がない場合は1万円宝くじを購入して得られる金額の期待値は5000円を超えません。

それでも買うかどうかや、宝くじの存在意義についての議論についてはおまかせします。

[（戻る）](/?page=robot_and_stats_questions#宝くじ)

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

　\\(\mu_x, \mu_y\\)を、それぞれ\\(x,y\\)の平均値、
\\(\sigma_x^2, \mu_y^2\\)を、それぞれ\\(x,y\\)の分散とすると、
* \\(\sigma_x^2 = \langle (x-\mu_x)^2 \rangle_{p(x)}\\)
* \\(\sigma_y^2 = \langle (y-\mu_y)^2 \rangle_{p(y)}\\)

となります。

　また、\\(x \indep y\\)なので、
* \\(p(x,y) = p(x)p(y)\\)
* \\(\langle (x-\mu_x)(y-\mu_y) \rangle_{p(x,y)} = 0\\)

が成り立ちます。


　したがって、
\begin{align}
\langle (z - \mu_z)^2 \rangle_{p(z)} &= \langle (x + y - \mu_x - \mu_y)^2 \rangle_{p(x,y)} \\\\ 
&= \langle (x-\mu_x)^2 + (y-\mu_y)^2 + 2(x-\mu_x)(y-\mu_y) \rangle_{p(x,y)} \\\\ 
&= \langle (x-\mu_x)^2 \rangle_{p(x,y)} + \langle (y-\mu_y)^2 \rangle_{p(x,y)} + \langle 2(x-\mu_x)(y-\mu_y) \rangle_{p(x,y)} \\\\ 
&= \langle (x-\mu_x)^2 \rangle_{p(x)p(y)} + \langle (y-\mu_y)^2 \rangle_{p(x)p(y)} + \langle 2(x-\mu_x)(y-\mu_y) \rangle_{p(x,y)} \\\\ 
&= \langle (x-\mu_x)^2 \rangle_{p(x)} + \langle (y-\mu_y)^2 \rangle_{p(y)} + 0 \\\\
&= \sigma_x^2 + \sigma_y^2 
\end{align}
となります。つまり、\\(z\\)の分散は、\\(x,y\\)それぞれの分散の和になります。

[（戻る）](/?page=robot_and_stats_questions#独立した変数の和の分散)


### 2つのサイコロの目の分散

2つのサイコロの目は、1方が1方に影響を与えることなく独立である。したがって、1つのサイコロの出目の分散を\\(\sigma^2\\)と表すと、小問1, 2は次のように解ける。

* 小問1: 目の和の分散

\\(\sigma^2\\)を単純に2つ足したものとなり、

$$2\sigma^2 = 35/12 \cdot 2 = 35/6$$

となる。

* 小問2: 目の平均値の分散

2つのサイコロの出目を\\(x_1,x_2\\)とする。出目の平均値は

$$\bar{x} = (x_1 + x_2)/2 = x_1/2 + x_2/2$$

となり、\\(x_1/2 \indep x_2/2\\)なので、\\(\bar{x}\\)の分散は、\\(x_1/2, x_2/2\\)の分散の和、すなわち、サイコロ1つの出目を2で割った値の分散の和となる。サイコロ1つの出目\\(x\\)を2で割った値の分散は、サイコロの出目の確率分布を\\(P\\)と表記すると、

\begin{align}
\langle (x/2 - 3.5/2)^2 \rangle_P = \dfrac{1}{4}\langle (x - 3.5)^2 \rangle_P = \dfrac{1}{4}\sigma^2
\end{align}

と、\\(\sigma^2\\)の1/4となる。したがって、求める値は、

$$2\sigma^2/4 = 35/24$$

となる。

[（戻る）](/?page=robot_and_stats_questions#2つのサイコロの目の分散)


## 4章

### ガウス分布の式

$$p(x | \mu, \sigma^2 ) = \frac{1}{\sqrt{2\pi\sigma^2}} e^{ - \frac{(x - \mu)^2}{2\sigma^2}}$$

となります。ここで\\(\mu\\)は\\(x\\)の平均値、\\(\sigma^2\\)は分散です。

[（戻る）](/?page=robot_and_stats_questions#ガウス分布の式)

### 2次元ガウス分布の式

$$p(\boldsymbol{x} | \boldsymbol{\mu}, \Sigma ) = \dfrac{1}{\sqrt{(2\pi)^2|\Sigma|}} \exp \left\\{ - \dfrac{1}{2} {(\boldsymbol{x} - \boldsymbol{\mu}})^\top \Sigma^{-1}(\boldsymbol{x} - \boldsymbol{\mu}) \right\\}$$

ここで

\begin{align}
\boldsymbol{\mu} &= \begin{pmatrix} \mu_1 \\\\ \mu_2 \end{pmatrix}\\\\
\Sigma &= \begin{pmatrix} \sigma_1^2 & \sigma_{12} \\\\ \sigma_{12} & \sigma_2^2 \end{pmatrix}
\end{align}

であり、\\(\mu_1, \mu_2\\)はそれぞれ\\(x_1, x_2\\)の平均値、\\(\sigma_1^2, \sigma_2^2 \\)はそれぞれ\\(x_1, x_2\\)の分散である。また、\\(\sigma_{12}\\)は\\(x_1, x_2\\)の共分散である。

[（戻る）](/?page=robot_and_stats_questions#2次元ガウス分布の式)

### 連続値と確率

* 例（ちょっとごまかしがあるかもしれませんが）

　\\(x\\)が連続的な値をとるとき、確率は「発生する\\(x\\)の値のうち，\\(x\\)がある範囲に入る割合」として定義される．1つの任意の\\(x\\)の値に対してこの範囲を狭めていくと確率は0に近づいていく．一方で，\\(p\\)の数値はとり得る任意の\\(x\\)に対しては0より大きい固定値で，0には近づかない．したがって\\(p\\)から得られる値は確率ではない．

[（戻る）](/?page=robot_and_stats_questions#連続値と確率)


### ガウス分布に従う2変数の和の分布

$$\mathcal{N}(\boldsymbol{\mu}_1 + \boldsymbol{\mu}_2, \Sigma_1 + \Sigma_2)$$になります。

[（戻る）](/?page=robot_and_stats_questions#ガウス分布に従う2変数の和の分布)

### ガウス分布の積

$$\mathcal{N}\left[ (\Lambda_1 + \Lambda_2)^{-1}(\Lambda_1 \boldsymbol{\mu}_1 + \Lambda_2 \boldsymbol{\mu}_2), (\Lambda_1 + \Lambda_2)^{-1} \right]$$

となります。ただし、\\(\Lambda_n \ (n=1,2) \\)は\\(\Sigma_n\\)の逆行列（精度行列）です。


[（戻る）](/?page=robot_and_stats_questions#ガウス分布の積)

## 5章

### ベイズの定理の導出

　\\(P(X,Y)\\)について、乗法定理より、

\begin{align}
P(X,Y) &= P(X|Y)P(Y) \text{・・・(1)}\\\\
P(X,Y) &= P(Y|X)P(X) \text{・・・(2)}
\end{align}

となる。(1)、(2)の右辺より、\\(P(Y) \neq 0\\)ならば、

\begin{align}
P(X|Y)P(Y) &= P(Y|X)P(X)\\\\
P(X|Y) &= \dfrac{P(Y|X)P(X)}{P(Y)}\text{・・・(3)}
\end{align}
となり、(3)がベイズの定理の式となる。


[（答え）](/?page=robot_and_stats_questions#ベイズの定理の導出)


### ベイズの定理からの推定

　[Pythonでのコードの例](/pages/robot_and_stats_questions/coin.py)を示します。（表示の関係でインデントがずれているかもしれません。）

```python3
#!/usr/bin/python3

import sys

prob_a = 0.5     #Aである確率（初期値1/2）

A_TOP = 0.5      #Aを投げたら表が出る確率
A_BACK = 0.5     #Aを投げたら裏が出る確率
B_TOP = 1.0/3    #Bを投げたら表が出る確率
B_BACK = 2.0/3   #Bを投げたら裏が出る確率

for c in sys.stdin:
    c = c.strip()
    if c == "表":   #↓ベイズの定理（P(A|表) = P(表|A)*P(A)/(P(表|A)P(A)+P(表|B)P(B)) ）
        prob_a = A_TOP*prob_a/(A_TOP*prob_a + B_TOP*(1.0 - prob_a))
    if c == "裏":   #↓ベイズの定理（P(A|裏) = P(裏|A)*P(A)/(P(裏|A)P(A)+P(裏|B)P(B)) ）
        prob_a = A_BACK*prob_a/(A_BACK*prob_a + B_BACK*(1.0 - prob_a))

print(prob_a)
```

実行するとこうなります。

```bash
$ cat coin.txt | tr ' ' \\n | ./coin.py
0.0027473967158593666
```

したがって、Aである確率は0.27%ということになります。投げたのはBである確率が極めて高いのですが、Aである可能性も1000に2, 3はあるということになります。

　なお、10回ごとにAである確率を記録していくと、

```bash
$ seq 10 | while read i ;do head -$i coin.txt | tr ' ' \\n | ./coin.py ;done
0.3105864160192721
0.0921295840646165
0.022347673087940438
0.03956213821246428
0.035786268196507195
0.03235863131847253
0.02924933718877189
0.006741295095506945
0.006078072096803084
0.0027473967158593666
```

となり、Aである確率がだんだん下がっていくことが分かります。

[（答え）](/?page=robot_and_stats_questions#ベイズの定理からの推定)
