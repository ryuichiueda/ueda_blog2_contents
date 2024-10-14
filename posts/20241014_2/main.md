---
Keywords: ロボットの確率・統計
Copyright: (C) 2024 Ryuichi Ueda
---

# 不偏分散で二乗誤差の和ををNでなくN-1で割る理由の証明の別解（書きかけ）

　「分散はNでなくてN-1で割れ」と統計の授業とか研究室とかで言われた人は多いと思いますが、その証明となると結構ややこしいです。

　証明については[「高校数学の美しい物語」](https://manabitimes.jp/math/1035)にあり、「[ロボットの確率・統計](https://amzn.to/4eYBEk4)」でも同様のものを書きました。

　ただ、この証明方法だと証明の解釈が難しいので、もうひとつ別解を考えてみましたのでメモしておきます。

## 分布と標本の定義


　まず、ある分布\\(p\\)を考えます。この分布の平均（母平均）\\(\mu\\)と分散（母分散）\\(\sigma^2\\)は、\\(p\\)にしたがう変数\\(x\\)を使って、

\begin{align}
\mu &= \langle x \rangle_{p(x)}\text{・・・(1)} \\\\
\sigma^2 &= \langle (x - \mu)^2 \rangle_{p(x)}\text{・・・(2)} 
\end{align}

で定義できます。ここで\\(\langle f(x) \rangle_{p(x)}\\)は、\\(x\\)が分布\\(p\\)にしたがうときの関数\\(f\\)の期待値です。


　また、分布\\(p\\)から独立同分布でサンプリングされた標本

$$x_{1:N} = \\{ x_i | i=1,2,\dots,N \\}$$

を考えましょう。この標本の平均値は

\begin{align}
\bar{x} &= \dfrac{1}{N}\sum_{i=1}^N x_i \text{・・・(3)}
\end{align}
となります。

## 問題

不偏分散

$$s^2 = \dfrac{1}{N-1}\sum_{i=1}^N ( x_i - \bar{x} )^2$$

を考えます。不偏分散の期待値が、母分散と一致することを証明してください。これが証明できると、標本から分布の分散を求めようとすれば、分母に\\(N-1\\)を使う不偏分散を使うべきだということになります。


## 解きますよ

### 様々な分散の関係

　(2)の分散の定義は、\\(x\\)を何度も（無限に）選んで\\(\mu\\)との差の2乗の平均（期待値）を計算すると分散となる、というものですが、\\(x\\)を選ぶ個数を\\(N\\)個に制限すると、その値は\\(\sigma^2\\)を期待値としてばらつきます。


　仮に\\(\mu\\)が分かっているとして、標本の分散を母平均\\(\mu\\)を使って計算すると、その値は

\begin{align}
\sigma_x^2 &= \dfrac{1}{N}\sum_{i=1}^N (x_i - \mu)^2
\end{align}

となります。

また、標本を何回も取り直して\\(\sigma_x^2\\)の平均値をとると、それは母分散と一致するので、

\begin{align}
\langle \sigma_x^2 \rangle_{p(x)} &= \sigma^2 \text{・・・(5)}
\end{align}

となります。

　さらに、[この記事](/?post=20241014)から、\\(\bar{x}\\)の分散は、

$$\sigma_{\bar{x}}^2 = \dfrac{1}{N} \sigma^2\text{・・・(6)}$$

が得られます。（[この記事](/?post=20241014)の\\(\sigma_N^2\\)が式(6)の\\(\sigma_{\bar{x}}^2\\)に相当します。）



そして、(3)について、

\begin{align}
\bar{x} &= \dfrac{1}{N}\sum_{i=1}^N x_i = \dfrac{1}{N}\sum_{i=1}^N \bar{x}
\end{align}

つまり
\begin{align}
\sum_{i=1}^N x_i = \sum_{i=1}^N \bar{x} \text{・・・(6)}
\end{align}

となります。

## 標本の平均値のばらつき


## 変形


$$\dfrac{1}{N-1}\sum_{i=1}^N ( x_i - \bar{x} )^2 - \dfrac{1}{N}\sum_{i=1}^N (x_i - \mu )^2$$
$$=\dfrac{1}{N(N-1)}\sum_{i=1}^N \left\\{ N(x_i^2 -2x_i\bar{x} + \bar{x}^2) - (N-1)(x_i^2 -2x_i\mu + \mu^2) \right\\}$$
$$=\dfrac{1}{N(N-1)}\sum_{i=1}^N \left\\{ x_i^2 -2N x_i\bar{x} + N\bar{x}^2 + 2(N-1)x_i\mu - (N-1)\mu^2\right\\}$$
$$=\dfrac{1}{N(N-1)}\sum_{i=1}^N \left\\{ x_i^2 -2N \bar{x}^2 + N\bar{x}^2 + 2(N-1)\bar{x}\mu - (N-1)\mu^2\right\\}$$
$$=\dfrac{1}{N(N-1)}\sum_{i=1}^N \left\\{ x_i^2 -N \bar{x}^2 + 2(N-1)\bar{x}\mu - (N-1)\mu^2\right\\}$$
$$=\dfrac{1}{N(N-1)}\sum_{i=1}^N \left\\{ x_i^2 - 2\bar{x}\mu + \mu^2 - N\bar{x}^2 + 2N\bar{x}\mu - N \mu^2 \right\\}$$
$$=\dfrac{1}{N(N-1)}\sum_{i=1}^N \left\\{ x_i^2 - 2x_i\mu + \mu^2 - N\bar{x}^2 + 2N\bar{x}\mu - N \mu^2 \right\\}$$
$$=\dfrac{1}{N(N-1)}\sum_{i=1}^N  (x_i - \mu )^2 - \dfrac{1}{N-1}\sum_{i=1}^N  (\bar{x} - \mu )^2$$
$$=\dfrac{\sigma_x^2}{N-1} - \dfrac{N}{N-1}(\bar{x} - \mu )^2$$
>>>>>>> 45f2f7b81b95482cd1d8eaa7aad84d54e4284dc7



