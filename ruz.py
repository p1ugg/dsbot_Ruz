# -*- coding: utf-8 -*-

import requests
from pprint import pprint
import json
from datetime import date


main_url = "https://ruz.hse.ru"

def get_student_schedule(email, start_date, end_date, lng):
    params = { 'start': start_date,
               'end': end_date,
               'email': email
               }
    headers = {"Accept-Language": "ru-RU, ru;q=0.9"}
    url = 'https://api.hseapp.ru/v3/ruz/lessons'
    r = requests.get(url, params=params, headers=headers)
    return json.loads(r.text)


def email_is_valid(email):

    try:
        email = email.strip()
        test_date = date.today()
        test_date_f= test_date.strftime("%Y.%m.%d")
        resp = get_student_schedule(email, test_date_f, test_date_f, 1)
        resp['error']
        return False
    except Exception as e:
        return True

# print(email_is_valid("iegazz12aev@edu.hse.ru"))