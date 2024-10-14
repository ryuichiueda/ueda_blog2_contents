---
Keywords: ロボットの確率・統計
Copyright: (C) 2024 Ryuichi Ueda
---

# 標本の平均値はどれだけばらつくか


　「[ロボットの確率・統計](https://amzn.to/4eYBEk4)」で扱わなかった話題を書いておきます。

## 問題

ある確率分布\\(p\\)から\\(N\\)個データをドローして作った標本

$$x_{1:N} = \\{ x_i | i=1,2,\dots,N \\}$$

の平均値

$$\overline{x_N} = (x_1 + x_2 + \dots + x_N)/N$$


は、\\(p\\)の平均（母平均）\\(\mu\\)からどれだけばらつくでしょうか。分散を求めてみましょう。\\(p\\)の分散（母分散）は\((\sigma^2\))とします。

## 解答

　互いに独立な変数\\(y_1, y_2,\dots, y_M\\)を足した値\\(y_1 + y_2 +\dots + y_M\\)の分散は、それぞれの変数の分散\\(\sigma_{y_1}^2, \sigma_{y_2}^2, \dots, \sigma_{y_M}^2\\)の和\\(\sigma_{y_1}^2 + \sigma_{y_2}^2 + \dots + \sigma_{y_M}^2\\)の和になる。


　問題については、\\(x_1/N, x_2/N, \dots, x_N/N \\)は互いに独立（\\(p\\)に対して独立同分布）だと暗に仮定されているので、これらの和の分散は、\\(\overline{x_N}\\)の分散と一致する。したがって、計算すべき分散の値は、

\begin{align}
\sum_{i=1}^N \langle (x_i/N - \mu/N)^2 \rangle_p &= \dfrac{1}{N^2} \sum_{i=1}^N \langle (x_i - \mu)^2 \rangle_p  \\\\
&= \dfrac{1}{N^2} N \sigma^2  \\\\
&= \dfrac{1}{N} \sigma^2 
\end{align}

## 別解（長い）

### ヒント


　分散の式は、


$$\sigma_N^2 = \left\langle (\overline{x_N} - \mu )^2 \right\rangle_{p(x)}$$

となります。また、分布\\(p\\)自体の分散（母分散）は、

$$\sigma^2 = \left\langle (x - \mu )^2 \right\rangle_{p(x)}\text{・・・(1)}$$

です。

　また、\\(N=1\\)のとき、\\(\overline{x_N}\\)は\\(x_1\\)に一致するので、


$$\sigma_1^2 = \left\langle (x_1 - \mu )^2 \right\rangle_{p(x)}$$

となりますが、\\(x_1\\)と\\(p(x)\\)の\\(x\\)は同じものなので、

$$\sigma_1^2 = \left\langle (x - \mu )^2 \right\rangle_{p(x)} = \sigma^2\text{・・・(2)}$$

が成り立ちます。

### 解き方

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

と、3つの期待値に分解できます。この3つの期待値は、

* 最初のもの: \\(\sigma_N^2\\)
* 2番目のもの: \\(x_{N+1}\\)が単に\\(p\\)からドローされた変数でしかないので、(1)の式と同じ。つまり母分散になる。
* 3番目のもの: \\(\overline{x_N}\\)と\\(x_{N+1}\\)の共分散になりますが、\\(x_{N+1}\\)は\\(x_1, x_2, \dots, x_N\\)からはなにも影響を受けず独立なので、0になる。


したがって、
$$\sigma_{N+1}^2 = \dfrac{N^2}{(N+1)^2} \sigma_N^2  + \dfrac{1}{(N+1)^2} \sigma^2$$ 
となります。

\begin{align}
(N+1)^2 \sigma_{N+1}^2 &= N^2 \sigma_N^2  +  \sigma^2 \\\\
&= (N-1)^2 \sigma_{N-1}^2  +  2\sigma^2 \\\\
&= \cdots \\\\
&= 1^2\sigma_1^2  +  N\sigma^2 \\\\
&= 1^2\sigma^2  +  N\sigma^2 \quad (\because (2) )\\\\
&= (N+1)\sigma^2
\end{align}
となり、
$$\sigma_N^2 = \dfrac{1}{N}\sigma^2$$
が得られます。

### というわけで


ある確率分布から\\(N\\)個データをドローして平均値をとると、その平均値は、もともとの確率分布の分散を個数\\(N\\)で割った分散でばらつきます。
