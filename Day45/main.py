from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")
yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, "html.parser")

selector = soup.select(".title > .titleline > a")
score_selector = soup.select(".subtext > .subline > .score")

text = []
href = []
score = []

for span_element in score_selector:
    score.append(int(span_element.get_text().split()[0]))

for a_element in selector:
    text.append(a_element.get_text())
    href.append(a_element.get('href'))

# print(text)
# print(href)
# print(score)

max_score = max(score)
max_index = score.index(max_score)

print(text[max_index])
print(href[max_index])