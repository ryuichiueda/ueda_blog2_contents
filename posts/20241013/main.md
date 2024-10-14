---
Keywords: ロボットの確率・統計
Copyright: (C) 2024 Ryuichi Ueda
---

# 不偏分散で二乗誤差の和ををNでなくN-1で割る理由の証明の別解（書きかけ）

　「分散はNでなくてN-1で割れ」と統計の授業とか研究室とかで言われた人は多いと思いますが、その証明となると結構ややこしいです。

　証明については[「高校数学の美しい物語」](https://manabitimes.jp/math/1035)にあり、「[ロボットの確率・統計](https://amzn.to/4eYBEk4)」でも同様のものを書きました。

　ただ、この証明方法だと証明の解釈が難しいので、もうひとつ別解を考えてみましたのでメモしておきます。

## 分布の定義

　まず、ある分布\\(p\\)を考えます。この分布の平均（母平均）\\(\mu\\)と分散（母分散）\\(\sigma\\)は、\\(p\\)にしたがう変数\\(x\\)を使って、

\begin{align}
\mu &= \langle x \rangle_{p(x)}\text{・・・(1)} \\\\
\sigma &= \langle (x - \mu)^2 \rangle_{p(x)}\text{・・・(2)} 
\end{align}

で定義できます。


## \\(\alpha_N\\)の定義


　まず、分布の平均値が\\(\mu\\)のある分布\\(p\\)から独立同分布でサンプリングされた標本

$$x_{1:N} = \\{ x_i | i=1,2,\dots,N \\}$$

を考えます。この標本から、

$$\alpha_N = \left\langle (x_1 + x_2 + \dots + x_N - N \mu )^2 \right\rangle_{p(x)}\text{・・・(1)}$$
 
という数を考えます。ここで\\(\langle f \rangle_{p(x)}\\)は、\\(x\\)が分布\\(p\\)にしたがうときの\\(f\\)の期待値です。式(1)の場合、\\(x_1, x_2, x_N\\)はそれぞれ分布\\(p\\)にしたがっていることになります。

## 式(1)の変形


$$\dfrac{1}{M-1}\sum_{i=1}^M ( x_i - \bar{x} )^2 - \dfrac{1}{M}\sum_{i=1}^M (x_i - \mu )^2$$
$$=\dfrac{1}{M(M-1)}\sum_{i=1}^M \left\\{ M(x_i^2 -2x_i\bar{x} + \bar{x}^2) - (M-1)(x_i^2 -2x_i\mu + \mu^2) \right\\}$$
$$=\dfrac{1}{M(M-1)}\sum_{i=1}^M \left\\{ x_i^2 -2M x_i\bar{x} + M\bar{x}^2 + 2(M-1)x_i\mu - (M-1)\mu^2\right\\}$$
$$=\dfrac{1}{M(M-1)}\sum_{i=1}^M \left\\{ x_i^2 -2M \bar{x}^2 + M\bar{x}^2 + 2(M-1)\bar{x}\mu - (M-1)\mu^2\right\\}$$
$$=\dfrac{1}{M(M-1)}\sum_{i=1}^M \left\\{ x_i^2 -M \bar{x}^2 + 2(M-1)\bar{x}\mu - (M-1)\mu^2\right\\}$$
$$=\dfrac{1}{M(M-1)}\sum_{i=1}^M \left\\{ x_i^2 + 2\bar{x}\mu - \mu^2 - M\bar{x}^2 + 2M\bar{x}\mu - M \mu^2 \right\\}$$

## 式(1)の変形

　次に(1)を変形していきます。

\begin{align}
\alpha_N &= \left\langle (x_1 + x_2 + \dots + x_N - N \mu )^2 \right\rangle_{p(x)} \\\\
&= \left\langle \left\\{ \left(x_1 + x_2 + \dots + x_{N-1} - [N-1]\mu \right) + (x_N - \mu ) \right\\}^2 \right\rangle_{p(x)}\\\\
&= \left\langle  \left(x_1 + x_2 + \dots + x_{N-1} - [N-1]\mu \right)^2 \right\rangle_{p(x)} \\\\
&\quad+ 2\left\langle \left(x_1 + x_2 + \dots + x_{N-1} - [N-1]\mu \right)(x_N - \mu ) \right\rangle_{p(x)} \\\\
&\quad+ \left\langle (x_N - \mu )^2 \right\rangle_{p(x)}
\end{align}

このように3つの期待値に分解できますが、ひとつめの期待値は(1)から\\(\alpha_{N-1}\\)となります。また、ふたつめの期待値は、\\(x_1 + x_2 + \dots + x_{N-1}\\)と\\(x_N\\)の共分散になりますが、\\(x_N\\)と、他の\\(x_i \ (i=1,2,\dots,N-1)\\)は独立なので、これは0になります。みっつめの期待値は、\\(x_N\\)が\\(p(x)\\)から選ばれる値なので、これは分散\\(\sigma^2\\)になります。

　ということで、

$$ \alpha_N = \alpha_{N-1} + \sigma^2\text{・・・(2)}$$

が成り立ちます。

