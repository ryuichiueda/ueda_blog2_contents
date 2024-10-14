---
Keywords: ロボットの確率・統計
Copyright: (C) 2024 Ryuichi Ueda
---

# 標本の平均値はどれだけばらつくか（書きかけ）


　「[ロボットの確率・統計](https://amzn.to/4eYBEk4)」で扱わなかった話題を書いておきます。

## 問題

ある確率分布\\(p\\)から\\(N\\)個データをドローして作った標本

$$x_{1:N} = \\{ x_i | i=1,2,\dots,N \\}$$

の平均値

$$\overline{x_N} = (x_1 + x_2 + \dots + x_N)/N$$


は、\\(p\\)の平均（母平均）\\(\mu\\)からどれだけばらつくでしょうか。分散を求めてみましょう。

## ヒント


　分散の式は、


$$\sigma_N^2 = \left\langle (\overline{x_N} - \mu )^2 \right\rangle_{p(x)}$$

となります。また、\\(p\\)の分散（簿分散）は、

$$\sigma^2 = \left\langle (x - \mu )^2 \right\rangle_{p(x)}$$

## 解き方

\\(N\\)を1つ増やして、

$$\sigma_{N+1}^2 = \left\langle (\overline{x_{N+1}} - \mu )^2 \right\rangle_{p(x)}$$

を変形していきましょう。\\(x_1, x_2, \dots, x_N\\)と\\(x_{N+1}\\)を分けるように変形すると、

\begin{align}
\sigma_{N+1}^2 &= \left\langle (\overline{x_{N+1}} - \mu )^2 \right\rangle_{p(x)}\\\\
&= \dfrac{1}{(N+1)^2} \left\langle \left\\{ x_1 + x_2 + \dots + x_{N+1} - (N+1)\mu \right\\}^2  \right\rangle_{p(x)}\\\\
&= \dfrac{1}{(N+1)^2} \left\langle \left\\{ (x_1 + x_2 + \dots + x_N - N \mu ) + x_{N+1} - \mu \right\\}^2 \right\rangle_{p(x)}\\\\
&= \dfrac{1}{(N+1)^2} \Big\\{ \Big\langle (x_1 + x_2 + \dots + x_N - N \mu )^2 \Big\rangle_{p(x)} \\\\
&+ \Big\langle (x_{N+1} - \mu)^2 \Big\rangle_{p(x)} \\\\
&+ \Big\langle 2(x_1 + x_2 + \dots + x_N - N \mu )(x_{N+1} - \mu) \big\\} \Big\rangle_{p(x)} \Big\\} \\\\
&= \dfrac{1}{(N+1)^2} \Big\\{ N^2 \Big\langle (\overline{x_N} - \mu )^2 \Big\rangle_{p(x)} \\\\
&+ \Big\langle (x_{N+1} - \mu)^2 \Big\rangle_{p(x)} \\\\
&+ 2N \Big\langle (\overline{x_N} -  \mu )(x_{N+1} - \mu) \big\\} \Big\rangle_{p(x)} \Big\\} \\\\
&= 
\end{align}

と、3つの期待値に分解できます。この3つの期待値のうち、

* 最初のもの: \\(\sigma_N^2\\)
* 2番目のもの: \\(x_{N+1}\\)が単に\\(p\\)からドローする変数でしかないので、分散となる

