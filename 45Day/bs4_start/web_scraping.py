from bs4 import BeautifulSoup
import requests
response = requests.get("https://news.ycombinator.com/news")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
# print(soup.title)
# first_title = soup.find(name="span", class_="titleline")
# article_text = first_title.getText()
# print(article_text)
# article_link = first_title.find(name="a").get("href")
# print(article_link)
# article_upvote = soup.find(name="span", class_="score").getText()
# print(article_upvote)
articles = soup.find_all(name="span", class_="titleline")
article_texts = []
article_links = []
for article_tag in articles:
    text = article_tag.getText()
    article_texts.append(text)
    link = article_tag.find(name="a").get("href")
    article_links.append(link)
article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

print(article_texts)
print(article_links)
print(article_upvotes)
max_number_of_upvotes = max(article_upvotes)
index = article_upvotes.index(max_number_of_upvotes)
challenge_list = []
challenge_list.append(article_texts[index])
challenge_list.append(article_links[index])
challenge_list.append(article_upvotes[index])
print(challenge_list)