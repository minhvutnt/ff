
function click_change_amount(value){
    if(value === 'ZERO'){bet_amount.value = 0;}
    else{if(value === 'ALL'){bet_amount.value = parseInt(document.getElementById('amount').innerHTML);}
    else{
        if(parseFloat(bet_amount.value) + value < 0){
        bet_amount.value = 0;
    }
    else{
        bet_amount.value = parseFloat(bet_amount.value) + value;
    }
    }}
    update_bet_amount();
}


function update_bet_amount(){
    input_2digit(bet_amount);
    var amount = bet_amount.value;
    add_bet_amount_value.innerHTML = " +" + amount;
    add_bet_amount_value.style.color = "var(--color-buy)";
};

function show_my_his_info(number){
    var list_expand = document.getElementsByClassName('expand');
    for(var k = 0; k < list_expand.length; k++){
        if(list_expand[k].id == 'my-his-' + number){
            $("#" + list_expand[k].id).slideDown();

        }
        else{
            $("#" + list_expand[k].id).slideUp();
        }
    }
}

function my_bo_history(data, last_page, next_page, max_page, page, last_result) {
    console.log(page, data)
    my_bo_his_data.innerHTML = '';
    for (var i = 0; i < data.length; i++) {
        var bv = data[i].bet_value;
        var first_content = '';
        var first_color = '';
        var select_name = bv;
        if(bv == 'DOWN'){select_name = 'Giảm'; first_color = 'bg-down'; first_content = 'ct-big';}
        if(bv == 'UP'){select_name = 'Tăng';first_color = 'bg-up'; first_content = 'ct-small';}

        var rn = data[i].roundnumber;
        var ot = timeConverter(data[i].ordertime);

        var wi = '';
        var pr = '';
        if(data[i].result != ''){
            if(data[i].profit <= 0){
                wi = "<a class='win-loss loss_border' style='color: var(--norm_red-color) !important;'>Thất bại</a>";
                pr = "<a class='right' style='color: var(--norm_red-color) !important;'>" + data[i].profit + "</a>";
            }
            else{
                if(data[i].profit == data[i].amount){
                    wi = "<a class='win-loss win_border' style='color: var(--norm_green-color) !important;'>Hoà</a>";
                }
                else{
                    wi = "<a class='win-loss win_border' style='color: var(--norm_green-color) !important;'>Thành công</a>";
                }
                pr = "<a class='right' style='color: var(--norm_green-color) !important;'> $" + data[i].profit + "</a>";
            }
        }
        my_bo_his_data.innerHTML += "<li class='my-bo-history' onclick='show_my_his_info(\"" + data[i].stt + "\")'>" +
            "<span class='" + first_color + " " + first_content + "'></span>" +
            "<span class='round-time'><a>" + rn + "</a><a>" + ot + "</a></span>" +
            "<span class='round-time'>" + wi + pr + "</span>" +
            "</li>" +
            "<div class='expand' style='display: none' id='my-his-" + data[i].stt + "'>" +
            "<li><span>Kỳ xổ</span><span>" + rn + "</span></li>" +
            "<li><span>Số tiền mua</span><span>$ " + data[i].amount + "</span></li>" +
            "<li><span>Thuế</span><span>$ " + data[i].tax + "</span></li>" +
            "<li><span>Tiền sau thuế</span><span>$ " + parseFloat((data[i].amount - data[i].tax).toFixed(4)) + "</span></li>" +
            "<li><span>Kết quả</span><span>" + data[i].result + "</span></li>" +
            "<li><span>Chọn</span><span class='" + "'>" + select_name + "</span></li>" +
            "<li><span>Tình trạng</span><span>" + wi + "</span></li>" +
            "<li><span>Thắng thua</span><span>" + data[i].profit + "</span></li>" +
            "<li><span>Thời gian tạo</span><span>" + ot + "</span></li>" +
            "</div>";

    }
    my_no.innerHTML = "<a><span class='number disabled'>" + page + "/" + max_page + "</span></a>";
    if (page == 1) {
        my_first_page.classList.add('disabled');
        my_back_page.classList.add('disabled');
        my_next_page.classList.remove('disabled');
        my_last_page.classList.remove('disabled');
    } else {
        if (page == max_page) {
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