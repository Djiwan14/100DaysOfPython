import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
response = requests.get(URL)
web_page = response.text
soup = BeautifulSoup(web_page, "html.parser")

# web scraping
movies = soup.find_all(name="h3", class_="title")
titles = [movie.getText() for movie in movies]
for title in titles[::-1]:
    print(title)

# file handling
with open("movies.txt", mode="w") as data:
    for title in titles[::-1]:
        data.write(f"{title}\n")
