import requests
from bs4 import BeautifulSoup
import lxml
import smtplib
import os

my_email = os.environ['my_email']
password = os.environ['password']

url = "https://www.amazon.com/-/zh_TW/16757045-Fujifilm-X-H2-%E7%84%A1%E5%8F%8D%E5%85%89%E9%8F%A1%E7%9B%B8%E6%A9%9F%E6%A9%9F%E8%BA%AB-%E9%BB%91%E8%89%B2/dp/B0BCLYBK1F/ref=sr_1_3?crid=1J5Q3BUHT8WTI&keywords=fuji%2Bxt5&qid=1694254515&sprefix=fuji%2Bxt%2Caps%2C255&sr=8-3&th=1"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 "
                  "Safari/537.36",
    "Accept-Language": "zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7"
}

response = requests.get(url=url, headers=headers)
web_page = response.text

# print(response.content)

soup = BeautifulSoup(web_page, "lxml")
song_selector = soup.select_one(".a-price-whole")

price = song_selector.get_text().split('.')[0]
int_price = int(price.replace(",", ""))
print(int_price)

is_price_fall = False

if int_price < 1900:
    is_price_fall = True

if is_price_fall:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="huanghank2000@myyahoo.com",
                            msg="Subject:Price fall alert!!!\n\n"
                                f"Look up the link:{url} and check the product you are looking for!")
