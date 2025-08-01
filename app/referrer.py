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

name_db_referrer = 'db_referrer.db'


def create_db():
    try:
        conn = sqlite3.connect(name_db_referrer)
        c = conn.cursor()

        try:
            user_table = '''CREATE TABLE {}(stt INTEGER PRIMARY KEY AUTOINCREMENT,
                                            chat_id int,
                                            uid int,
                                            f0 int,
                                            ref_level int,
                                            day int
                                            )'''.format('REFERRER')
            c.execute(user_table)
        except Exception as e:
            print("Table REFERRER: ", str(e))

        try:
            user_table = '''CREATE TABLE {}(stt INTEGER PRIMARY KEY AUTOINCREMENT,
                                            chat_id int, 
                                            uid int, 
                                            from_uid int,
                                            percent float,
                                            amount float,
                                            ref_amount float,
                                            ref_level int,
                                            ref_type char[50],
                                            day int
                                            )'''.format('REFERRER_HISTORY')
            c.execute(user_table)
        except Exception as e:
            print("Table REFERRER: ", str(e))

        conn.commit()
        conn.close()
        print("create db ok")
    except Exception as e:
        print("Table: ", str(e))


create_db()

LIST_REFERRER = []
LIST_REFERRER_HISTORY = []


def local_check_referrer(ref):
    DATA_REFERRER('CHECK',
               [
                   ref['stt'],
                   ref['chat_id'],
                   ref['uid'],
                   ref['f0'],
                   ref['ref_level'],
                   ref['day']
               ])


class DATA_REFERRER:
    def __init__(self, status, jsdata):
        if status == 'CHECK':
            is_old = False
            for i in range(len(LIST_REFERRER)):
                if jsdata[0] == LIST_REFERRER[i].stt:
                    is_old = True
                    LIST_REFERRER[i].chat_id = jsdata[1]
                    LIST_REFERRER[i].uid = jsdata[2]
                    LIST_REFERRER[i].f0 = jsdata[3]
                    LIST_REFERRER[i].ref_level = jsdata[4]
                    LIST_REFERRER[i].day = jsdata[5]
            if not is_old:
                self.stt = jsdata[0]
                self.chat_id = jsdata[1]
                self.uid = jsdata[2]
                self.f0 = jsdata[3]
                self.ref_level = jsdata[4]
                self.day = jsdata[5]
                LIST_REFERRER.append(self)
        elif status == 'INSERT':
            ref = {
                'stt': (LIST_REFERRER[-1].stt + 1) if LIST_REFERRER else 1,
                'chat_id': jsdata['chat_id'],
                'uid': jsdata['uid'],
                'f0': jsdata['f0'],
                'ref_level': jsdata['ref_level'],
                'day': jsdata['day']
            }
            result = threading_referrer('INSERT', ref=ref)
            if result:
                local_check_referrer(ref)
        elif status == 'UPDATE':
            ref_info = info_referrer_stt(jsdata['stt'])
            ref = {
                'stt': ref_info.stt,
                'chat_id': ref_info.chat_id,
                'uid': jsdata['uid'] if 'uid' in jsdata else ref_info.uid,
                'f0': jsdata['f0'] if 'f0' in jsdata else ref_info.f0,
                'ref_level': jsdata['ref_level'] if 'ref_level' in jsdata else ref_info.ref_level,
                'day': jsdata['day'] if 'day' in jsdata else ref_info.day
            }
            result = threading_referrer('UPDATE', ref=ref)
            if result:
                local_check_referrer(ref)

    @property
    def info(self):
        return {
            'stt': self.stt,
            'chat_id': self.chat_id,
            'uid': self.uid,
            'f0': self.f0,
            'ref_level': self.ref_level,
            'day': self.day
        }


def _START_DATA_REFERRER_():
    conn = sqlite3.connect(name_db_referrer)
    cursor = conn.cursor()
    all_user = check_table(cursor, "REFERRER")
    conn.close()
    for user in all_user:
        DATA_REFERRER('CHECK', user)


_START_DATA_REFERRER_()


def info_referrer_stt(stt):
    for user in LIST_REFERRER:
        if user.stt == stt:
            return user
    else:
        return None

#============================================================

def local_check_referrer_history(ref):
    DATA_REFERRER_HISTORY('CHECK',
               [
                   ref['stt'],
                   ref['chat_id'],
                   ref['uid'],
                   ref['from_uid'],
                   ref['percent'],
                   ref['amount'],
                   ref['ref_amount'],
                   ref['ref_level'],
                   ref['ref_type'],
                   ref['day']
               ])

# stt INTEGER PRIMARY KEY AUTOINCREMENT,
# chat_id int,
# uid int,
# from_uid int,
# percent float,
# ref_level int,
# ref_type char[50]
class DATA_REFERRER_HISTORY:
    def __init__(self, status, jsdata):
        if status == 'CHECK':
            is_old = False
            for i in range(len(LIST_REFERRER_HISTORY)):
                if jsdata[0] == LIST_REFERRER_HISTORY[i].stt:
                    is_old = True
                    LIST_REFERRER_HISTORY[i].chat_id = jsdata[1]
                    LIST_REFERRER_HISTORY[i].uid = jsdata[2]
                    LIST_REFERRER_HISTORY[i].from_uid = jsdata[3]
                    LIST_REFERRER_HISTORY[i].percent = jsdata[4]
                    LIST_REFERRER_HISTORY[i].amount = jsdata[5]
                    LIST_REFERRER_HISTORY[i].ref_amount = jsdata[6]
                    LIST_REFERRER_HISTORY[i].ref_level = jsdata[7]
                    LIST_REFERRER_HISTORY[i].ref_type = jsdata[8]
                    LIST_REFERRER_HISTORY[i].day = jsdata[9]
            if not is_old:
                self.stt = jsdata[0]
                self.chat_id = jsdata[1]
                self.uid = jsdata[2]
                self.from_uid = jsdata[3]
                self.percent = jsdata[4]
                self.amount = jsdata[5]
                self.ref_amount = jsdata[6]
                self.ref_level = jsdata[7]
                self.ref_type = jsdata[8]
                self.day = jsdata[9]
                LIST_REFERRER_HISTORY.append(self)
        elif status == 'INSERT':
            ref = {
                'stt': (LIST_REFERRER_HISTORY[-1].stt + 1) if LIST_REFERRER_HISTORY else 1,
                'chat_id': jsdata['chat_id'],
                'uid': jsdata['uid'],
                'from_uid': jsdata['from_uid'],
                'percent': jsdata['percent'],
                'amount': jsdata['amount'],
                'ref_amount': jsdata['ref_amount'],
                'ref_level': jsdata['ref_level'],
                'ref_type': jsdata['ref_type'],
                'day': jsdata['day']
            }
            result = threading_referrer('INSERT', ref_history=ref)
            if result:
                local_check_referrer_history(ref)
        elif status == 'UPDATE':
            ref_info = info_referrer_history_stt(jsdata['stt'])
            ref = {
                'stt': ref_info.stt,
                'chat_id': ref_info.chat_id,
                'uid': jsdata['uid'] if 'uid' in jsdata else ref_info.uid,
                'from_uid': jsdata['from_uid'] if 'from_uid' in jsdata else ref_info.from_uid,
                'percent': jsdata['percent'] if 'percent' in jsdata else ref_info['percent'],
                'amount': jsdata['amount'] if 'amount' in jsdata else ref_info['amount'],
                'ref_amount': jsdata['ref_amount'] if 'ref_amount' in jsdata else ref_info['ref_amount'],
                'ref_level': jsdata['ref_level'] if 'ref_level' in jsdata else ref_info['ref_level'],
                'ref_type': jsdata['ref_type'],
                'day': jsdata['day'] if 'day' in jsdata else ref_info['day']

            }
            result = threading_referrer('UPDATE', ref_history=ref)
            if result:
                local_check_referrer_history(ref)

    @property
    def info(self):
        return {
            'stt': self.stt,
            'chat_id': self.chat_id,
            'uid': self.uid,
            'from_uid': self.from_uid,
            'percent': self.percent,
            'amount': self.amount,
            'ref_amount': self.ref_amount,
            'ref_level': self.ref_level,
            'ref_type': self.ref_type,
            'day': self.day
        }


def _START_DATA_REFERRER_HISTORY_():
    conn = sqlite3.connect(name_db_referrer)
    cursor = conn.cursor()
    all_user = check_table(cursor, "REFERRER_HISTORY")
    conn.close()
    for user in all_user:
        DATA_REFERRER_HISTORY('CHECK', user)


_START_DATA_REFERRER_HISTORY_()


def info_referrer_history_stt(stt):
    for user in LIST_REFERRER_HISTORY:
        if user.stt == stt:
            return user
    else:
        return None
# ====================================[                  Save data                 ]====================================
lock_ref = Lock()


def threading_referrer(status, ref=None, ref_history=None):
    lock_ref.acquire()
    conn = sqlite3.connect(name_db_referrer)
    cursor = conn.cursor()
    try:
        if ref is not None:
            if status == 'UPDATE':
                update_trade = """UPDATE REFERRER SET 
                                        chat_id=?,
                                        uid=?,
                                        f0=?,
                                        ref_level=?,
                                        day=?
                                         WHERE stt=?"""
                info_update = (
                    ref["chat_id"],
                    ref["uid"],
                    ref["f0"],
                    ref["ref_level"],
                    ref["day"],
                    ref["stt"]
                )
                cursor.execute(update_trade, info_update)
            elif status == 'INSERT':
                insert_log = """Insert INTO REFERRER (
                                        chat_id,
                                        uid,
                                        f0,
                                        ref_level,
                                        day
                                        ) values(?, ?, ?, ?, ?);"""
                info_update = (
                    ref['chat_id'],
                    ref['uid'],
                    ref['f0'],
                    ref['ref_level'],
                    ref['day']
                )
                cursor.execute(insert_log, info_update)
        elif ref_history is not None:
            if status == 'UPDATE':
                update_trade = """UPDATE REFERRER_HISTORY SET 
                                        chat_id=?,
                                        uid=?,
                                        from_uid=?,
                                        percent=?,
                                        amount=?,
                                        ref_amount=?,
                                        ref_level=?,
                                        ref_type=?,
                                        day=?
                                         WHERE stt=?"""
                info_update = (
                    ref_history["chat_id"],
                    ref_history["uid"],
                    ref_history["from_uid"],
                    ref_history["percent"],
                    ref_history["amount"],
                    ref_history["ref_amount"],
                    ref_history["ref_level"],
                    ref_history["ref_type"],
                    ref_history["day"],
                    ref_history["stt"]
                )
                cursor.execute(update_trade, info_update)
            elif status == 'INSERT':
                insert_log = """Insert INTO REFERRER_HISTORY (
                                        chat_id,
                                        uid,
                                        from_uid,
                                        percent,
                                        amount,
                                        ref_amount,
                                        ref_level,
                                        ref_type,
                                        day
                                        ) values(?, ?, ?, ?, ?, ?, ?, ?, ?);"""
                info_update = (
                    ref_history['chat_id'],
                    ref_history['uid'],
                    ref_history['from_uid'],
                    ref_history['percent'],
                    ref_history['amount'],
                    ref_history['ref_amount'],
                    ref_history['ref_level'],
                    ref_history['ref_type'],
                    ref_history['day']
                )
                cursor.execute(insert_log, info_update)
        result = True
    except Exception as e:
        result = False
        print("DATA REFERRER ERR: ", e)

    conn.commit()
    conn.close()
    lock_ref.release()
    return result

def add_ref(chat_id, uid):
    result = None
    if not is_int(uid):
        result = {'status': False, 'msg': 'UID không đúng'}
    else:
        uid = int(uid)

        user = None
        user_f0 = None
        for u in LIST_USER:
            if u.uid == uid:
                user_f0 = u
            if u.chat_id == chat_id:
                user = u
            if user is not None and user_f0 is not None:
                break
        if user_f0 is None:
            result = {
                'status': False,
                'msg': 'UID người giới thiệu không tồn tại'
            }
        elif user == user_f0:
            result = {
                'status': False,
                'msg': 'UID của bạn'
            }
        else:
            is_new = True
            data_my_ref = get_ref(chat_id, full=True)['ref']

            all_ref = []
            for i in range(1, 11):
                for u in data_my_ref['f' + str(i)]:
                    all_ref.append(u['uid'])
            for ref in LIST_REFERRER:
                if ref.chat_id == chat_id:
                    is_new = False


                    if ref.uid == uid:
                        result = {'status': False,
                                  'msg': 'Lỗi phân cấp, đây là cấp dưới trực tiếp của bạn'}
                    elif uid in all_ref:
                        result = {'status': False,
                                  'msg': 'Mã giới thiệu thuộc hệ thống của bạn'}
                    elif ref.f0 is None:
                        DATA_REFERRER('UPDATE', {
                            'stt': ref.stt,
                            'f0': user_f0.uid,
                            'day': int(date_to_timestamp(time_now()) * 1000)
                        })
                        result = {'status': True,
                                  'msg': 'Đã đăng ký mã giới thiệu {} của {}'.format(uid, user_f0.full_name)}
                    else:
                        result = {'status': False,
                                  'msg': ''}
                    break
            if is_new:
                if uid not in all_ref:
                    DATA_REFERRER('INSERT', {
                        'chat_id': user.chat_id,
                        'uid': user.uid,
                        'f0': uid,
                        'ref_level': 0,
                        'day': int(date_to_timestamp(time_now())*1000)
                    })
                    result = {'status': True,
                              'msg': 'Đã đăng ký mã giới thiệu {} của {}'.format(uid, user.full_name)}
                else:
                    result = {'status': False,
                              'msg': 'Mã giới thiệu thuộc hệ thống của bạn.'}
    return result


def get_ref(chat_id, fnum=0, fpage=0, full=False):
    result = None
    for ref in LIST_REFERRER:
        if ref.chat_id == chat_id:
            result = ref.info
            break
    if result is None:
        user = None
        for u in LIST_USER:
            if u.chat_id == chat_id:
                user = u
                break
        result = {
            'chat_id': chat_id,
            'uid': user.uid,
            'f0': None,
            'ref_level': 0,
            'day': None
        }
        DATA_REFERRER('INSERT', result)
    data = {
        'f1': [],
        'f2': [],
        'f3': [],
        'f4': [],
        'f5': [],
        'f6': [],
        'f7': [],
        'f8': [],
        'f9': [],
        'f10': [],
    }
    #data {uid, name, balance}
    list_ref_uid = [[], [], [], [], [], [], [], [], [], []]
    #f1
    for ref in LIST_REFERRER:
        if ref.f0 == result['uid']:
            u = info_by_chat_id(ref.chat_id)
            d = {'stt': ref.stt,
            'chat_id': ref.chat_id,
            'uid': ref.uid,
            'f0': ref.f0,
            'ref_level': ref.ref_level,
            'amount': u.usdt_amount,
            'full_name': u.full_name,
            'level': 1}

            data['f1'].append(d)
            list_ref_uid[0].append(ref.uid)
    # f2 - 10
    for i in range(2, 11):
        for ref in LIST_REFERRER:
            if ref.f0 in list_ref_uid[i - 2]:
                u = info_by_chat_id(ref.chat_id)
                d = {'stt': ref.stt,
                     'chat_id': ref.chat_id,
                     'uid': ref.uid,
                     'f0': ref.f0,
                     'ref_level': ref.ref_level,
                     'amount': u.usdt_amount,
                     'full_name': u.full_name,
                     'ref': [],
                     'level': i}

                data['f' + str(i)].append(d)
                list_ref_uid[i - 1].append(ref.uid)
    return {'status': True,
            'data': result,
            'ref': data}
def ref_money(uid, trade_amount, reftype):
    f = [None, None, None, None, None, None, None, None, None, None, None]

    for ref in LIST_REFERRER:
        if ref.uid == uid:
            f[0] = ref.info
            break
    for i in range(1, 11):
        for ref in LIST_REFERRER:
            if f[i - 1] is not None and ref.uid == f[i - 1]['f0']:
                f[i] = ref.info
                break
    this_ts = int(date_to_timestamp(time_now())*1000)
    user = f[1:]
    for i in range(len(user)):
        if f[i] is not None:
            if reftype == 'INVEST':
                percent = REFERRAL_INVEST[str(f[i]['ref_level'])][i - 1]
            else:
                percent = REFERRAL[str(f[i]['ref_level'])][i - 1]
            if i - 1 != -1:
                ref_amount = round(trade_amount * percent/100, 7)
                if ref_amount != 0:
                    db_user_update_balance(f[i]['chat_id'], f[0]['chat_id'], 'referrer', ref_amount)
                    DATA_REFERRER_HISTORY('INSERT', {
                        'chat_id': f[i]['chat_id'],
                        'uid': f[i]['uid'],
                        'from_uid': uid,
                        'percent': percent,
                        'amount': trade_amount,
                        'ref_amount': ref_amount,
                        'ref_level': f[i]['ref_level'],
                        'ref_type': reftype + ' F' + str(i),
                        'day': this_ts
                    })


def get_ref_history(chat_id, page):
    result = []
    for ref in LIST_REFERRER_HISTORY:
        if ref.chat_id == chat_id:
            result.append(ref.info)

    result, last_page, next_page, max_page = split_page(result, page, per_page=20)
    return {
        'status': True,
        'data': result,
        'last_page': last_page,
        'next_page': next_page,
        'page': page + 1,
        'max_page': max_page,

    }
#
# lastd = 1000220
# for u in LIST_USER:
#     a =add_ref(u.chat_id, lastd)
#     lastd = u.uid
#     print(a['msg'])
# #
# for i in LIST_REFERRER:
#     print(i.info)
#
# get_ref(435514676, fnum=0, fpage=0, full=False)

# ref_money(1000247, random.randint(1, 1000)/100, 'WINGO')
# ref_money(1000247, random.randint(1, 1000)/100, 'WINGO')
# ref_money(1000247, random.randint(1, 1000)/100, 'WINGO')
# for re in LIST_REFERRER_HISTORY:
#     print(re.chat_id, re.uid)