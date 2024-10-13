---
Keywords: ロボットの確率・統計
Copyright: (C) 2024 Ryuichi Ueda
---

# 不偏分散で二乗誤差の和ををNでなくN-1で割る理由の証明の別解（書きかけ）

　「分散はNでなくてN-1で割れ」と統計の授業とか研究室とかで言われた人は多いと思いますが、その証明となると結構ややこしいです。

　証明については[「高校数学の美しい物語」](https://manabitimes.jp/math/1035)にあり、「[ロボットの確率・統計](https://amzn.to/4eYBEk4)」でも同様のものを書きました。

　ただ、この証明方法だと証明の解釈が難しいので、もうひとつ別解を考えてみましたのでメモしておきます。

## \\(\delta_N\\)の定義


　まず、分布の平均値が\\(\mu\\)のある分布\\(p\\)から独立同分布でサンプリングされた標本

$$x_{1:N} = \\{ x_i | i=1,2,\dots,N \\}$$

を考えます。この標本から、

$$\delta_N = \left\langle (x_1 + x_2 + \dots + x_N - N \mu )^2 \right\rangle_{p(x)}\text{・・・(1)}$$
 
という数を考えます。ここで\\(\langle f \rangle_{p(x)}\\)は、\\(x\\)が分布\\(p\\)にしたがうときの\\(f\\)の期待値です。式(1)の場合、\\(x_1, x_2, x_N\\)はそれぞれ分布\\(p\\)にしたがっていることになります。

## 式(1)の変形

　次に(1)を変形していきます。

\begin{align}
\delta_N &= \left\langle (x_1 + x_2 + \dots + x_N - N \mu )^2 \right\rangle_{p(x)} \\\\
&= \left\langle (x_1 + x_2 + \dots + x_N - N \mu )^2 \right\rangle_{p(x)} 
\end{align}
&= \left\langle \left\{ (x_1 + x_2 + \dots + x_{N-1} - [N-1]\mu) + (x_N - \mu ) \}^2 \right\rangle_{p(x)}

