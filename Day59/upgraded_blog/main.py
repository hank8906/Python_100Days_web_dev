from flask import Flask, render_template
import requests

app = Flask(__name__)

url = "https://api.npoint.io/238651492acd348bbdea"
all_post = requests.get(url=url).json()


@app.route('/')
def home_page():
    return render_template("index.html", posts=all_post)


@app.route('/about')
def about_page():
    return render_template("about.html")


@app.route('/contact')
def contact_page():
    return render_template("contact.html")


@app.route('/post/<num>')
def get_post(num):
    index = int(num) - 1
    posts_body = all_post[index]

    return render_template("post.html", posts_body=posts_body)


if __name__ == "__main__":
    app.run(debug=True)
