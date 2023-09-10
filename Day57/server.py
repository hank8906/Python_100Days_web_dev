from flask import Flask, render_template, url_for
import datetime
import requests

app = Flask(__name__)


@app.route("/")
def main_page():
    current_year = datetime.datetime.now().year
    return render_template("index.html", now_year=current_year)


@app.route("/<name>")
def guess_age(name):
    age_url = f"https://api.agify.io?name={name}"
    gender_url = f"https://api.genderize.io?name={name}"

    age_response = requests.get(url=age_url)
    gender_response = requests.get(url=gender_url)

    predict_age = age_response.json()['age']
    predict_gender = gender_response.json()['gender']

    message = f"Hi {name}!\nI guessed you are a {predict_gender} and is {predict_age} years old"

    return render_template("index.html", message=message)


@app.route("/blog/<num>")
def get_blog(num):
    response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
    all_posts = response.json()

    return render_template("blog.html", posts=all_posts)


if __name__ == "__main__":
    app.run(debug=True)
