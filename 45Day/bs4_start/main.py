from bs4 import BeautifulSoup
with open("website.html", encoding="utf8", mode="r") as site:
    data = site.read()

soup = BeautifulSoup(data, 'html.parser')
# print(soup)
# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)

# print(soup.prettify())
# print(soup.a)

# anchor_tags = soup.find_all(name="a")
# for tag in anchor_tags:
#     # print(tag.getText())
#     print(tag.get("href"))
heading = soup.find(name="h1", id="name")
print(heading)

section_heading = soup.find(name="h3", class_="heading")
print(section_heading)

name = soup.select("#name")
print(name)

company_url = soup.select_one(selector="p a")
print(company_url)