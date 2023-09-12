from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route('/')
def home():
    all_posts_response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
    posts = all_posts_response.json()
    return render_template("index.html", posts=posts)


@app.route('/post/<num>')
def get_post(num):
    response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
    index = int(num) - 1
    posts_body = response.json()[index]

    return render_template("post.html", posts_body=posts_body)


if __name__ == "__main__":
    app.run(debug=True)
