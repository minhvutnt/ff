import sqlite3
import sys
from datetime import datetime
import requests
import json
from threading import Thread
import time



db_name = "app.db"

def check_all():
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    res = c.execute("SELECT name FROM sqlite_master WHERE type='table';")
    table = []
    for name in res:
        table.append(name[0])
    conn.commit()
    conn.close()
    return table


def check_table(name):
    conn = sqlite3.connect(db_name)
    conn_cursor = conn.cursor()

    conn_cursor.execute("SELECT * FROM {}".format(name))
    table = conn_cursor.fetchall()
    conn.close()
    return table

def check_table_title(name):
    conn = sqlite3.connect(db_name)
    cursor = conn.execute('select * from {}'.format(name))
    return cursor.description

def delete_row():
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    for i in range(100):
        sql_delete_query = """DELETE from user where id = {}""".format(i)
        cursor.execute(sql_delete_query)
    conn.commit()
    conn.close()
delete_row()
print(check_all())
print(check_table("user"))
# print("TABLE TAB: ", check_table_title("user"))