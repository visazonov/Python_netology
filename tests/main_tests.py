import os
from dotenv import load_dotenv

load_dotenv()
token = os.getenv("TOKEN")

import requests
from pprint import pprint
import tests.configuration


def summarise(x, y):
    return x + y


def myltiply(x, y):
    return x * y


def get_dict():
    return {"name": "Ivan", "age": 29, "city": "Moscow"}


def geo_logs_russia(geo_logs):
    geo_logs_rus = []

    for logs in geo_logs:
        for key, value in logs.items():
            if value[1] == "Россия":
                geo_logs_rus.append(logs)
    return geo_logs_rus


def unique_geo_id(ids):
    ids_new = []
    for ids2 in ids.values():
        ids_new += ids2
    ids_new2 = set(ids_new)
    return list(ids_new2)


def queries_percent(queries):
    total_request_quantity = len(queries)  # общее кол-во запросов
    dct = {}
    dct_percent = {}

    for query in queries:
        count = len(query.split())
        dct[count] = dct.get(count, 0) + 1

    # Для каждого элемента словаря, т.е. для каждого кол-ва слов расчитываем процент и выводим на печать
    for key in dct:
        percent_of_queries = round(dct[key] / total_request_quantity * 100)
        dct_percent[key] = dct_percent.setdefault(key, percent_of_queries)
        # print(f'Кол-во слов в запросе {key}  - {percent_of_queries}')
    return dct_percent


def get_headers():
    return {"Content-Type": "application/json", "Authorization": f"OAuth {token}"}


def create_folder(path):
    create_url = tests.configuration.base_host + tests.configuration.create_folder_uri
    params = {"path": path}
    response = requests.put(create_url, headers=get_headers(), params=params)
    return response


def get_files_list():  #  получить список файлов
    request_url = tests.configuration.base_host + tests.configuration.get_files_list_uri
    params = {"limit": "30"}
    response = requests.get(request_url, headers=get_headers(), params=params)
    return response


def get_folder_list(path):  # получить список папок
    request_url = (
        tests.configuration.base_host + tests.configuration.get_folder_list_uri
    )
    params = {"path": path}
    response = requests.get(request_url, headers=get_headers(), params=params)
    return response


def del_folder(path):
    request_url = tests.configuration.base_host + tests.configuration.del_folder_uri
    params = {"path": path}
    response = requests.delete(request_url, headers=get_headers(), params=params)
    return response
