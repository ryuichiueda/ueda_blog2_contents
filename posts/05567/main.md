---
Copyright: (C) Ryuichi Ueda
---

# シェル芸勉強会参加者数
<h2>サマリー</h2><br />
<span style="font-size: 30px;">これまでに世に放たれたシェル芸人数:<br />
のべ1158人</span><br />
<h2>数え方シェル芸</h2><br />
Macの端末（coreutilsインストール済み）とUbuntu 14.04.1 LTSで動作確認済み。<br />
<br />
[bash]<br />
$ curl 'https://blog.ueda.tech/?page_id=5567' 2&gt; /dev/null | sed -n '/&lt;table/,/&lt;\\/table/p' | grep -A 3 '&lt;tr&gt;' | grep -A 2 '&lt;td&gt;[0-9]*回&lt;/td&gt;' | awk 'NR%4==3' | tr -cd '0-9\\n' | numsum<br />
[/bash]<br />
<br />
<h2>各回の参加者数</h2><br />
<table><br />
<tbody><br />
<tr><br />
<th>回</th><br />
<td>年月日</td><br />
<td>人数</td><br />
<td>根拠</td><br />
</tr><br />
<br />
<tr><br />
<td>28回</td><br />
<td>201704</td><br />
<td>50</td><br />
<td>東京(28)会計から、<a href="http://papiro.hatenablog.jp/entry/2017/04/24/002533">福岡</a>(6)(papironさん)、<a href="http://www.kunst1080.net/entry/2017/04/23/162231">大阪</a>（16）（くんすとさん）</td><br />
</tr><br />
<br />
<tr><br />
<td>27回</td><br />
<td>201702</td><br />
<td>52</td><br />
<td>東京(32)会計から、<a href="http://papiro.hatenablog.jp/entry/2017/02/12/162647">福岡</a>(8)(papironさん)、<a href="http://www.kunst1080.net/entry/2017/02/13/235721">大阪</a>（12）（くんすとさん）</td><br />
</tr><br />
<br />
<tr><br />
<td>26回</td><br />
<td>201612</td><br />
<td>47</td><br />
<td>東京(29)会計から、<a href="http://papiro.hatenablog.jp/entry/2016/12/26/011307">福岡</a>(7)(papironさん)、<a href="https://atnd.org/events/83966#members-join">大阪</a>（11）（くんすとさん）</td><br />
</tr><br />
<br />
<tr><br />
<td>25回</td><br />
<td>201610</td><br />
<td>48</td><br />
<td>東京(30)会計から、<a href="http://papiro.hatenablog.jp/entry/2016/10/29/225423" target="_blank">福岡</a>(9)(papironさん)、<a href="http://www.kunst1080.net/entry/2016/10/29/231725" target="_blank">大阪</a>（9）（くんすとさん）</td><br />
</tr><br />
<tr><br />
<td>24回</td><br />
<td>201608</td><br />
<td>46</td><br />
<td>東京(31)会計から、<a href="http://papiro.hatenablog.jp/entry/2016/08/28/135036" target="_blank">福岡</a>(3)(papironさん)、<a href="http://kunst1080.hatenablog.com/entry/2016/08/28/174226" target="_blank">大阪</a>（12）（くんすとさん）</td><br />
</tr><br />
<tr><br />
<td>23回</td><br />
<td>20160618</td><br />
<td>70</td><br />
<td>東京(48)会計から、<a href="http://papiro.hatenablog.jp/entry/2016/06/19/012906" target="_blank">福岡</a>(9)(papironさん)、<a href="http://kunst1080.hatenablog.com/entry/2016/06/19/143803" target="_blank">大阪</a>（13）（くんすとさん）</td><br />
</tr><br />
<tr><br />
<td>22回</td><br />
<td>20160430</td><br />
<td>67</td><br />
<td>東京(39)会計から、<a href="http://papiro.hatenablog.jp/entry/2016/04/30/234351" target="_blank">福岡(8)</a>(papironさん)、<a href="http://kunst1080.hatenablog.com/entry/2016/05/01/130621" target="_blank">大阪（20）</a>（くんすとさん）</td><br />
</tr><br />
<tr><br />
<td>21回</td><br />
<td>20160213</td><br />
<td>66</td><br />
<td>東京(50)会計から、<a href="http://papiro.hatenablog.jp/entry/2016/02/14/013100" target="_blank">福岡(8)</a>(papironさん)、<a href="http://kunst1080.hatenablog.com/entry/2016/02/15/164254" target="_blank">大阪（8）</a>（くんすとさん）</td><br />
</tr><br />
<tr><br />
<td>20回</td><br />
<td>20151226</td><br />
<td>53</td><br />
<td>東京(46)会計から、福岡(7)。<a href="https://twitter.com/papiron/status/684716869744340992" target="_blank">papironさんから</a></td><br />
</tr><br />
<tr><br />
<td>19回</td><br />
<td>20151031</td><br />
<td>37</td><br />
<td>東京(24)会計から, 福岡(9): <a href="http://papiro.hatenablog.jp/entry/2015/10/31/221613" target="_blank">papironさんのブログ</a>, 大阪(4): <a href="http://kunst1080.hatenablog.com/entry/2015/11/01/182428" target="_blank">くんすとさんのブログ</a></td><br />
</tr><br />
<tr><br />
<td>18回</td><br />
<td>20150829</td><br />
<td>50</td><br />
<td>東京(46)会計から, 福岡(4): papironさんのブログ</td><br />
</tr><br />
<tr><br />
<td>17回</td><br />
<td>20150618</td><br />
<td>45</td><br />
<td>\@ジュンク堂さん 予約数で概算（登壇者を含めると上回っている）</td><br />
</tr><br />
<tr><br />
<td>16回</td><br />
<td>20150418</td><br />
<td>52</td><br />
<td>東京(38);会計から、大阪(7):くんすとさんのブログ, 福岡(7):\@papironさんのブログから</td><br />
</tr><br />
<tr><br />
<td>15回</td><br />
<td>201502</td><br />
<td>20</td><br />
<td>会計から</td><br />
</tr><br />
<tr><br />
<td>14回</td><br />
<td>201412</td><br />
<td>20</td><br />
<td>会計から</td><br />
</tr><br />
<tr><br />
<td>13回</td><br />
<td>201410</td><br />
<td>38</td><br />
<td>東京(33)会計から, 大阪(5)申込者数</td><br />
</tr><br />
<tr><br />
<td>12回</td><br />
<td>201408</td><br />
<td>37</td><br />
<td>会計から</td><br />
</tr><br />
<tr><br />
<td>11回</td><br />
<td>201406</td><br />
<td>28</td><br />
<td>jus共催. 申込者数</td><br />
</tr><br />
<tr><br />
<td>10回</td><br />
<td>201404</td><br />
<td>42</td><br />
<td>会計から</td><br />
</tr><br />
<tr><br />
<td>9回</td><br />
<td>201402</td><br />
<td>24</td><br />
<td>会計から</td><br />
</tr><br />
<tr><br />
<td>8回</td><br />
<td>201312</td><br />
<td>28</td><br />
<td>会計から</td><br />
</tr><br />
<tr><br />
<td>7回</td><br />
<td>201310</td><br />
<td>34</td><br />
<td>会計から</td><br />
</tr><br />
<tr><br />
<td>6回</td><br />
<td>201308</td><br />
<td>20</td><br />
<td>LLまつりにて. 概算</td><br />
</tr><br />
<tr><br />
<td>5回</td><br />
<td>201306</td><br />
<td>29</td><br />
<td>会計から</td><br />
</tr><br />
<tr><br />
<td>4回</td><br />
<td>201304</td><br />
<td>53</td><br />
<td>申込者数</td><br />
</tr><br />
<tr><br />
<td>3回</td><br />
<td>201302</td><br />
<td>32</td><br />
<td>申込者数</td><br />
</tr><br />
<tr><br />
<td>2回</td><br />
<td>201212</td><br />
<td>25</td><br />
<td>申込者数</td><br />
</tr><br />
<tr><br />
<td>1回</td><br />
<td>201210</td><br />
<td>45</td><br />
<td>申込者数. hbstudy</td><br />
</tr><br />
</tbody><br />
</table>
