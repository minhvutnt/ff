import time
from datetime import datetime
import requests
import json
import random
import threading

def request_link(link):
    all_leader_request = requests.get(link)
    content = all_leader_request.content.decode("utf8")
    js = json.loads(content)
    return js

def request_post(link, data=None):
    all_leader_request = requests.post(link, json=data)
    content = all_leader_request.content.decode("utf8")
    js = json.loads(content)
    return js

def date_to_timestamp(date_check):
    timestamp = datetime.timestamp(date_check)
    return timestamp


def timestamp_to_date(timestamp):
    dt_object = datetime.fromtimestamp(timestamp)
    return dt_object


def time_now():
    result = datetime.now()
    ts = date_to_timestamp(result)
    new_result = timestamp_to_date(ts)
    return new_result


def convert_string_to_date(year_month_day):
    return datetime.strptime(year_month_day, '%Y-%m-%d')

URL = 'http://127.0.0.1:4040/api/'
LINK_CREATE_USER = URL + 'create_user'
LINK_LIST_ROOM_DATA = URL + 'list_baucua_room'
LINK_CREATE_ROOM = URL + 'create_baucua_room'
LINK_DEPOSIT = URL + 'deposit'
LINK_EXP = URL + 'exp'
LINK_BET_BAUCUA = URL + 'bet_baucua'
LINK_BAUCUA_STATUS = URL + 'change_room_baucua_status'
LINK_CHANGE_ROOM_AMOUNT = URL + 'change_room_baucua_amount'


DATA = [{"id": 1000 ,"check": 0, "status": 1, "name": "Keponakan Stanly🌱SEED 🐾 🌊"},
        {"id": 1001 ,"check": 0, "status": 1, "name": "Artur Ferreira"},
        {"id": 1002 ,"check": 0, "status": 1, "name": "Khoa 🐾 Đặng Đình"},
        {"id": 1003 ,"check": 0, "status": 1, "name": "🐤Agus Gra-Gra 🌱"},
        {"id": 1004 ,"check": 0, "status": 1, "name": "Sascha"},
        {"id": 1005 ,"check": 0, "status": 1, "name": "Song Diệp 🆙 UXUY"},
        {"id": 1006 ,"check": 0, "status": 1, "name": "⚜️ 𝑴𝒂𝒊 𝑷𝒉𝒖̛𝒐̛𝒏𝒈 ⚜️"},
        {"id": 1007 ,"check": 0, "status": 1, "name": "ℕ𝕒ℝ𝕚 ⚜️⚜️"},
        {"id": 1008 ,"check": 0, "status": 1, "name": "Thanh Sơn DM"},
        {"id": 1009 ,"check": 0, "status": 1, "name": "linh ❤️🌺"},
        {"id": 1010 ,"check": 0, "status": 1, "name": "LaBuBu"},
        {"id": 1011 ,"check": 0, "status": 1, "name": "MAY MẮN 🦋"},
        {"id": 1012 ,"check": 0, "status": 1, "name": "🐉 ĐẠI 🐉"},
        {"id": 1013 ,"check": 0, "status": 1, "name": "Robert Nguyễn 🥷💥"},
        {"id": 1014 ,"check": 0, "status": 1, "name": "Thawka Yee"},
        {"id": 1015 ,"check": 0, "status": 1, "name": "Thida Aung"},
        {"id": 1016 ,"check": 0, "status": 1, "name": "May Nwe Nhin Su"},
        {"id": 1017 ,"check": 0, "status": 1, "name": "Hline Phyu Yu Yi"},
        {"id": 1018 ,"check": 0, "status": 1, "name": "Win Phyu Yee U"},
        {"id": 1019 ,"check": 0, "status": 1, "name": "Mo"},
        {"id": 1020 ,"check": 0, "status": 1, "name": "☘️ 𝐍𝐠𝐨̣𝐜 𝐃𝐢𝐞̂̃𝐦 "},
        {"id": 1021 ,"check": 0, "status": 1, "name": "☘️ 𝓚𝓲𝓶 𝓝𝓰ọ𝓬 ☘️"},
        {"id": 1022 ,"check": 0, "status": 1, "name": "🦋 𝐁𝐚̉𝐨 🌸 𝐍𝐠𝐨̣𝐜 * 𝟤❤♡𝟥 🦋"},
        {"id": 1023 ,"check": 0, "status": 1, "name": "𝓚𝓱á𝓷𝓱 𝓛𝓲𝓷𝓱"},
        {"id": 1024 ,"check": 0, "status": 1, "name": "🍻 𝕿𝖎́𝖌𝖊𝖗 🍻"},
        {"id": 1025 ,"check": 0, "status": 1, "name": "Kim Tan"},
        {"id": 1026 ,"check": 0, "status": 1, "name": "NXP | Support"},
        {"id": 1027 ,"check": 0, "status": 1, "name": "☯ 𝕙ạ 𝕧𝕐 ☝️"},
        {"id": 1028 ,"check": 0, "status": 1, "name": "Hùng Trọng"}
        ]


# print(request_post(LINK_LIST_ROOM_DATA))
# print(request_post(LINK_CREATE_USER, {'chat_id': 123123, 'full_name': 'Hcneu e '}))
# print(request_post(LINK_DEPOSIT, {'chat_id': 123123, 'amount': 1000}))
# print(request_post(LINK_EXP, {'chat_id': 123123, 'exp': 100000}))
# print(request_post(LINK_CREATE_USER, {'chat_id': 123123, 'full_name': 'Hcneu e '}))

# print(request_post(LINK_CREATE_ROOM, {'chat_id': 123123, 'full_name': 'Gia Hiếu :D', 'room_balance': 960}))

def create_mutil_user():
    for i in range(len(name)):
        print(1000 + i, end=', ')
        print(request_post(LINK_CREATE_USER, {'chat_id': ID[i], 'full_name': name[i]}))

def deposit_exp_amount():
    for i in range(len(name)):
        print(request_post(LINK_DEPOSIT, {'chat_id': ID[i], 'amount': 1000000}))
        print(request_post(LINK_EXP, {'chat_id': ID[i], 'exp': 100000}))
        
def create_baucua_room(id, name, balance):
    request_post(LINK_CREATE_ROOM, {'chat_id': id, 'full_name': name, 'room_balance': balance})

def list_room_data():
    result = request_post(LINK_LIST_ROOM_DATA)
    return result

def bet_baucua(chat_id, bet_amount, bet_value, admin_id, round_number):
    def mini_bet():
        time.sleep(random.randint(3, 15))
        request_post(LINK_BET_BAUCUA,
                     {'chat_id': chat_id,
                      'bet_amount': bet_amount,
                      'bet_value': bet_value,
                      'admin_id': admin_id,
                      'round_number': round_number})
    threading.Thread(target=mini_bet).start()

def change_room_baucua_status(chat_id, dice_status):
    request_post(LINK_BAUCUA_STATUS,
                  {
                      'chat_id': chat_id,
                      'dice_status': dice_status,
                  })

def change_room_baucua_amount(chat_id, amount):
    request_post(LINK_CHANGE_ROOM_AMOUNT,
                  {
                      'chat_id': chat_id,
                      'amount': amount,
                  })

#----------------------------------------------#
LIST_CHAT_ID_REMOTE = []
# change_room_baucua_status(1000, 1)

a = {'chat_id': 1000,
     'dice_next': '',
     'dice_status': 0,
     'history': [[1, 1001, 2, 10.0, 10.0, '324', 0],
                 [2, 435514676, 3, 10.0, 10.0, '553', 1],
                 [4, 1001, 2, 10.0, 10.0, '264', 0],
                 [4, 1002, 1, 10.0, 0, '264', 0],
                 [4, 1001, 5, 10.0, 0, '264', 0],
                 [4, 1001, 6, 10.0, 10.0, '264', 0]],
     'last_dice': '264',
     'licence': 1738250346000,
     'password': '',
     'profit': 0.0,
     'room_amount': 450.0,
     'room_history': ['324', '553', '356', '264'],
     'room_id': 40114,
     'room_name': 'Keponakan Stanly🌱SEED 🐾 🌊',
     'room_status': 0,
     'round_number': 4,
     'stt': 4,
     'total_trade': 60.0
     }

delay_create_room = 0
entry = 0
while True:
    ts = int(date_to_timestamp(time_now()))
    list_room_fake = []
    all_room = list_room_data()['list']
    for room in all_room:
        #THIS fake ID not open room
        if room['chat_id'] < 10000:
            #check room have order fake
            if room['room_amount'] < 100:
                change_room_baucua_amount(room['chat_id'],
                                          random.randint(100 - int(room['room_amount']),
                                                         100 - int(room['room_amount']) + random.randint(0, 400)))

            if room['room_amount'] > 2000:
                change_room_baucua_amount(room['chat_id'],
                                          -1*random.randint(int(room['room_amount']) - 2000,
                                                         int(room['room_amount']) - 2000 + random.randint(0, 400)))
            is_old = False
            for his in room['history']:
                if his[5] == '' and his[6] == 0:
                    is_old = True
            if not is_old:
                list_room_fake.append(room['chat_id'])
                #fake room -> try order use DATA[1]
                number_order = random.randint(1, 6)
                order_select = []
                for i in range(number_order):
                    order_select.append(random.randint(1, 6))
                for order in order_select:
                    if room['chat_id'] == DATA[0]['id']:
                        idd = DATA[1]['id']
                    else:
                        idd = DATA[0]['id']
                    max_bet = int(room['room_amount']/30)
                    if max_bet < 1:
                        max_bet = 3
                    bet_amount = random.randint(1, max_bet)
                    if room['dice_status'] == 0:
                        bet_baucua(DATA[1]['id']    ,
                                   bet_amount,
                                   order,
                                   room['chat_id'],
                                   room['round_number'] + 1)

            #fake room, set time next action
            #{"id": 1028 ,"check": 0, "status": 1, "name": "Hùng Trọng"}
            for i in range(len(DATA)):
                if room['chat_id'] == DATA[i]['id']:
                    if DATA[i]['check'] == 0:
                        #wait to click countdown
                        DATA[i]['check'] = ts + random.randint(15, 30)
                    elif DATA[i]['check'] < ts:
                        if room['dice_status'] == 0:
                            #click countdown
                            change_room_baucua_status(room['chat_id'], 1)
                            DATA[i]['check'] = ts + random.randint(10, 15)
                            DATA[i]['status'] = 3
                        else:
                            #click roll
                            if room['dice_status'] == 3:
                                round_number = room['round_number']
                                real_bet = [0, 0, 0, 0, 0, 0]
                                fake_bet = [0, 0, 0, 0, 0, 0]
                                real_win = 0
                                for h in room['history']:
                                    if h[0] == (round_number + 1) and h[5] == '':
                                        if h[6] == 1:
                                            real_bet[h[2] - 1] += h[3]
                                        else:
                                            fake_bet[h[2] - 1] += h[3]
                                    if h[6] == 1 and h[5] != '':
                                        real_win += h[4]
                                    
                                #set next trade

                                
                                change_room_baucua_status(room['chat_id'], 4)
                                DATA[i]['check'] = 0
                                DATA[i]['status'] = 1

        



    if ts > delay_create_room:
        delay_create_room = ts + random.randint(10, 20)*60
        for admin in DATA:
            if admin['id'] not in list_room_fake:
                create_baucua_room(admin['id'], admin['name'], random.randint(100, 700))
    # break
    time.sleep(random.randint(3, 10))