import json
import sqlite3


database_binance_name = 'user_binance.db'

def binance_create_db():
    # try:
        conn = sqlite3.connect(database_binance_name)
        c = conn.cursor()


        try: #update tp_7
            c.execute('''ALTER TABLE SIGNAL ADD COLUMN tp7 float''')
            c.execute('''ALTER TABLE SIGNAL ADD COLUMN tp7_hit char[3]''')

            c.execute('''ALTER TABLE SYMBOL ADD COLUMN tp7 float''')
        except Exception as e:
            print("Signal add col tp7: {}".format(str(e)))

        try: #update group_group
            c.execute('''ALTER TABLE LIST_GROUP ADD COLUMN number int''')
        except Exception as e:
            print("Group of Group: {}".format(str(e)))

        try: #update digit
            c.execute('''ALTER TABLE SYMBOL ADD COLUMN digit float''')
        except Exception as e:
            print("Signal add col digit: {}".format(str(e)))

        conn.commit()
        conn.close()
        print("create db ok")
    # except:
    #     print("create db false")

binance_create_db()

def binance_check_table(cursor, name):
    cursor.execute("SELECT * FROM {}".format(name))
    table = cursor.fetchall()
    return table


# def start_list_port_tradingview():
#     conn = sqlite3.connect(database_binance_name)
#     cursor = conn.cursor()
#     all_port = binance_check_table(cursor, "LIST_PORT_TRADINGVIEW")
#     for port in all_port:
#         DATA_LIST_PORT_TRADINGVIEW.append({
#             "stt": port[0],
#             "time": port[1],
#             "signal": port[2],
#             "full_opentime": timestamp_to_date(port[1]/1000)
#         })
#     conn.close()
#
# start_list_port_tradingview()


# ======================================================================================================================
def save_data(data, link):
    data_new = open(link, "w", encoding='utf-8')
    json.dump(data, data_new, indent=4)
    data_new.close()

def open_data(link):
    with open(link, 'r+', encoding='utf-8') as user:
        data = json.load(user)
    user.close()
    return data
