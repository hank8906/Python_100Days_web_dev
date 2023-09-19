from flask import Flask, render_template, request
import requests
import smtplib

app = Flask(__name__)

my_email = "huanghank8906@gmail.com"
password = "xwcczfmjyoudaave"

url = "https://api.npoint.io/238651492acd348bbdea"
all_post = requests.get(url=url).json()


@app.route('/')
def home_page():
    return render_template("index.html", posts=all_post)


@app.route('/about')
def about_page():
    return render_template("about.html")


@app.route('/contact', methods=['GET', 'POST'])
def contact_page():
    if request.method == 'GET':
        return render_template("contact.html")
    else:
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        message = request.form['message']
        success_message = 'Successfully send the message!'

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email,
                                to_addrs="huanghank2000@myyahoo.com",
                                msg="Subject:Contact message from Hank's Blog\n\n"
                                    f"name:{name}\nemail:{email}\nphone:{phone}\nmessage:{message}")

        print(f"{name}\n{email}\n{phone}\n{message}")
        return render_template("contact.html",success_message=success_message)


@app.route('/post/<num>')
def get_post(num):
    index = int(num) - 1
    posts_body = all_post[index]

    return render_template("post.html", posts_body=posts_body)


if __name__ == "__main__":
    app.run(debug=True)
