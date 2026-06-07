from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <body style="
        margin:0;
        min-height:100vh;
        background-image:url('/static/background.jpg');
        background-size:cover;
        background-position:center;
        background-repeat:no-repeat;
        color:white;
        text-align:center;
        padding-top:100px;
        font-family:Arial;
    ">

    <h1>鄭道可個人網站</h1>

    <a style="color:white;" href="/about">關於我</a><br><br>
    <a style="color:white;" href="/works">我的作品</a><br><br>
    <a style="color:white;" href="/contact">聯絡方式</a>

    </body>
    """

@app.route("/about")
def about():
    return """
    <h1>關於我</h1>
    <p>我是 Douglas。</p>
    <a href="/">回首頁</a>
    """

@app.route("/works")
def works():
    return """
    <h1>我的作品</h1>
    <p>這裡之後可以放 Blender 作品。</p>
    <a href="/">回首頁</a>
    """

@app.route("/contact")
def contact():
    return """
    <h1>聯絡方式</h1>
    <p>Instagram：@DOARTS</p>
    <a href="/">回首頁</a>
    """

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)