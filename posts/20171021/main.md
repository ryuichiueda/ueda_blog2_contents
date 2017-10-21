---
Keywords: 寝る,頭の中だだ漏らし,日記
Copyright: (C) 2017 Ryuichi Ueda
---

# 雑記（2017年10月21日）

### MathJaxでこのサイトに数式を出したい

この[サイト](http://docs.mathjax.org/en/latest/start.html#tex-and-latex-input)の、次のコードをHTMLのhead要素に書くだけ。あと、ドルマーク二つで式を囲むだけ。超簡単。

```html
<script type="text/javascript" async src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.2/MathJax.js?config=TeX-MML-AM_CHTML"></script>
```

$$ P(A|B) = \dfrac{P(B|A)P(A)}{P(B)} = \dfrac{P(B|A)P(A)}{\sum_{A' \in \mathcal{A}} P(B|A')P(A')} $$


出た。


寝る。
