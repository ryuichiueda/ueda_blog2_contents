---
Keywords: プログラミング,OpenCV,Python,Travis
Copyright: (C) 2017 Ryuichi Ueda
---

# Python2.7でOpenCVを使ったコードをTravis CI（まだUbuntu 14.04）でテストするときの設定
新年早々ドハマりしたのでメモ。環境はTravisCI標準のUbuntu 14.04（いつになったら16.04になるんでしょうか？！？！？！）。OpenCVはaptで入るバージョンです。

.travis.ymlはこんな感じ。PYTHONPATHを設定するという正解にたどり着くまでに3時間くらいかかりました・・・
<pre>sudo: required
dist: trusty

script:
 - sudo apt-get update
 - sudo apt-get install libopencv-dev python-opencv
 - export PYTHONPATH=$PYTHONPATH:/usr/lib/python2.7/dist-packages
 - ./test.py
</pre>

./test.pyというのはこれ。
<pre>#!/usr/bin/env python
import cv2
print cv2.__version__
</pre>

PYTHONPATHの設定がないと
<pre>$ ./test.py
Traceback (most recent call last):
 File "./test.py", line 2, in <module>
 import cv2
ImportError: No module named cv2</pre>
となってテスト（といっても何もテストしてませんが）が失敗します。

PYTHONPATHの行を加えてテストを走らせて<a href="https://travis-ci.org/ryuichiueda/travis_opencv_test/builds/188429578">ログ</a>を見ると
<pre>libdc1394 error: Failed to initialize libdc1394</pre>
と出ますが、./test.pyの終了ステータスは0で無事に成功と表示されました。

デスクトップでも「ImportError: No module named cv2」と出るときはPYTHONPATHを疑うということで。

<h2>補足</h2>

PYTHONPATHで加えるべきディレクトリは
<pre>
sudo find / | grep -F cv2.so
</pre>
で検索できるので、.travis.ymlに書いて探すとよいでしょう。


