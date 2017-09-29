---
Keywords: コマンド,dayslash,Haskell,open,寝る,コードが汚い,眠い
Copyright: (C) 2017 Ryuichi Ueda
---

# Haskell版dayslash作った
前回に引き続きOpen usp Tukubaiネタ．dayslash.hsを作りました．日付けをフォーマットしたり，逆に取り除いたりするコマンドです．

コードが汚い・・・

<a href="https://github.com/usp-engineers-community/Open-usp-Tukubai/blob/master/COMMANDS.HS/dayslash.hs" target="_blank">https://github.com/usp-engineers-community/Open-usp-Tukubai/blob/master/COMMANDS.HS/dayslash.hs</a>

コードは汚いけど，便利なんです．

```bash
uedamac:COMMANDS.HS ueda$ ghc dayslash.hs 
[1 of 1] Compiling Main ( dayslash.hs, dayslash.o )
Linking dayslash ...
uedamac:COMMANDS.HS ueda$ echo 20130101 | ./dayslash "yyyy/mm/dd" 1
2013/01/01
uedamac:COMMANDS.HS ueda$ echo 20130101 | ./dayslash "yyyy/m/d" 1
2013/1/1
uedamac:COMMANDS.HS ueda$ echo "10時12分14秒" | ./dayslash -r "H時M分S秒" 1
101214
uedamac:COMMANDS.HS ueda$ echo 1970/12/20:12:34:50 | ./dayslash -r "yyyy/mm/dd/HH/MM/SS" 1
19701220123450
```


寝る！
