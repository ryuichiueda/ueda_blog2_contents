# Python2.7でOpenCVを使ったコードをTravis CI（まだUbuntu 14.04）でテストするときの設定
新年早々ドハマりしたのでメモ。環境はTravisCI標準のUbuntu 14.04（いつになったら16.04になるんでしょうか？！？！？！）。OpenCVはaptで入るバージョンです。<br />
<br />
.travis.ymlはこんな感じ。PYTHONPATHを設定するという正解にたどり着くまでに3時間くらいかかりました・・・<br />
<pre>sudo: required<br />
dist: trusty<br />
<br />
script:<br />
 - sudo apt-get update<br />
 - sudo apt-get install libopencv-dev python-opencv<br />
 - export PYTHONPATH=$PYTHONPATH:/usr/lib/python2.7/dist-packages<br />
 - ./test.py<br />
</pre><br />
<br />
./test.pyというのはこれ。<br />
<pre>#!/usr/bin/env python<br />
import cv2<br />
print cv2.__version__<br />
</pre><br />
<br />
PYTHONPATHの設定がないと<br />
<pre>$ ./test.py<br />
Traceback (most recent call last):<br />
 File "./test.py", line 2, in <module><br />
 import cv2<br />
ImportError: No module named cv2</pre><br />
となってテスト（といっても何もテストしてませんが）が失敗します。<br />
<br />
PYTHONPATHの行を加えてテストを走らせて<a href="https://travis-ci.org/ryuichiueda/travis_opencv_test/builds/188429578">ログ</a>を見ると<br />
<pre>libdc1394 error: Failed to initialize libdc1394</pre><br />
と出ますが、./test.pyの終了ステータスは0で無事に成功と表示されました。<br />
<br />
デスクトップでも「ImportError: No module named cv2」と出るときはPYTHONPATHを疑うということで。<br />
<br />
<h2>補足</h2><br />
<br />
PYTHONPATHで加えるべきディレクトリは<br />
<pre><br />
sudo find / | grep -F cv2.so<br />
</pre><br />
で検索できるので、.travis.ymlに書いて探すとよいでしょう。<br />
<br />

