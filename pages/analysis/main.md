---
Keywords: bashcms2
Copyright: (C) Ryuichi Ueda
---


# サイトの統計


## リアルタイム

|||
|----|----:|
|過去1分の閲覧数| <span id="last1min" style="font-size:200%"></span> |
|過去30分の閲覧数| <span id="last30min" style="font-size:200%"></span> |
|本日の閲覧数| <span id="todayvisit" style="font-size:200%"></span> |


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


lastmin(1);
lastmin(30);
lastvisit(10);
todayvisit(10);

setInterval(lastvisit, 3000, 10);
setInterval(todayvisit, 3000, 10);
setInterval(lastmin, 3000, 30);
setInterval(lastmin, 3000, 1);
</script>
