from bs4 import BeautifulSoup
import requests

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/"
                        "best-movies-2/")

movie_webpage = response.text

soup = BeautifulSoup(movie_webpage, "html.parser")

selector = soup.select(".article-title-description > .article-title-description__text > .title")
# print(selector)

movies = []

for movie in selector:
    movies.append(movie.get_text())

reversed_movies = movies[::-1]
# print(reversed_movies)

with open("top_100_movies.text_1", 'w', errors='ignore') as file:
    for movie in reversed_movies:
        file.write(f"{movie}\n")