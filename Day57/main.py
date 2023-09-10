from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route('/')
def home(num):
    response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
    posts = response.json()
    return render_template("index.html", posts=posts)


@app.route('/blog/<num>')
def get_blog(num):
    response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
    posts = response.json()[num-1]

    return render_template("post.html", posts=posts)


if __name__ == "__main__":
    app.run(debug=True)
