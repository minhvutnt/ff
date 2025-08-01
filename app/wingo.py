import random
import sqlite3
import json
import threading
from app.lib_bool import is_int, is_float
from app.timestamp import *
from threading import Thread, Lock
from flask_socketio import SocketIO, emit, join_room, leave_room, close_room, rooms, disconnect
from app.socketio import socketio
from app.glo import *
from app.database_lib import *
from app.db_user_wallet import *
from app.LANGUAGE import *
from app.referrer import ref_money
from app.db_promotion import *
name_db_wingo = 'db_wingo.db'


def create_db():
    try:
        conn = sqlite3.connect(name_db_wingo)
        c = conn.cursor()

        try:
            user_table = '''CREATE TABLE {}(stt INTEGER PRIMARY KEY AUTOINCREMENT,
                                            roundnumber int,
                                            number char[5])'''.format('WINGO')
            c.execute(user_table)
        except Exception as e:
            print("Table WINGO: ", str(e))

        try:
            user_table = '''CREATE TABLE {}(stt INTEGER PRIMARY KEY AUTOINCREMENT,
                                            roundnumber int, 
                                            chat_id int,
                                            ordertime int,
                                            bet_value char[1],
                                            amount float,
                                            result char[1],
                                            profit float,
                                            tax float,
                                            wallet int
                                            )'''.format('MY_WINGO')
            c.execute(user_table)
        except Exception as e:
            print("Table MY_WINGO: ", str(e))

        conn.commit()
        conn.close()
        print("create db ok")
    except Exception as e:
        print("Table: ", str(e))


create_db()

LIST_WINGO = []
LIST_MY_WINGO = []

def local_check_wingo(wingo):
    DATA_WINGO('CHECK',
                 [
                     1 if len(LIST_WINGO) == 0 else (LIST_WINGO[-1].stt + 1),
                     wingo['roundnumber'],
                     wingo['number'],
                 ])


class DATA_WINGO:
    def __init__(self, status, jsdata):
        if status == 'CHECK':
            self.stt = jsdata[0]
            self.roundnumber = jsdata[1]
            self.number = jsdata[2]
            LIST_WINGO.append(self)
        elif status == 'INSERT':
            wingo = {
                'roundnumber': jsdata['roundnumber'],
                'number': jsdata['number']
            }
            result = threading_wingo('INSERT', wingo=wingo)
            if result:
                local_check_wingo(wingo)

    @property
    def info(self):
        return {
            'stt': self.stt,
            'roundnumber': self.roundnumber,
            'number': self.number
        }


def _START_DATA_WINGO_():
    conn = sqlite3.connect(name_db_wingo)
    cursor = conn.cursor()
    all_user = check_table(cursor, "WINGO")
    conn.close()
    for user in all_user:
        DATA_WINGO('CHECK', user)


_START_DATA_WINGO_()

# ====================================[                  Save data                 ]====================================
lock_wingo = Lock()


def threading_wingo(status, wingo=None, my_wingo=None):
    lock_wingo.acquire()
    conn = sqlite3.connect(name_db_wingo)
    cursor = conn.cursor()
    try:
        if wingo is not None:
            if status == 'INSERT':
                insert_log = """Insert INTO WINGO (
                                        roundnumber,
                                        number
                                        ) values(?, ?);"""
                info_update = (
                    wingo["roundnumber"],
                    wingo["number"])
                cursor.execute(insert_log, info_update)
        elif my_wingo is not None:
            if status == 'UPDATE':
                update_trade = """UPDATE MY_WINGO SET 
                                        roundnumber=?,
                                        chat_id=?,
                                        ordertime=?,
                                        bet_value=?,
                                        amount=?,
                                        result=?,
                                        profit=?,
                                        tax=?,
                                        wallet=?
                                         WHERE stt=?"""
                info_update = (
                    my_wingo["roundnumber"],
                    my_wingo["chat_id"],
                    my_wingo["ordertime"],
                    my_wingo["bet_value"],
                    my_wingo["amount"],
                    my_wingo["result"],
                    my_wingo["profit"],
                    my_wingo["tax"],
                    my_wingo["wallet"],
                    my_wingo["stt"]
                )
                cursor.execute(update_trade, info_update)
            elif status == 'INSERT':
                insert_log = """Insert INTO MY_WINGO (
                                        roundnumber,
                                        chat_id,
                                        ordertime,
                                        bet_value,
                                        amount,
                                        result,
                                        profit,
                                        tax,
                                        wallet
                                        ) values(?, ?, ?, ?, ?, ?, ?, ?, ?);"""
                info_update = (
                    my_wingo['roundnumber'],
                    my_wingo['chat_id'],
                    my_wingo['ordertime'],
                    my_wingo['bet_value'],
                    my_wingo['amount'],
                    my_wingo['result'],
                    my_wingo['profit'],
                    my_wingo['tax'],
                    my_wingo['wallet']
                )
                cursor.execute(insert_log, info_update)

        result = True
    except Exception as e:
        result = False
        print("DATA WINGO  ERR: ", e)

    conn.commit()
    conn.close()
    lock_wingo.release()
    return result


def local_check_my_wingo(my_wingo):
    DATA_MY_WINGO('CHECK',
                    [
                        my_wingo['stt'],
                        my_wingo['roundnumber'],
                        my_wingo['chat_id'],
                        my_wingo['ordertime'],
                        my_wingo['bet_value'],
                        my_wingo['amount'],
                        my_wingo['result'],
                        my_wingo['profit'],
                        my_wingo['tax'],
                        my_wingo['wallet']
                    ])
def info_mywingo_by_stt(stt):
    result = None
    for wingo in LIST_MY_WINGO:
        if wingo.stt == stt:
            result = wingo
            break
    return result

class DATA_MY_WINGO:
    def __init__(self, status, jsdata):
        if status == 'CHECK':
            is_old = False
            for i in range(len(LIST_MY_WINGO)):
                if jsdata[0] == LIST_MY_WINGO[i].stt:
                    is_old = True
                    LIST_MY_WINGO[i].roundnumber = jsdata[1]
                    LIST_MY_WINGO[i].chat_id = jsdata[2]
                    LIST_MY_WINGO[i].ordertime = jsdata[3]
                    LIST_MY_WINGO[i].bet_value = jsdata[4]
                    LIST_MY_WINGO[i].amount = jsdata[5]
                    LIST_MY_WINGO[i].result = jsdata[6]
                    LIST_MY_WINGO[i].profit = jsdata[7]
                    LIST_MY_WINGO[i].tax = jsdata[8]
                    LIST_MY_WINGO[i].wallet = jsdata[9]
            if not is_old:
                self.stt = jsdata[0]
                self.roundnumber = jsdata[1]
                self.chat_id = jsdata[2]
                self.ordertime = jsdata[3]
                self.bet_value = jsdata[4]
                self.amount = jsdata[5]
                self.result = jsdata[6]
                self.profit = jsdata[7]
                self.tax = jsdata[8]
                self.wallet = jsdata[9]
                LIST_MY_WINGO.append(self)

        elif status == 'INSERT':
            mywingo = {
                'stt': 1 if len(LIST_MY_WINGO) == 0 else LIST_MY_WINGO[-1].stt + 1,
                'roundnumber': jsdata['roundnumber'],
                'chat_id': jsdata['chat_id'],
                'ordertime': jsdata['ordertime'],
                'bet_value': jsdata['bet_value'],
                'amount': jsdata['amount'],
                'result': jsdata['result'],
                'profit': jsdata['profit'],
                'tax': jsdata['tax'],
                'wallet': jsdata['wallet']
            }
            result = threading_wingo('INSERT', my_wingo=mywingo)
            if result:
                local_check_my_wingo(mywingo)
        elif status == 'UPDATE':
            week = info_mywingo_by_stt(jsdata['stt'])
            mywingo = {
                'stt': jsdata['stt'],
                'roundnumber': jsdata['roundnumber'] if 'roundnumber' in jsdata else week.roundnumber,
                'chat_id': jsdata['chat_id'] if 'chat_id' in jsdata else week.chat_id,
                'ordertime': jsdata['ordertime'] if 'ordertime' in jsdata else week.ordertime,
                'bet_value': jsdata['bet_value'] if 'bet_value' in jsdata else week.bet_value,
                'amount': jsdata['amount'] if 'amount' in jsdata else week.amount,
                'result': jsdata['result'] if 'result' in jsdata else week.result,
                'profit': jsdata['profit'] if 'profit' in jsdata else week.profit,
                'tax': jsdata['tax'] if 'tax' in jsdata else week.tax,
                'wallet': jsdata['wallet'] if 'wallet' in jsdata else week.wallet
            }
            result = threading_wingo('UPDATE', my_wingo=mywingo)
            if result:
                local_check_my_wingo(mywingo)

    @property
    def info(self):
        return {
            'stt': self.stt,
            'roundnumber': self.roundnumber,
            'chat_id': self.chat_id,
            'ordertime': self.ordertime,
            'bet_value': self.bet_value,
            'amount': self.amount,
            'result': self.result,
            'profit': self.profit,
            'tax': self.tax,
            'wallet': self.wallet
        }


def _START_DATA_MY_WINGO_():
    conn = sqlite3.connect(name_db_wingo)
    cursor = conn.cursor()
    all_user = check_table(cursor, "MY_WINGO")
    conn.close()
    for user in all_user:
        DATA_MY_WINGO('CHECK', user)


_START_DATA_MY_WINGO_()

def wingo_roundnumber(dt):
    return '{}{}{}{}'.format(dt.year, str(dt.month).rjust(2, '0'), str(dt.day).rjust(2, '0'), str(dt.hour*60 + dt.minute).rjust(4, '0'))

def wingo_next_roundnumber(dt):
    dt = timestamp_to_date(date_to_timestamp(dt) + 60)
    return '{}{}{}{}'.format(dt.year, str(dt.month).rjust(2, '0'), str(dt.day).rjust(2, '0'), str(dt.hour*60 + dt.minute).rjust(4, '0'))

def wingo_round_to_time(roundnumber):
    roundnumber = str(roundnumber)
    total_minutes = int(roundnumber[-4:])
    hours = total_minutes // 60
    minutes = total_minutes % 60
    year = roundnumber[:4]
    month = roundnumber[4:6]
    day = roundnumber[6:8]
    datetime_str = '{}/{}/{} {}:{}:{}'.format(year, month, day, hours, minutes, 00)
    datetime_object = datetime.strptime(datetime_str, "%Y/%m/%d %H:%M:%S")
    return datetime_object

def _NEW_DATA_WINGO_():
    if not LIST_WINGO:
        for i in range(30*1400):
            tsnow = date_to_timestamp(time_now())
            day = int(tsnow * 1000) - (30*1400*60 - (i + 1)*60)*1000
            dt = datetime.fromtimestamp(day/1000)
            dt = dt.replace(second=0, microsecond=0)

            roundnumber = wingo_roundnumber(dt)

            DATA_WINGO('INSERT', {
                'roundnumber': roundnumber,
                'number': str(random.randint(0, 99999)).rjust(5, '0')
            })

_NEW_DATA_WINGO_()

def wingo_history(page):
    result, last_page, next_page, max_page = split_page(LIST_WINGO, page)
    data = []
    for p in result:
        data.append(p.info)
    if result:
        return {
            'status': True,
            'data': data,
            'last_page': last_page,
            'next_page': next_page,
            'max_page': max_page,
            'page': int(page) + 1,
            'last_result': LIST_WINGO[-1].number,
            'roundnumber': LIST_WINGO[-1].roundnumber,
            'next_roundnumber': wingo_next_roundnumber(time_now()),
        }
    else:
        return None

def wingo_my_history(chat_id, page):
    my_his = []
    for his in LIST_MY_WINGO:
        if his.chat_id == chat_id:
            my_his.append(his.info)
    result, last_page, next_page, max_page = split_page(my_his, page)
    return {
        'status': True,
        'data': result,
        'last_page': last_page,
        'next_page': next_page,
        'max_page': max_page,
        'page': int(page) + 1
    }
def next_result(data):
    return str(random.randint(0, 99999)).rjust(5, '0')

def bet_wingo(chat_id, bet_value, amount, roundnumber, by_wallet):
    result = None
    tn = time_now()

    user = db_user_info_emit(chat_id)

    user_amount = None
    promotion_wallet = None
    if by_wallet == '0': user_amount = user['usdt_amount']
    else:
        for w in user['promotion_amount']:
            if str(w['stt']) == str(by_wallet):
                user_amount = w['amount']
                promotion_wallet = w
    if not is_float(amount) or (is_float(amount) and float(amount) <= 0):
        result = {'status': False, 'msg': 'Giá trị cược không hợp lệ'}
    elif roundnumber != wingo_next_roundnumber(tn):
        result = {'status': False, 'msg': 'Kỳ xổ đã kết thúc'}
    elif tn.second >= 55:
        result = {'status': False, 'msg': 'Hết thời gian đặt cược'}
    elif bet_value not in ['B', 'S', 'G', 'R', 'P', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
        result = {'status': False, 'msg': 'Loại cược không hợp lệ'}
    else:
        if user is None:
            result = {'status': False, 'msg': 'Người dùng không tồn tại'}
        else:
            amount = int(float(amount)*100)/100
            if user_amount < amount:
                result = {'status': False, 'msg': 'Ví không đủ số dư'}
            else:
                exp_per_dollar = EXP_TABLE['wingo_bet_1']['exp']
                exp = int(amount)*exp_per_dollar

                ticket_per_001 = EXP_TABLE['wingo_bet_0_01']['ticket']
                ticket = amount*100*ticket_per_001

                if promotion_wallet is None or user.is_mkt == 0:
                    db_user_update_balance(chat_id, None, 'WINGO', amount*-1)
                else:
                    my_promotion_trade(promotion_wallet['stt'],
                                       chat_id,
                                       amount*-1,
                                       'WINGO')
                DATA_USER('UPDATE', {
                    'chat_id': chat_id,
                    'exp': user['exp'] + exp,
                    'tickets': user['tickets'] + ticket,
                })


                tax = int(amount*REF_FEE[1]['fee']*10000)/1000000
                data = {
                    'roundnumber': roundnumber,
                    'chat_id': chat_id,
                    'ordertime': int(date_to_timestamp(tn)*1000),
                    'bet_value': bet_value,
                    'amount': amount,
                    'result': '',
                    'profit': 0,
                    'tax': tax,
                    'wallet': promotion_wallet['stt'] if promotion_wallet is not None else 0
                }
                DATA_MY_WINGO('INSERT', data)
                ref_money(user['uid'], amount, 'WINGO')
                result = {'status': True, 'data': data}

                uinfo = db_user_info_emit(chat_id)
                uinfo.update({'level': LEVEL_EXP})
                socketio.emit('return_user_info_{}'.format(chat_id),
                              uinfo
                              )
    return result

def threading_round_wingo():
    ts = time_now()
    if LIST_WINGO[-1].roundnumber != wingo_roundnumber(ts):
        last_round_time = wingo_round_to_time(LIST_WINGO[-1].roundnumber) #202502050718
        while True:
            next_round_time = timestamp_to_date(date_to_timestamp(last_round_time) + 60)
            if next_round_time > ts:
                break
            else:
                roundnumber = wingo_roundnumber(next_round_time)
                last_round_time = next_round_time
                #check bet result
                rrrr = next_result('data')
                DATA_WINGO('INSERT', {
                    'roundnumber': roundnumber,
                    'number': rrrr
                })
                #===================================== check trade
                list_trade = []
                for i in range(len(LIST_MY_WINGO)):
                    if LIST_MY_WINGO[i].roundnumber == roundnumber and LIST_MY_WINGO[i].result == '':
                        list_trade.append(LIST_MY_WINGO[i])

                list_user = []
                for trade in list_trade:
                    if trade.bet_value == 'B' and int(rrrr[0]) >= 5:
                        p = 2
                    elif trade.bet_value == 'S' and int(rrrr[0]) <= 4:
                        p = 2
                    elif trade.bet_value == 'G' and rrrr[0] in ['1', '3', '7', '9']:
                        p = 2
                    elif trade.bet_value == 'R' and rrrr[0] in ['2', '4', '6', '8']:
                        p = 2
                    elif trade.bet_value == 'G' and rrrr[0] in ['5']:
                        p = 1.5
                    elif trade.bet_value == 'R' and rrrr[0] in ['0']:
                        p = 1.5
                    elif trade.bet_value == 'P' and rrrr[0] in ['0', '5']:
                        p = 4.5
                    elif is_int(trade.bet_value) and int(trade.bet_value) == int(rrrr[0]):
                        p = 9
                    else:
                        p = 0

                    profit = round((trade.amount - trade.tax)*p, 2)
                    DATA_MY_WINGO('UPDATE',{
                        'stt': trade.stt,
                        'result': rrrr[0],
                        'profit': profit
                    })
                    if profit > 0:
                        #check wallet -> add amount
                        if trade.wallet == 0:
                            db_user_update_balance(trade.chat_id, None, 'WINGO', profit)
                        else:
                            my_promotion_trade(trade.wallet, trade.chat_id, profit, 'WINGO')
                            uinfo = db_user_info_emit(trade.chat_id)
                            uinfo.update({'level': LEVEL_EXP})
                            socketio.emit('return_user_info_{}'.format(trade.chat_id),
                                          uinfo
                                          )


                    if trade.chat_id not in list_user:
                        list_user.append(trade.chat_id)

                for user in list_user:
                    data = wingo_my_history(user,
                                            0)
                    socketio.emit('return_wingo_my_history_{}'.format(user),
                                  data)

        rr = wingo_history(0)
        if rr is not None:
            socketio.emit('return_wingo_history',
                          rr)



threading_round_wingo()
