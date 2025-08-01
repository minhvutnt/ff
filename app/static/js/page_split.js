var room_per_page = 10;
function list_page_data(data, data_page){
    var mini_page = [];
    for(var i = 0; i < data.length; i++){
        mini_page.push(data[data.length - i - 1]);
        if((i + 1)%room_per_page === 0 && mini_page !== []){
            data_page.push(mini_page);
            mini_page = [];
        }
        if(i === data.length - 1 && mini_page.length !== 0){
            data_page.push(mini_page);
            mini_page = [];
        }
    }
}
function html_my_dice_history(r_data){
    var result = 'Chờ xổ';
    if(r_data[5] === undefined || r_data[5] === ''){}
    else{
        result = number_to_baucua(r_data[5][0]) + number_to_baucua(r_data[5][1]) + number_to_baucua(r_data[5][2]);
    }
    var profit = '-';
    if(r_data[4] !== -1) {
        if(r_data[4] == 0){
            profit = '';
        }else{
            profit = r_data[4].toFixed(2);
        }
    }
    var  a = "<li><a class='dice_history_user'><span>" + r_data[0]
        + "</span><span>" + number_to_baucua(r_data[2])
        + "</span><span>" + result
        + "</span><span>" + r_data[3].toFixed(2)
        + "</span><span >" + profit
        + "</span></a></li>";
    return a
}
function html_admin_dice_history(r_data){
    var result = 'Chờ xổ';
    if(r_data.result === undefined || r_data.result === ''){}
    else{
        result = number_to_baucua(r_data.result[0]) +
            number_to_baucua(r_data.result[1]) +
            number_to_baucua(r_data.result[2]);
    }
    var a ="<li><a class='dice_history_admin'><span>" + r_data.session
            + "</span><span>" + result
            + "</span><span>" + r_data.bet
            + "</span><span >" + r_data.win
            + "</span></a></li>";
    return a

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

function html_room_data(r_data){
    var dice_1 = number_to_baucua(1);
    var dice_2 = number_to_baucua(2);
    var dice_3 = number_to_baucua(3);
    if(r_data.last_dice !== null){
        dice_1 = number_to_baucua(r_data.last_dice[0]);
        dice_2 = number_to_baucua(r_data.last_dice[1]);
        dice_3 = number_to_baucua(r_data.last_dice[2]);
    }
    var his = dice_1 + dice_2 + dice_3;
    return "<li><a class='list_dice_des' onclick='openclose_switch(\"btn_room_" + r_data.room_id + "\", \"description_room_" + r_data.room_id + "\", \"dice\");'>" +
        "<span class='openclose_switch openswitch' id='btn_room_" + r_data.room_id + "'></span><span>" + r_data.room_id + "</span><span>" + r_data.room_name + "</span><span >" + r_data.room_amount + "</span></a></li>" +
        "<div class='dice-game-room-mini-data' id='description_room_" + r_data.room_id + "'  style='display: none;'>" +
        "<div>" +
            '<li class="two_col_grid"><a>Tên phòng:</a><a>' + r_data.room_name + '</a></li>' +
            '<li class="two_col_grid"><a>Số dư: </a><a>$ ' + r_data.room_amount + '</a></li>' +
            '<li class="two_col_grid"><a>Thời hạn: </a><a>' + countdown_return(r_data.licence) + '</a></li>' +
            '<li class="two_col_grid"><a>Tổng giao dịch: </a><a>' + r_data.total_trade + '</a></li>' +
            '<li class="two_col_grid"><a>Lượt xổ trước: </a><a>' + his + '</a></li>' +
        '</div>' +
        "<div class='gold-btn' onclick='join_room(" + r_data.chat_id + ")'>Tham gia</div></div>";
}

function select_page(select_page, data_page, pagelist, btnpage, dataarea, data_type='LIST_DICE_ROOOM') {
    var first_page = document.getElementById(btnpage + '_first_page');
    var back_page = document.getElementById(btnpage + '_back_page');
    var next_page = document.getElementById(btnpage + '_next_page');
    var last_page = document.getElementById(btnpage + '_last_page');
    //list data
    var page_data = [];
    try {
        page_data = data_page[select_page - 1];
    } catch (e) {
    }
    data_area = document.getElementById(dataarea);
    data_area.innerHTML = "";
    if(page_data !== undefined) {
        if (page_data === []) {

        } else {
            for (var a = 0; a < page_data.length; a++) {
                switch (true) {
                    case data_type == 'LIST_DICE_ROOOM':
                        data_area.innerHTML += html_room_data(page_data[a]);
                        break
                    case data_type == 'MY_DICE_HISTORY':
                        data_area.innerHTML += html_my_dice_history(page_data[a]);
                        break
                    case data_type == 'ADMIN_DICE_HISTORY':
                        data_area.innerHTML += html_admin_dice_history(page_data[a]);
                        break
                    case data_type == 'ADMIN_DICE_STRATEGY':
                        data_area.innerHTML += html_admin_dice_strategy(page_data[a]);
                        break
                }
            }
        }
    }
    //page no
    var page_1 = null;
    var page_2 = null;
    var page_3 = null;
    var page_4 = null;
    var page_5 = null;
    var page_6 = null;
    var page_7 = null;
    if(data_page.length === 0) {
    }else{
    if (data_page.length === 1) {
        page_1 = 1;
    } else {
        if (data_page.length === 2) {
            page_1 = 1;
            page_2 = 2;}
    else{if(data_page.length === 3){page_1 = 1; page_2 = 2; page_3 = 3;}
    else{if(data_page.length === 4){page_1 = 1; page_2 = 2; page_3 = 3; page_4 = 4;}
    else{if(data_page.length === 5){page_1 = 1; page_2 = 2; page_3 = 3; page_4 = 4; page_5 = 5;}
    else{
        if(select_page <= 3){
            page_1 = 1; page_2 = 2; page_3 = 3;
            if(select_page === 3){
                page_4 = 4;
                page_5 = '...';
                page_6 = data_page.length;
            }
            else{
                page_4 = '...';
                page_5 = data_page.length;
            }
        }
        else{if(select_page >= (data_page.length - 2)){
            page_5 = data_page.length - 2; page_6 = data_page.length - 1; page_7 = data_page.length;
            if(select_page === (data_page.length - 2)){
                page_4 = data_page.length - 3;
                page_2 = '...';
                page_1 = 1;
            }
            else{
                page_2 = '...';
                page_1 = 1;
            }
        }
        else{
            page_1 = 1;
            page_2 = '...';
            page_7 = data_page.length;
            page_6 = '...';
            page_3 = select_page - 1;
            page_4 = select_page;
            page_5 = select_page + 1;
        }}

    }}}}}}
    page_number = document.getElementById(pagelist);
    page_number.innerHTML = '';
    var pagepage = [page_1, page_2, page_3, page_4, page_5, page_6, page_7];
    for(var page = 0; page < pagepage.length; page++){
        var disabled = '';
        if(pagepage[page] === '...' || pagepage[page] === select_page){disabled = 'disabled';}
        if(pagepage[page] !== null){
            page_number.innerHTML +=
                "<a onclick='select_page(" + pagepage[page] + ", data_page, pagelist, btnpage, dataarea, data_type );'><span class='number " + disabled + "'>" + pagepage[page] + "</span></a>";
        }
    }
    if(data_page.length === 0){
        first_page.classList.add('disabled');
        back_page.classList.add('disabled');
        next_page.classList.add('disabled');
        last_page.classList.add('disabled');
    }
    else{if(select_page === 1){
        first_page.classList.add('disabled');
        back_page.classList.add('disabled');
        next_page.classList.remove('disabled');
        last_page.classList.remove('disabled');
    }
    else{if(select_page === data_page.length){
        next_page.classList.add('disabled');
        last_page.classList.add('disabled');
        first_page.classList.remove('disabled');
        back_page.classList.remove('disabled');

    }else{
        first_page.classList.remove('disabled');
        back_page.classList.remove('disabled');
        next_page.classList.remove('disabled');
        last_page.classList.remove('disabled');
    }}}

}
