# Haskell版dayslash作った
前回に引き続きOpen usp Tukubaiネタ．dayslash.hsを作りました．日付けをフォーマットしたり，逆に取り除いたりするコマンドです．<br />
<br />
コードが汚い・・・<br />
<br />
<a href="https://github.com/usp-engineers-community/Open-usp-Tukubai/blob/master/COMMANDS.HS/dayslash.hs" target="_blank">https://github.com/usp-engineers-community/Open-usp-Tukubai/blob/master/COMMANDS.HS/dayslash.hs</a><br />
<br />
コードは汚いけど，便利なんです．<br />
<br />
[bash]<br />
uedamac:COMMANDS.HS ueda$ ghc dayslash.hs <br />
[1 of 1] Compiling Main ( dayslash.hs, dayslash.o )<br />
Linking dayslash ...<br />
uedamac:COMMANDS.HS ueda$ echo 20130101 | ./dayslash &quot;yyyy/mm/dd&quot; 1<br />
2013/01/01<br />
uedamac:COMMANDS.HS ueda$ echo 20130101 | ./dayslash &quot;yyyy/m/d&quot; 1<br />
2013/1/1<br />
uedamac:COMMANDS.HS ueda$ echo &quot;10時12分14秒&quot; | ./dayslash -r &quot;H時M分S秒&quot; 1<br />
101214<br />
uedamac:COMMANDS.HS ueda$ echo 1970/12/20:12:34:50 | ./dayslash -r &quot;yyyy/mm/dd/HH/MM/SS&quot; 1<br />
19701220123450<br />
[/bash]<br />
<br />
<br />
寝る！
