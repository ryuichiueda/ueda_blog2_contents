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

$$\bar{x}_N = (x_1 + x_2 + \dots + x_N)/N$$


は、\\(p\\)の平均（母平均）\\(\mu\\)からどれだけばらつくでしょうか。分散を求めてみましょう。


## 分散の式


　まず分散の式は、


\begin{align}
\sigma_N^2 &= \left\langle (x_N - \mu )^2 \right\rangle_{p(x)}\text{・・・(1)}
\end{align}



となります。ドローする数をひとつ増やして\\(x_{N+1}\\)を追加すると、

$$\sigma_{N+1}^2 = \left\langle (\bar{x}_{N+1} - \mu )^2 \right\rangle_{p(x)}\text{・・・(1)}$$

となります。