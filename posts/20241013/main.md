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

で定義できます。ここで\\(\langle f(x) \rangle_{p(x)}\\)は、\\(x\\)が分布\\(p\\)にしたがうときの関数\\(f\\)の期待値です。

## 標本


　分布\\(p\\)から独立同分布でサンプリングされた標本

$$x_{1:N} = \\{ x_i | i=1,2,\dots,N \\}$$

この標本の平均と分散を母平均\\(\mu\\)を使って考えると、

\begin{align}
\bar{x} &= \dfrac{1}{N}\sum_{i=1}^N x_i \text{・・・(3)} \\\\
\sigma_x^2 &= \dfrac{1}{N}\sum_{i=1}^N (x_i - \mu)^2 \text{・・・(4)}
\end{align}


となります。また、標本を何回も取り直して\\(\sigma_x^2\\)の平均値をとると、それは母分散と一致するので、

\begin{align}
\langle \sigma_x^2 \rangle &= \sigma^2 \text{・・・(5)}
\end{align}

となります。

## 式(1)の変形


$$\dfrac{1}{M-1}\sum_{i=1}^M ( x_i - \bar{x} )^2 - \dfrac{1}{M}\sum_{i=1}^M (x_i - \mu )^2$$
$$=\dfrac{1}{M(M-1)}\sum_{i=1}^M \left\\{ M(x_i^2 -2x_i\bar{x} + \bar{x}^2) - (M-1)(x_i^2 -2x_i\mu + \mu^2) \right\\}$$
$$=\dfrac{1}{M(M-1)}\sum_{i=1}^M \left\\{ x_i^2 -2M x_i\bar{x} + M\bar{x}^2 + 2(M-1)x_i\mu - (M-1)\mu^2\right\\}$$
$$=\dfrac{1}{M(M-1)}\sum_{i=1}^M \left\\{ x_i^2 -2M \bar{x}^2 + M\bar{x}^2 + 2(M-1)\bar{x}\mu - (M-1)\mu^2\right\\}$$
$$=\dfrac{1}{M(M-1)}\sum_{i=1}^M \left\\{ x_i^2 -M \bar{x}^2 + 2(M-1)\bar{x}\mu - (M-1)\mu^2\right\\}$$
$$=\dfrac{1}{M(M-1)}\sum_{i=1}^M \left\\{ x_i^2 - 2\bar{x}\mu + \mu^2 - M\bar{x}^2 + 2M\bar{x}\mu - M \mu^2 \right\\}$$
$$=\dfrac{1}{M(M-1)}\sum_{i=1}^M \left\\{ x_i^2 - 2x_i\mu + \mu^2 - M\bar{x}^2 + 2M\bar{x}\mu - M \mu^2 \right\\}$$
$$=\dfrac{1}{M(M-1)}\sum_{i=1}^M  (x_i - \mu )^2 - \dfrac{1}{M-1}\sum_{i=1}^M  (\bar{x} - \mu )^2$$



