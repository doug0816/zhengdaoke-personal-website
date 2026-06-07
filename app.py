@app.route("/")
def home():
    return """
<!DOCTYPE html>
<html>
<head>
<style>
body{
    margin:0;
    min-height:100vh;
    overflow:hidden;
    color:white;
    text-align:center;
    font-family:Arial;
}

.bg{
    position:fixed;
    inset:0;
    background-image:url('/static/background.png');
    background-size:cover;
    background-position:center;
    background-repeat:no-repeat;
    transform:translateY(100%);
    animation:slideUp 1.8s cubic-bezier(0.16, 1, 0.3, 1) forwards;
}

.content{
    position:relative;
    z-index:2;
    padding-top:100px;
}

@keyframes slideUp{
    from{
        transform:translateY(100%);
    }
    to{
        transform:translateY(0);
    }
}
</style>
</head>

<body>

<div class="bg"></div>

<div class="content">
    <h1>鄭道可個人網站</h1>

    <a style="color:white;" href="/about">關於我</a><br><br>
    <a style="color:white;" href="/works">我的作品</a><br><br>
    <a style="color:white;" href="/contact">聯絡方式</a>
</div>

</body>
</html>
"""