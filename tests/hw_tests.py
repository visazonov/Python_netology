from unittest import TestCase
import pytest
from decimal import Decimal

import requests
import tests.configuration

from tests.main_tests import geo_logs_russia
from tests.main_tests import unique_geo_id
from tests.main_tests import queries_percent
from tests.main_tests import create_folder
from tests.main_tests import get_files_list
from tests.main_tests import get_folder_list
from tests.main_tests import del_folder


def test_geo_logs_russia():
    geo_logs = [
        {'visit1': ['Москва', 'Россия']},
        {'visit2': ['Дели', 'Индия']},
        {'visit3': ['Владимир', 'Россия']},
        {'visit4': ['Лиссабон', 'Португалия']},
        {'visit5': ['Париж', 'Франция']},
        {'visit6': ['Лиссабон', 'Португалия']},
        {'visit7': ['Тула', 'Россия']},
        {'visit8': ['Тула', 'Россия']},
        {'visit9': ['Курск', 'Россия']},
        {'visit10': ['Архангельск', 'Россия']}
    ]
    res = geo_logs_russia(geo_logs)
    assert {'visit1': ['Москва', 'Россия']} in res
    assert len(res) == 6
    for r in res:
        assert 'Россия' in list(r.values())[0]
        # for k, v in r.items():
        #     assert 'Россия' in v

def test_unique_geo_id():
    ids = {'user1': [213, 213, 213, 15, 213],
           'user2': [54, 54, 119, 119, 119],
           'user3': [213, 98, 98, 35]}

    res = unique_geo_id(ids)
    assert len(res) == len(set(res))

def test_queries_percent():
    queries = [
        'смотреть сериалы онлайн',
        'новости спорта',
        'афиша кино',
        'курс доллара',
        'сериалы этим летом',
        'курс по питону',
        'сериалы про спорт'
    ]
    res = queries_percent(queries)
    assert isinstance(res, dict)
    assert res == {3: 57, 2: 43}

def test_create_folder():

    folder_list = get_folder_list('/').json()
    for list_folder in folder_list['_embedded']['items']:
        if list_folder['name'] == 'backup':
            del_folder('/backup/')

    res = create_folder('/backup/')

    folder_list = get_folder_list('/').json()
    count = 0
    for list_folder in folder_list['_embedded']['items']:
        if list_folder['name'] == 'backup':
            count+= 1

    assert res.status_code == 201
    assert count > 0

def test_create_folder_no_auth():

    folder_list = get_folder_list('/').json()
    for list_folder in folder_list['_embedded']['items']:
        if list_folder['name'] == 'backup':
            del_folder('/backup/')

    def get_headers():
        return {
            'Content-Type': 'application/json',
        }

    def create_folder_no_auth(path):
        create_url = tests.configuration.base_host + tests.configuration.create_folder_uri
        params = {'path': path}
        response = requests.put(create_url, headers=get_headers(), params=params)
        return response

    res = create_folder_no_auth('/backup/')

    assert res.status_code == 401
    assert res.json()['message'] == 'Не авторизован.'

def test_create_folder_iam_exstat():

    folder_list = get_folder_list('/').json()
    for list_folder in folder_list['_embedded']['items']:
        if list_folder['name'] == 'backup':
            del_folder('/backup/')

    result = create_folder('/backup/')
    res = create_folder('/backup/')

    folder_list = get_folder_list('/').json()
    count = 0
    for list_folder in folder_list['_embedded']['items']:
        if list_folder['name'] == 'backup':
            count+= 1

    assert res.status_code == 409
    assert res.json()['message'] == 'По указанному пути "/backup/" уже существует папка с таким именем.'



# pytest tests\hw_tests.py