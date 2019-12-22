---
Copyright: (C) Ryuichi Ueda
---


# サイトの統計

## 現在閲覧されているページ

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

setInterval(lastvisit, 3000, 10);
</script>
