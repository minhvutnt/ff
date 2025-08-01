import random
from enum import Enum

BOT_LINK = 'https://t.me/FreeFunBbot'
SOCKETIO_URL = 'http://127.0.0.1:80'
# SOCKETIO_URL = 'https://api.sdaufbasudfbuasdfbs.click'
PROJECT_NAME = 'WINLUCK'
TRUE_TEST = True
LOTTERY_RATE = [
    {
        'from': 0,
        'to': 9885,
        'pay': int(0.0005*26000)
    },
    {
        'from': 9886,
        'to': 9985,
        'pay': int(0.0051*26000)
    },
    {
        'from': 9986,
        'to': 9993,
        'pay': int(0.0513*26000)
    },
    {
        'from': 9994,
        'to': 9997,
        'pay': int(0.5129*26000)
    },
    {
        'from': 9998,
        'to': 9999,
        'pay': int(5.1294*26000)
    },
    {
        'from': 10000,
        'to': 10000,
        'pay': int(51.2941*26000)
    }
]


LEVEL_EXP = [
    {
        'exp_from': 0,
        'exp_to': 10,
        'level': 1,
        'rights': 'Nhận USDT miễn phí mỗi giờ<br>'
                  'Tham gia mọi trò chơi<br>'
                  '24h không onl bị trừ tối đa 10exp'
    },
    {
        'exp_from': 11,
        'exp_to': 100,
        'level': 2,
        'rights': 'Quyền lợi VIP 1<br>'
                  'Mở nhận/chuyển tiền nội bộ<br>'
                  'Mở liên kết hệ thống, nhận hoa hồng'
    },
    {
        'exp_from': 101,
        'exp_to': 1000,
        'level': 3,
        'rights': 'Quyền lợi VIP 2<br>'
                  'Mở phòng Bầu Cua'
    },
    {
        'exp_from': 1001,
        'exp_to': 10000,
        'level': 4,
        'rights': 'Quyền lợi VIP 3<br>'
                  'Tăng hoa hồng nhận từ hệ thống<br>'
                  'Giảm 5 phút nhận USDT miễn phí<br>'
                  'Mở kênh đầu tư lợi nhuận ngày'
    },
    {
        'exp_from': 10001,
        'exp_to': 100000,
        'level': 5,
        'rights': 'Quyền lợi VIP 4<br>'
                  'Tăng hoa hồng nhận từ hệ thống<br>'
                  'Giảm 5 phút nhận USDT miễn phí (55 phút)'
    },
    {
        'exp_from': 100001,
        'exp_to': 1000000,
        'level': 6,
        'rights': 'Quyền lợi VIP 5<br>'
                  'Tăng lợi nhuận từ kênh đầu tư<br>'
                  'Tăng USDT nhận miễn phí<br>'
                  'Giảm thêm 5 phút nhận USDT miễn phí (50 phút)'
    },
    {
        'exp_from': 1000001,
        'exp_to': 10000000,
        'level': 7,
        'rights': 'Quyền lợi VIP 6<br>'
                  'Mở gói đầu tư VIP<br>'
                  'Nhận thưởng $1.000 lần đầu đạt<br>'
                  'Tăng USDT nhận miễn phí<br>'
                  'Giảm thêm 5 phút nhận USDT miễn phí (45 phút)'
    },
    {
        'exp_from': 10000001,
        'exp_to': 100000000,
        'level': 8,
        'rights': 'Quyền lợi VIP 7<br>'
                  'Nhận thưởng $12.000 lần đầu đạt<br>'
                  'Tăng USDT nhận miễn phí<br>'
                  'Giảm 5 phút nhận USDT miễn phí (40 phút)'
    },
    {
        'exp_from': 100000001,
        'exp_to': 1000000000,
        'level': 9,
        'rights': 'Quyền lợi VIP 8<br>'
                  'Nhận thưởng $150.000 lần đầu đạt<br>'
                  'Tăng USDT nhận miễn phí<br>'
                  'Giảm 10 phút nhận USDT miễn phí (30 phút)'
    },
]

EXP_TABLE = {
    'ticket_roll': {
        'name': 'ticket_roll',
        'exp': 1,
        'ticket': 1,
        'rights': '1 lượt nhận miễn phí USDT'
    },
    'ticket_buy': {
        'name': 'ticket_buy',
        'exp': 0,
        'ticket': 1,
        'rights': 'Mua mỗi 100 vé số'
    },
    'dice_bet_0_01': {
        'name': 'dice_bet_0_01',
        'exp': 0,
        'ticket': 1,
        'rights': 'Cược trò chơi Bầu cua mỗi $0.01'
    },
    'wingo_bet_0_01': {
        'name': 'wingo_bet_0_01',
        'exp': 0,
        'ticket': 1,
        'rights': 'Cược trò chơi Wingo mỗi $0.01'
    },
    'wingo_bet_1': {
        'name': 'wingo_bet_1',
        'exp': 1,
        'ticket': 0,
        'rights': 'Cược trò chơi Wingo mỗi $1'
    },
    'bo_bet_0_01': {
        'name': 'wingo_bet_0_01',
        'exp': 0,
        'ticket': 1,
        'rights': 'Cược trò chơi BO mỗi $0.01'
    },
    'bo_bet_1': {
        'name': 'wingo_bet_1',
        'exp': 1,
        'ticket': 0,
        'rights': 'Cược trò chơi BO mỗi $1'
    },
}

REF_FEE = [
    {
        'game': 'BAUCUA',
        'fee': 2
    },
    {
        'game': 'WINGO',
        'fee': 2
    }
]

INVEST = [
    {  
        'no': '1',
        'name': 'Cơ bản 1',
        'from': 2000000,
        'to': 19999000,
        'bonus': 0,
        'day': 180,
        'min_exp': LEVEL_EXP[3]['exp_from'],
        'level': LEVEL_EXP[3]['level']
    },
    {
        'no': '2',
        'name': 'Cơ bản 2',
        'from': 20000000,
        'to': 99999000,
        'bonus': 0.05,
        'day': 150,
        'min_exp': LEVEL_EXP[3]['exp_from'],
        'level': LEVEL_EXP[3]['level']
    },
    {
        'no': '3',
        'name': 'Cao cấp 1',
        'from': 100000000,
        'to': 499999000,
        'bonus': 0.1,
        'day': 120,
        'min_exp': LEVEL_EXP[6]['exp_from'],
        'level': LEVEL_EXP[6]['level']
    },
    {
        'no': '4',
        'name': 'Cao cấp 2',
        'from': 500000000,
        'to': 500000000,
        'bonus': 0.15,
        'day': 90,
        'min_exp': LEVEL_EXP[6]['exp_from'],
        'level': LEVEL_EXP[6]['level']
    }
]
SECOND_GET_FREE = 60*60
PRICE_PER_TICKET = int(0.001*26000)


REFERRAL = {
    '0': [1,    0.5,   0.25,    0.125,    0.0625,    0.003125,  0.0115625, 0.0078125],
    '1': [1.3,  0.65,  0.325,   0.1625,   0.08125,   0.040625,  0.0203125, 0.01015625],
    '2': [1.5,  0.75,  0.375,   0.1875,   0.09375,   0.046875,  0.0234375, 0.01171875]
}
REFERRAL_INVEST = {
    '0': [1.418,  0.861,  0.417,   0.232,   0.132,   0.071,  0.0410,  0.0205],
    '1': [1.721,  1.055,  0.619,   0.334,   0.185,   0.102,  0.0530,  0.0265],
    '2': [1.927,  1.188,  0.728,   0.562,   0.333,   0.211,  0.0949,  0.0465]
}


def EXP_POINT(name):
    try:
        return EXP_TABLE[name]['exp']
    except:
        return 0

def TICKET_POINT(name):
    try:
        return EXP_TABLE[name]['ticket']
    except:
        return 0
# ============= DATA ==============
def BOOL(value):
    if value == 0:
        return True
    else:
        return False

def LEVEL(exp):
    result = 0
    for lev in LEVEL_EXP:
        if lev['exp_from'] <= exp <= lev['exp_to']:
            result = lev['level']
        else:
            result = LEVEL_EXP[-1]['level']
    return result

def RANDOM_LOTTERY():
    select = random.randrange(1, 10000)
    return str(select).rjust(5, '0')

def ROUND_BALANCE(balance):
    return round(balance, 7)

PER_PAGE = 10

def split_page(data, page, per_page=PER_PAGE):
    """
        :param data: [data]
        :param page: 0 -> max
    """
    max_page = int(len(data) / per_page)
    if len(data) % per_page >= max_page:
        max_page += 1

    this_page_from = page*per_page
    this_page_to = (page + 1)*per_page

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

    # // var xValues = JSON.parse('{{ DAY | tojson | safe}}');
    # // var yValues = JSON.parse("{{ PROFIT | tojson | safe}}");