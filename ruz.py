# -*- coding: utf-8 -*-

import requests
from pprint import pprint
import json
from datetime import date, timedelta
import formater


main_url = "https://ruz.hse.ru"


def get_students_list(student_name):
    params = { 'term': student_name,
               'type': 'student'}
    url = main_url+'/api/search'
    r = requests.get(url, params=params)
    return json.loads(r.text)


def get_student_schedule(email, start_date, end_date, lng): # ('254711', '2020.09.28','2020.10.04', 1)
    params = { 'start': start_date,
               'end': end_date,
               'email': email
               }
    headers = {"Accept-Language": "ru-RU, ru;q=0.9"}
    url = 'https://api.hseapp.ru/v3/ruz/lessons'
    r = requests.get(url, params=params, headers=headers)
    return json.loads(r.text)

# a = get_student_schedule("iegazzaev@edu.hse.ru", "2024.05.13", "2024.05.20", 1)
# pprint(a)
# print(formater.format_schedule_active(a))

def get_group_schedule(group_id, start_date, end_date, lng): # ('254711', '2020.09.28','2020.10.04', 1)
    params = { 'start': start_date,
               'end': end_date,
               'group': group_id
               }
    headers = {"Accept-Language": "ru-RU, ru;q=0.9"}
    url = 'https://api.hseapp.ru/v3/ruz/lessons'
    r = requests.get(url, params=params, headers=headers)
    return json.loads(r.text)


def get_groups_list(group_name):
    # https://ruz.hse.ru/api/search?term=ББИ2008&type=group
    params = { 'term': group_name,
               'type': 'group'}
    url = 'https://ruz.hse.ru/api/search'
    r = requests.get(url, params=params)
    return json.loads(r.text)





def email_is_valid(email):
    """
    Определяет, существует ли такой EMAIL,
    отправляя запрос на получение его расписания
    """
    try:
        email = email.strip()
        test_date = date.today()
        test_date_f= test_date.strftime("%Y.%m.%d")
        resp = get_student_schedule(email, test_date_f, test_date_f, 1)
        resp['error']
        return False
    except Exception as e:
        return True
