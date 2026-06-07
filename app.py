from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1><h1>鄭道可個人網站</h1></h1>

    <img src="https://picsum.photos/600/300" width="600">

    <br><br>

    <a href="/about">關於我</a>

    <br><br>

    <a href="/works">我的作品</a>

    <br><br>

    <a href="/contact">聯絡方式</a>
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
    app.run(debug=True)
           