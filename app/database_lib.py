import sqlite3
import random
import string
import json
from app.request_data import *

DATA_MANIFEST = open_data('manifest.json')

def check_table(cursor, name):
    cursor.execute("SELECT * FROM {}".format(name))
    table = cursor.fetchall()
    return table

def random_string(length):
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(length))

def split_page(data, page):
    max_page = int(len(data) / PER_PAGE)
    if len(data) % PER_PAGE > max_page:
        max_page += 1

    this_page_from = page*PER_PAGE
    this_page_to = (page + 1)*PER_PAGE

    if this_page_to > len(data) - 1:
        this_page_to = len(data)

    result = []
    for i in range(len(data)):
        da = data[(len(data) - 1 - i)]
        if this_page_from <= i < this_page_to:
            result.append(da)

    if page > 0:
        last_page = page - 1
    else:
        last_page = None

    if page < max_page:
        next_page = page + 1
    else:
        next_page = None
    return result, last_page, next_page, max_page

def check_user_data(chat_id, full_name):
    if DATA_MANIFEST['user'] == 'OFF':
        return None
    else:
        pass

def get_list_item_name(data):
    result = []
    for name, item in data.items():
        result.append(name)
    return result


#===========================+++