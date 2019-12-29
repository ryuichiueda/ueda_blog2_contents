---
Keywords: bashcms2
Copyright: (C) Ryuichi Ueda
---


# サイトの統計


## リアルタイム

### 閲覧数

|||
|----|----:|
|過去1分| <span id="last1min" style="font-size:200%"></span> |
|過去30分| <span id="last30min" style="font-size:200%"></span> |
|本日| <span id="todayvisit" style="font-size:200%"></span> |
|通算（2017年10月〜）| <span id="allpv" style="font-size:200%"></span> |


### 現在閲覧されているページ

<span id="lastvisit"></span>

<script>
function lastvisit(num){
    var httpReq = new XMLHttpRequest();
    httpReq.onreadystatechange = function(){
        if(httpReq.readyState != 4 || httpReq.status != 200)
            return;

        document.getElementById("lastvisit").innerHTML = httpReq.responseText;
   }
    var url = "/analyzer/lastvisit.cgi?num=" + num;
    httpReq.open("GET",url,true);
    httpReq.send(null);
}

function lastmin(min){
    var httpReq = new XMLHttpRequest();
    httpReq.onreadystatechange = function(){
        if(httpReq.readyState != 4 || httpReq.status != 200)
            return;

        document.getElementById("last"+min+"min").innerHTML = httpReq.responseText;
   }
    var url = "/analyzer/lastmin.cgi?min=" + min;
    httpReq.open("GET",url,true);
    httpReq.send(null);
}

function todayvisit(){
    var httpReq = new XMLHttpRequest();
    httpReq.onreadystatechange = function(){
        if(httpReq.readyState != 4 || httpReq.status != 200)
            return;

        document.getElementById("todayvisit").innerHTML = httpReq.responseText;
   }
    var url = "/analyzer/todayvisit.cgi?d=" + new Date();
    httpReq.open("GET",url,true);
    httpReq.send(null);
}

function allpv(){
    var httpReq = new XMLHttpRequest();
    httpReq.onreadystatechange = function(){
        if(httpReq.readyState != 4 || httpReq.status != 200)
            return;

        document.getElementById("allpv").innerHTML = httpReq.responseText;
   }
    var url = "/analyzer/allpv.cgi?d=" + new Date();
    httpReq.open("GET",url,true);
    httpReq.send(null);
}


lastmin(1);
lastmin(30);
lastvisit(10);
todayvisit(10);
allpv();

setInterval(lastvisit, 3000, 10);
setInterval(todayvisit, 3000, 10);
setInterval(lastmin, 3000, 30);
setInterval(lastmin, 3000, 1);
setInterval(allpv, 3000);
</script>

## 閲覧数

### 日次（過去10日間）

<span id="daily"></span>

### 月次

<span id="monthly"></span>

<script>
function monthly(){
    var httpReq = new XMLHttpRequest();
    httpReq.onreadystatechange = function(){
        if(httpReq.readyState != 4 || httpReq.status != 200)
            return;

        document.getElementById("monthly").innerHTML = httpReq.responseText;
   }
    var url = "/analyzer/monthly.cgi?d=" + new Date();
    httpReq.open("GET",url,true);
    httpReq.send(null);
}

monthly();
</script>
