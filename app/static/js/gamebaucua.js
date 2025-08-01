function dice_roll_dice(last_dice, load_dice){
    if(load_dice){
        const diceVal1 = 2;
        const diceVal2 = 1;
        const diceVal3 = 3;
        $(".dice1").removeClass("throw rolling");
        $(".dice2").removeClass("throw rolling");
        $(".dice3").removeClass("throw rolling");

        setVal1(1);
        setVal2(3);
        setVal3(2);
        $("#diceVal1").empty();
        $("#diceVal2").empty();
        $("#diceVal3").empty();
        setTimeout(() => {
          $(".dice1").addClass("throw");
          $(".dice2").addClass("throw");
          $(".dice3").addClass("throw");
        }, 50);
        setTimeout(() => {
          $("#diceVal1").html(diceVal1);
          $("#diceVal2").html(diceVal2);
          $("#diceVal3").html(diceVal3);
        }, 700);
    }
    if(last_dice === null){
      setVal1(1);
      setVal2(2);
      setVal3(3);
    }else{
      setVal1(last_dice[0]);
      setVal2(last_dice[1]);
      setVal3(last_dice[2]);
    }
}

var max_my_history = 0;
var this_my_history = 0;
function my_history_select_page(p){
    var page_s = 0;
    if(p === ''){page_s = max_my_history-1;}
    if(p === '1'){page_s = 0;}
    if(p === '+1'){page_s = this_my_history;}
    if(p === '-1'){page_s = this_my_history - 2;}
    var data = {'room_admin': ROOM_ADMIN,
                 'chat_id': Telegram.WebApp.initDataUnsafe.user.id,
                 'load_dice': false,
                 'room_page': 0,
                 'my_page': page_s, 'strategy_page': 0};
    socket.emit('socketio_baucua_room_data',data);
}
function my_history(ROOM_DATA){
    this_my_history = ROOM_DATA.my_page;
    max_my_history = ROOM_DATA.my_max_page;
    var my_history_value = ROOM_DATA.history;
    var  a = '';
    for(var i = 0; i < my_history_value.length; i++){
        if(my_history_value[i][1] == Telegram.WebApp.initDataUnsafe.user.id) {
            var result = 'Chờ xổ';
            var profit = '';
            if (my_history_value[i][5] != '') {
                result = number_to_baucua(my_history_value[i][5][0]) + number_to_baucua(my_history_value[i][5][1]) + number_to_baucua(my_history_value[i][5][2]);
                profit = my_history_value[i][4];
            }
            a += "<li><a class='dice_history_user'><span>" + my_history_value[i][0]
                + "</span><span>" + number_to_baucua(my_history_value[i][2])
                + "</span><span>" + result
                + "</span><span>" + my_history_value[i][3].toFixed(0)
                + "</span><span >" + profit
                + "</span></a></li>";
        }
    }
    var history_title = document.getElementById('history_title');
    var history_data = document.getElementById('history_data');
    var my_history_no = document.getElementById('my_history_no');
    var my_first_page = document.getElementById('my-first-page');
    var my_back_page = document.getElementById('my-back-page');
    var my_next_page = document.getElementById('my-next-page');
    var my_last_page = document.getElementById('my-last-page');
    history_title.innerHTML = "<li><a class='dice_history_user title'><span>No.</span><span>Chọn</span><span>Kết quả</span><span>Cược</span><span >Thắng</span></a></li>";
    history_data.innerHTML = a;
    my_history_no.innerHTML = "<a><span class='number disabled'>" + this_my_history + "/" + max_my_history + "</span></a>";
    if (this_my_history == 1) {
        my_first_page.classList.add('disabled');
        my_back_page.classList.add('disabled');
        my_next_page.classList.remove('disabled');
        my_last_page.classList.remove('disabled');
    } else {
        if (this_my_history == max_my_history) {
            my_first_page.classList.remove('disabled');
            my_back_page.classList.remove('disabled');
            my_next_page.classList.add('disabled');
            my_last_page.classList.add('disabled');
        } else {
            my_first_page.classList.remove('disabled');
            my_back_page.classList.remove('disabled');
            my_next_page.classList.remove('disabled');
            my_last_page.classList.remove('disabled');
        }
    }
}

var max_room_history = 0;
var this_room_history = 0;
function room_history_select_page(p){
    var page_s = 0;
    if(p === ''){page_s = max_room_history-1;}
    if(p === '1'){page_s = 0;}
    if(p === '+1'){page_s = this_room_history;}
    if(p === '-1'){page_s = this_room_history - 2;}
    var data = {'room_admin': ROOM_ADMIN,
                 'chat_id': Telegram.WebApp.initDataUnsafe.user.id,
                 'load_dice': false,
                 'room_page': page_s,
                 'my_page': 0, 'strategy_page': page_s};
    socket.emit('socketio_baucua_room_data',data);
}
function room_history(ROOM_DATA){
    console.log(ROOM_DATA)
    this_room_history = ROOM_DATA.strategy_page;
    max_room_history = ROOM_DATA.strategy_max_page;
    var room_history_value = ROOM_DATA.strategy_value;
    var  a = '';
    for(var i = 0; i < room_history_value.length; i++){
        var result = 'Chờ xổ';
        var profit = '';
        var bet = '';
        if(room_history_value[i][1] != ''){
            result = number_to_baucua(room_history_value[i][1][0]) + number_to_baucua(room_history_value[i][1][1]) +number_to_baucua(room_history_value[i][1][2]);
            profit = room_history_value[i][3];
            bet = room_history_value[i][2];
        }
        a += "<li><a class='dice_history_admin'><span>" + room_history_value[i][0]
                + "</span><span>" + result
                + "</span><span>" + bet
                + "</span><span >" + profit
                + "</span></a></li>";
    }
    var room_history_title = document.getElementById('room_history_title');
    var history_data = document.getElementById('room_history_data');
    var room_history_no = document.getElementById('room_history_no');
    var room_first_page = document.getElementById('room-first-page');
    var room_back_page = document.getElementById('room-back-page');
    var room_next_page = document.getElementById('room-next-page');
    var room_last_page = document.getElementById('room-last-page');
    room_history_title.innerHTML = "<li><a class='dice_history_admin title'><span>No.</span><span>Kết quả</span><span>Σ Cược</span><span >Σ Thắng</span></a></li>";
    room_history_data.innerHTML = a;
    room_history_no.innerHTML = "<a><span class='number disabled'>" + this_room_history + "/" + max_room_history + "</span></a>";
    if (this_room_history == 1) {
        room_first_page.classList.add('disabled');
        room_back_page.classList.add('disabled');
        room_next_page.classList.remove('disabled');
        room_last_page.classList.remove('disabled');
    } else {
        if (this_room_history == max_room_history) {
            room_first_page.classList.remove('disabled');
            room_back_page.classList.remove('disabled');
            room_next_page.classList.add('disabled');
            room_last_page.classList.add('disabled');
        } else {
            room_first_page.classList.remove('disabled');
            room_back_page.classList.remove('disabled');
            room_next_page.classList.remove('disabled');
            room_last_page.classList.remove('disabled');
        }
    }
}


var max_strategy_history = 0;
var this_strategy_history = 0;
function strategy_history_select_page(p){
    var page_s = 0;
    if(p === ''){page_s = max_strategy_history-1;}
    if(p === '1'){page_s = 0;}
    if(p === '+1'){page_s = this_strategy_history;}
    if(p === '-1'){page_s = this_strategy_history - 2;}
    var data = {'room_admin': ROOM_ADMIN,
                 'chat_id': Telegram.WebApp.initDataUnsafe.user.id,
                 'load_dice': false,
                 'room_page': page_s,
                 'my_page': 0, 'strategy_page': page_s};
    socket.emit('socketio_baucua_room_data',data);
}

function html_admin_dice_strategy(r_data){
    var result = ['', '', '', '', '', ''];

    if(r_data === undefined || r_data === ''){}
    else{
        var r_loop = [0, 0, 0, 0, 0, 0];
        r_loop[parseInt(r_data[0]) - 1] += 1;
        r_loop[parseInt(r_data[1]) - 1] += 1;
        r_loop[parseInt(r_data[2]) - 1] += 1;
        for(var r = 0; r < r_loop.length; r++){
            if(r_loop[r] != 0){
                result[r] = "<div class='dice_strategy_status dice-win-" + r_loop[r] + "'><div>" + r_loop[r] + "</div></div>";
            }
        }
        // result[parseInt(r_data[0]) - 1] = "<div class='dice_strategy_status'></div>";
        // result[parseInt(r_data[1]) - 1] = "<div class='dice_strategy_status'></div>";
        // result[parseInt(r_data[2]) - 1] = "<div class='dice_strategy_status'></div>";
    }
    var a ="<li><a class='dice_strategy'><span>" + result[0]
            + "</span><span>" + result[1]
            + "</span><span >" + result[2]
            + "</span><span >" + result[3]
            + "</span><span >" + result[4]
            + "</span><span >" + result[5]
            + "</span></a></li>";
    return a

}
function strategy_history(ROOM_DATA){
    this_strategy_history = ROOM_DATA.strategy_page;
    max_strategy_history = ROOM_DATA.strategy_max_page;
    var strategy_history_value = ROOM_DATA.room_history;
    var  a = '';
    for(var i = 0; i < strategy_history_value.length; i++){

        a += html_admin_dice_strategy(strategy_history_value[i]);
    }
    var strategy_history_title = document.getElementById('strategy_title');
    var strategy_data = document.getElementById('strategy_data');
    var strategy_no = document.getElementById('strategy_no');
    var strategy_first_page = document.getElementById('strategy_first_page');
    var strategy_back_page = document.getElementById('strategy_back_page');
    var strategy_next_page = document.getElementById('strategy_next_page');
    var strategy_last_page = document.getElementById('strategy_last_page');
    strategy_history_title.innerHTML = "<li><a class='dice_strategy title'><span>" +
        number_to_baucua(1) + "</span><span>" +
        number_to_baucua(2) + "</span><span>" +
        number_to_baucua(3) + "</span><span >" +
        number_to_baucua(4) + "</span><span >" +
        number_to_baucua(5) + "</span><span >" +
        number_to_baucua(6) + "</span></a></li>";;
    strategy_data.innerHTML = a;
    strategy_no.innerHTML = "<a><span class='number disabled'>" + this_strategy_history + "/" + max_strategy_history + "</span></a>";
    if (this_room_history == 1) {
        strategy_first_page.classList.add('disabled');
        strategy_back_page.classList.add('disabled');
        strategy_next_page.classList.remove('disabled');
        strategy_last_page.classList.remove('disabled');
    } else {
        if (this_strategy_history == max_strategy_history) {
            strategy_first_page.classList.remove('disabled');
            strategy_back_page.classList.remove('disabled');
            strategy_next_page.classList.add('disabled');
            strategy_last_page.classList.add('disabled');
        } else {
            strategy_first_page.classList.remove('disabled');
            strategy_back_page.classList.remove('disabled');
            strategy_next_page.classList.remove('disabled');
            strategy_last_page.classList.remove('disabled');
        }
    }
}



function html_room_history(title, DATA, history, room_history, is_admin){
    var list_area = document.getElementsByClassName('amount-area');
    all_value = ROOM_DATA.all_value;

    var data = [];
    for(var nu = 0; nu < room_history.length; nu++){
        data.push({'session': nu + 1,
                    'bet': 0,
                    'result': room_history[nu],
                    'win': 0})
    }
    for(var a = 0; a < list_area.length; a++){
        list_area[a].classList.remove('amount-area-betting');
    }
    title.innerHTML = "<li><a class='dice_history_admin title'><span>No.</span><span>Kết quả</span><span>Σ Cược</span><span >Σ Thắng</span></a></li>";
    if((history == [] && !is_admin) || is_admin){
        DATA.innerHTML = "<li class='center'>Chưa có lịch sử</li>";
    }
    else{
        DATA.innerHTML = '';

        // if(!is_admin){
        // }
        for(var i = 0; i < history.length; i++){
            var is_new = true;
            var rrrrrr = 0;
            if(history[i][4] !== -1){
                rrrrrr = history[i][4];
            }
            for(var f = 0; f < data.length; f++){
                if(data[f].session === history[i][0]){

                    is_new = false;
                    data[f].bet += history[i][3];
                    data[f].win += rrrrrr;
                    break
                }
            }
            if(is_new){
                data.push({'session': history[i][0],
                            'bet': history[i][3],
                            'result': history[i][5],
                            'win': rrrrrr})
            }
            if(history[i][4] == -1 && history[i][3] !== 0){
                list_area[history[i][2] - 1].classList.add('amount-area-betting');
            }
        }

        var ds1 = [];
        list_page_data(data, ds1);
        select_page(1, ds1, 'room_no', 'room', 'room_history_data', data_type='ADMIN_DICE_HISTORY');
    }
}


function dice_history() {
    var my_room_name = document.getElementById('my_room_name');
    var my_room_balance = document.getElementById('my_room_balance');
    var my_room_profit = document.getElementById('my_room_profit');
    var my_room_end_time =document.getElementById('my_room_end_time');
    var my_room_total_trade = document.getElementById('my_room_total_trade');
    my_room_name.innerHTML = ROOM_DATA.room_name;
    my_room_balance.innerHTML = ROOM_DATA.room_amount + " đ";
    my_room_profit.innerHTML = ROOM_DATA.profit + " đ";
    my_room_total_trade.innerHTML = ROOM_DATA.total_trade + " đ";

    var list_area = document.getElementsByClassName('amount-area');
    var history = ROOM_DATA.history;

    var room_history_title = document.getElementById('room_history_title');
    var room_history_data = document.getElementById('room_history_data');

    var room_trade = document.getElementById('room_trade');

    var my_bet_tom = document.getElementById('my_bet_tom');
    var my_bet_cua = document.getElementById('my_bet_cua');
    var my_bet_bau = document.getElementById('my_bet_bau');
    var my_bet_ca = document.getElementById('my_bet_ca');
    var my_bet_nai = document.getElementById('my_bet_nai');
    var my_bet_ga = document.getElementById('my_bet_ga');
    var my = [my_bet_tom, my_bet_cua, my_bet_bau, my_bet_ca, my_bet_nai, my_bet_ga];
    var my_value = ROOM_DATA.my_value;

    var all_bet_tom = document.getElementById('all_bet_tom');
    var all_bet_cua = document.getElementById('all_bet_cua');
    var all_bet_bau = document.getElementById('all_bet_bau');
    var all_bet_ca = document.getElementById('all_bet_ca');
    var all_bet_nai = document.getElementById('all_bet_nai');
    var all_bet_ga = document.getElementById('all_bet_ga');
    var all = [all_bet_tom, all_bet_cua, all_bet_bau, all_bet_ca, all_bet_nai, all_bet_ga];

    var all_value = ROOM_DATA.all_value;
    var total_trade = 0;
    for (var c = 0; c < history.length; c++) {
        if (history[c][4] === -1) {
            total_trade += history[c][3];
            list_area[history[c][2] - 1].classList.add('amount-area-betting');
        }
    }
    for (var d = 0; d < all_value.length; d++) {
        if (all_value[d] === 0) {
            list_area[d].classList.remove('amount-area-betting');
        }
    }
    room_trade.innerHTML = total_trade.toFixed(0) + " đ";
    my_history(ROOM_DATA);
    room_history(ROOM_DATA);
    strategy_history(ROOM_DATA);
    //
    // var ISADMIN = Telegram.WebApp.initDataUnsafe.user.id === ROOM_ADMIN;
    // // html_room_history(history_title, history_data, history, ROOM_DATA.room_history, ISADMIN);
    // // html_room_history(room_history_title, room_history_data, history, ROOM_DATA.room_history, false);
    // if (!ISADMIN) {
    //
    //     if (history.length == 0) {
    //         history_data.innerHTML = "<li class='center'>Chưa có lịch sử</li>";
    //     } else {
    //
    //         var my_history = [];
    //         for (var i = 0; i < history.length; i++) {
    //             if (Telegram.WebApp.initDataUnsafe.user.id === history[i][1] && history[i][3] !== 0) {
    //                 if (history[i][4] !== -1) {
    //                 } else {
    //                     // my_value[history[i][2] - 1] = history[i][3].toFixed(2);
    //
    //                 }
    //             }
    //             if (Telegram.WebApp.initDataUnsafe.user.id === history[i][1]){
    //                 my_history.push(history[i]);
    //             }
    //         }
    //
    //         var ds = [];
    //         list_page_data(my_history, ds);
    //         select_page(1, ds, 'my_bet_no', 'my_bet', 'history_data', data_type = 'MY_DICE_HISTORY');
    //     }
    // }
    for (var c = 0; c < my.length; c++) {
        my[c].innerHTML = my_value[c].toFixed(0);
    }
    for (var b = 0; b < all.length; b++) {
        all[b].innerHTML = all_value[b].toFixed(0);
    }
    //
    // //strategy tab
    // var strategy_title = document.getElementById('strategy_title');
    // strategy_title.innerHTML = "<li><a class='dice_strategy title'><span>" +
    //     number_to_baucua(1) + "</span><span>" +
    //     number_to_baucua(2) + "</span><span>" +
    //     number_to_baucua(3) + "</span><span >" +
    //     number_to_baucua(4) + "</span><span >" +
    //     number_to_baucua(5) + "</span><span >" +
    //     number_to_baucua(6) + "</span></a></li>";

    // var ds3 = [];
    // list_page_data(ROOM_DATA.room_history, ds3);
    // if (ds3.length == 0) {
    //     document.getElementById('strategy_data').innerHTML = "<li class='center'>Chưa có lịch sử</li>";
    // } else {
    //     select_page(1, ds3, 'strategy_no', 'strategy', 'strategy_data', data_type = 'ADMIN_DICE_STRATEGY');
    // }
}
function change_dice_status(){
    if(Telegram.WebApp.initDataUnsafe.user.id == ROOM_ADMIN){
        if(new_dice_status === 1){
            Telegram.WebApp.showPopup({
                    title  : 'Phòng ' + ROOM_DATA.room_id,
                    message: 'Bắt đầu đếm ngược 10 giây trước khi lắc',
                    buttons: [
                        {id: 'accept', type: 'destructive', text: 'Bắt đầu'},
                        {type: 'cancel'},
                    ]
                }, function (buttonId) {
                    if (buttonId === 'accept') {
                        socket.emit('socketio_baucua_dice_status',
                            {'chat_id': ROOM_ADMIN, 'dice_status': 1});
                    }
                }
            );
        }else{

        }
    }
    if(ROOM_DATA.dice_status === 3){
        if(Telegram.WebApp.initDataUnsafe.user.id == ROOM_ADMIN) {
            Telegram.WebApp.showPopup({
                    title: 'Phòng ' + ROOM_DATA.room_id,
                    message: 'Lắc ',
                    buttons: [
                        {id: 'accept', type: 'destructive', text: 'Bắt đầu'},
                        {type: 'cancel'},
                    ]
                }, function (buttonId) {
                    if (buttonId === 'accept') {

                        socket.emit('socketio_baucua_dice_status',
                            {'chat_id': ROOM_ADMIN, 'dice_status': 4});
                    }
                }
            );
        }
    }
}
function disable_view_dice(bool){
    var dice_status_div = document.getElementById('dice_status');
    if(bool){
        dice_status_div.style.backgroundColor = '#00000088';
    }else{
        dice_status_div.style.backgroundColor = '#00000003';
    }
}
var new_dice_status = null;
var second_run = false;

function dice_status_dice(){
    var dice_status_text = document.getElementById('dice-status-text');
    var dice_status_number = document.getElementById('dice-status-number');
    if(ROOM_DATA.dice_status === 0){
        dice_status_text.innerHTML = '';
        dice_status_text.style.color = 'var(--color-buy)';
        if(Telegram.WebApp.initDataUnsafe.user.id == ROOM_ADMIN){
            dice_status_number.innerHTML = 'Đếm ngược';
            disable_view_dice(true);
            new_dice_status = 1;
        }else{
            disable_view_dice(false);
            dice_status_number.innerHTML = '';
        }
    }
    else{if(ROOM_DATA.dice_status === 4){

    }else{if(ROOM_DATA.dice_status === 3){
        TRUE_TRADE = false;
        if(Telegram.WebApp.initDataUnsafe.user.id == ROOM_ADMIN){
            dice_status_number.innerHTML = 'Lắc';
            disable_view_dice(true);
            new_dice_status = 4;
        }else{
            disable_view_dice(true);
            dice_status_number.innerHTML = 'Chờ lắc';
        }

    }else{if(!second_run){
            second_run = true;
            disable_view_dice(true);
            var interval_second = setInterval(function () {
                dice_status_number.classList.add('second_cd_animation');
                var second_left = countdown_return(ROOM_DATA.dice_status, type='second');
                if(second_left !== ''){
                    dice_status_number.innerHTML = second_left;
                }
                else{
                    socket.emit('socketio_baucua_room_data',
                        {'room_admin': ROOM_ADMIN,
                         'chat_id': Telegram.WebApp.initDataUnsafe.user.id,
                        'load_dice': false,
                        'my_page': ROOM_ADMIN.my_page,
                        'room_page': ROOM_ADMIN.room_page,
                         'strategy_page': ROOM_ADMIN.strategy_page});
                    second_run = false;
                    dice_status_number.classList.remove('second_cd_animation');
                    clearInterval(interval_second);
                }
            }, 1000);
        }
    }}}
}
