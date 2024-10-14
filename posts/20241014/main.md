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


　分散の式は、


$$\sigma_N^2 = \left\langle (\overline{x_N} - \mu )^2 \right\rangle_{p(x)}$$

となります。

## 解き方

\\(N\\)を1つ増やして、

$$\sigma_{N+1}^2 = \left\langle (\overline{x_{N+1}} - \mu )^2 \right\rangle_{p(x)}$$

を変形していきましょう。


\begin{align}
\sigma_{N+1}^2 &= \left\langle (\overline{x_{N+1}} - \mu )^2 \right\rangle_{p(x)}\\\\
&= 
\end{align}

