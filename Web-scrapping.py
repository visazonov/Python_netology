import requests
from bs4 import BeautifulSoup
from fake_headers import Headers
import json


def get_headers():
    headers = Headers(browser="firefox", os="win")
    return headers.generate()


responce = requests.get("https://habr.com/ru/all/", headers=get_headers())
# responce = requests.get('https://habr.com/ru/all/')
habr_main = responce.text
soup = BeautifulSoup(habr_main, features="lxml")


article_list = soup.find("div", class_="tm-articles-list")
articles = article_list.find_all("article")

parsed = []

for article in articles:
    time_tag = article.find("time")
    header = article.find("h2")

    time_parsed = time_tag["datetime"]
    header_parsed = header.text

    a_tag = header.find("a")
    link_related = a_tag["href"]
    link_absolute = f"https://habr.com{link_related}"

    responce = requests.get(link_absolute, headers=get_headers())
    habr_article = BeautifulSoup(responce.text, features="lxml")
    habr_article_tag = habr_article.find("div", id="post-content-body")
    habr_article_text = habr_article_tag.text

    item = {
        "time": time_parsed,
        "header": header_parsed,
        "link": link_absolute,
        "text": habr_article_text,
    }
    # print(item)
    parsed.append(item)
    if len(parsed) >= 5:
        break


with open("habr.json", "w", encoding="utf-8") as file:
    json.dump(parsed, file, indent=5, ensure_ascii=False)

# with open('habr.json') as file:
#   data = json.load(file)
# print(data)
print("ehf")


# получить статус код
import requests
import fake_headers

headers = fake_headers.Headers(browser="firefox", os="win").generate()

resource = requests.get("https://spb.hh.ru/", headers=headers)
print(resource.status_code)
