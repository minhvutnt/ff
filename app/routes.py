import time
from app import app, db
import flask
from flask import request, jsonify, render_template, Response
from flask.helpers import url_for, send_from_directory
import json
from flask_cors import CORS
from app.lib_bool import *
from app.request import *
from threading import Thread
import threading
from app.timestamp import *
import random
from app.glo import *
from app.LANGUAGE import WEB_LANGUAGE
CORS(app, resources={r"/*": {"origins": "*"}})

#===================================================[ SOCKETIO ]========================================================
# flask run --host=0.0.0.0 --port=4040 --with-threads
#================================================[ WEB SITE ]========================================================
@app.context_processor
def inject_random_style():
    user_lang = getattr(request, 'user_language', 'en')
    try:
        test_lang = WEB_LANGUAGE['welcome'][user_lang]
    except:
        user_lang = 'en'
    random_style = random.randint(0, 100000)
    return dict(random_style=random_style,
                user_language=user_lang,
                SOCKETIO_URL=SOCKETIO_URL,
                PROJECT_NAME=PROJECT_NAME,
                LINK_BOT=BOT_LINK,
                TRUE_TEST=TRUE_TEST,
                LANG=WEB_LANGUAGE)

def format_thousands(value):
    return f"{int(value):,}".replace(",", ".")

app.jinja_env.filters['format_thousands'] = format_thousands

@app.before_request
def detect_user_language():
    lang = request.args.get('lang', 'en')
    request.user_language = lang

@app.route('/empty', methods=['GET'])
def html_no_ref():
    return render_template('nof0.html')


@app.route('/', methods=['GET'])
@app.route('/home', methods=['GET'])
def index():
    return render_template('home-oasic.html')


@app.route('/select_game', methods=['GET'])
def html_select_game():
    return render_template('game.html')

@app.route('/select_freeusdt', methods=['GET'])
def html_select_freeusdt():
    return render_template('freeusdt.html',
                           PAGE_FREE_USDT=True,
                           LOTTERY_RATE=LOTTERY_RATE,
                           PRICE_PER_TICKET=PRICE_PER_TICKET)

@app.route('/BauCua_room', methods=['GET'])
def html_baucua_room():
    return render_template('BauCua_Room.html')

@app.route('/select_game_bau_cua/<admin>', methods=['GET'])
def html_select_game_bau_cua(admin):
    return render_template('game-bau-cua.html',
                           ADMIN=admin)

@app.route('/chat_support', methods=['GET'])
def chat_support():
    return render_template('chat_support.html')

@app.route('/invest', methods=['GET'])
def html_invest():
    # day, profit = db_list_daily_profit()
    return render_template('share.html',
                           INVEST=INVEST,
                           INVEST_PACKET=INVEST
                           )

@app.route('/wallet', methods=['GET'])
def html_wallet():
    return render_template('wallet.html')


@app.route('/wingo', methods=['GET'])
def html_wingo():
    return render_template('wingo.html')


@app.route('/referrer', methods=['GET'])
def html_referrer():
    return render_template('referrer.html',
                           REFERRAL=REFERRAL,
                           REFERRAL_INVEST=REFERRAL_INVEST)

@app.route('/spin_lucky', methods=['GET'])
def html_spin_lucky():
    return render_template('spin_lucky.html')

#==================================================================================================

@app.route('/binary_option')
def html_binary_option():
    return render_template('binary_option.html')

#==================================================================================================
@app.route('/admin', methods=['GET'])
def html_admin():
    return render_template('MANAGE.html')


@app.route('/event-daily', methods=['GET'])
def html_event_daily():
    return render_template('event-daily.html',
                           )
