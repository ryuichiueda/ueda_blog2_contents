---
Keywords: bashcms2
Copyright: (C) Ryuichi Ueda
---


# サイトの統計


## リアルタイム統計

* 過去30分の閲覧数: <span id="lastmin" style="font-size:200%"></span>


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

        document.getElementById("lastmin").innerHTML = httpReq.responseText;
   }
    var url = "/analyzer/lastmin.cgi?min=" + min;
    httpReq.open("GET",url,true);
    httpReq.send(null);
}

lastmin(30);
lastvisit(10);

setInterval(lastvisit, 3000, 10);
setInterval(lastmin, 3000, 30);
</script>
