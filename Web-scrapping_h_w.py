import requests
from bs4 import BeautifulSoup
from fake_headers import Headers
import json


def get_headers():
    headers = Headers(browser="firefox", os="win")
    return headers.generate()


def Web_scrapping():
    # responce = requests.get('https://spb.hh.ru/search/vacancy?text=python&area=1&area=2/', headers=get_headers())
    responce = requests.get(
        "https://spb.hh.ru/search/vacancy?text=python%20django%20flask&area=1&area=2/",
        headers=get_headers(),
    )
    hh_main = responce.text
    soup = BeautifulSoup(hh_main, features="lxml")

    a11y_main_content_list = soup.find("main", class_="vacancy-serp-content")

    main_content_list = a11y_main_content_list.find_all("div", class_="serp-item")
    print(len(main_content_list))
    parsed = []

    for content_list in main_content_list:
        link_tag = content_list.find("h3")
        link_tag_a = link_tag.find("a")
        link_related = link_tag_a["href"]
        link_absolute = f"{link_related}"

        span_tag = content_list.find("span")
        name_span = span_tag.text

        company_name_tag = content_list.find(
            "div", class_="vacancy-serp-item__meta-info-company"
        )
        company_name_tag_a = company_name_tag.find("a")
        company_name_text = company_name_tag_a.text

        salary_tag = content_list.find("span", class_="bloko-header-section-2")
        if salary_tag != None:
            salary_span = salary_tag.text
        else:
            salary_span = "None"
        print(salary_span)

        responce = requests.get(link_absolute, headers=get_headers())
        vacancy_content = BeautifulSoup(responce.text, features="lxml")
        vacancy_content_tag = vacancy_content.find(
            "div", class_="vacancy-company-redesigned"
        )
        sity_tag = vacancy_content_tag.find("p")
        if sity_tag != None:
            sity = sity_tag.text
        else:
            sity = "None"

        item = {
            "link": link_related,
            "company_name": company_name_text,
            "vacancy name": name_span,
            "salary": salary_span,
            "sity": sity,
        }

        parsed.append(item)

    # print()

    # with open('hh.json', 'w', encoding='utf-8') as file:
    #   json.dump(parsed, file, indent=5, ensure_ascii=False)


if __name__ == "__main__":
    Web_scrapping()
