function referrer_list(data) {
    const count_f1 = document.getElementById('count-f1');
    const count_ff = document.getElementById('count-ff');
    const total_amount_f1 = document.getElementById('total-amount-f1');
    const total_amount_ff = document.getElementById('total-amount-ff');

    count_f1.innerHTML = data.f1.length;
    count_ff.innerHTML = data.f2.length + data.f3.length + data.f4.length + data.f5.length + data.f6.length;

    let total_am_f1 = 0;
    let total_am_ff = 0;
    ref_list.innerHTML = "<div class='line-hide'><div></div><div></div><div></div><div></div><div></div></div>"
    for(let i = 0; i < 10; i++){
        var dd = [];
        if(i == 0){dd = data.f1;}
        if(i == 1){dd = data.f2;}
        if(i == 2){dd = data.f3;}
        for(let f = 0; f < dd.length; f++) {
            ref_list.innerHTML += "<div class='ref-user ref ref-" + (i + 1) + "'>" +
                 "<span class='bg-line left-pan expand'>" + dd[f].uid + "</span>" +
                 "<span>" + dd[f].amount + "</span>" +
                 "<span class='user-name'>" + dd[f].full_name + "</span>" +
                 "</div>";
            if(i == 0){
                total_am_f1 += dd[f].amount;
            }else{
                total_am_ff += dd[f].amount;
            }
        }
    }
    total_amount_f1.innerHTML = total_am_f1 + " đ";
    total_amount_ff.innerHTML = total_am_ff + " đ";
}

function ref_history(msg) {
    ref_history_data.innerHTML = '';
    if(msg.data == []){ref_history_data.innerHTML = "<li>Chưa có lịch sử hoa hồng</li>";}
    else{
        for(let i = 0; i < msg.data.length; i++) {
            ref_history_data.innerHTML += "<li onclick='check_his_ref(" + msg.data[i].stt + ")'><a class='ref_his'><span>" + timeConverter(msg.data[i].day) + "</span><span>" + msg.data[i].from_uid + "</span><span>$ " + msg.data[i].ref_amount + "</span></a></li>" +
                                "<div class='ex_history' id='ex_" + msg.data[i].stt + "'>" +
                                "    <span>{{ LANG['bet_amount'][user_language] }}</span><span>" + msg.data[i].amount + " đ</span>" +
                                "    <span>{{ LANG['commission_level'][user_language] }}</span><span>" + msg.data[i].ref_level + "</span>" +
                                "    <span>{{ LANG['commission_percent'][user_language] }}</span><span>" + msg.data[i].percent + "%</span>" +
                                "    <span>{{ LANG['commission_received'][user_language] }}</span><span>" + msg.data[i].ref_amount + " đ</span>" +
                                "    <span>{{ LANG['bet_type'][user_language] }}</span><span>" + msg.data[i].ref_type + "</span>" +
                                "</div>";

        }
    }

    if (this_res_history == 1 || this_res_history == 0) {
        his_first_page.classList.add('disabled');
        his_back_page.classList.add('disabled');
        his_next_page.classList.remove('disabled');
        his_last_page.classList.remove('disabled');
    } else {
        if (this_res_history == max_res_history) {
            his_first_page.classList.remove('disabled');
            his_back_page.classList.remove('disabled');
            his_next_page.classList.add('disabled');
            his_last_page.classList.add('disabled');
        } else {
            his_first_page.classList.remove('disabled');
            his_back_page.classList.remove('disabled');
            his_next_page.classList.remove('disabled');
            his_last_page.classList.remove('disabled');
        }
    }
}
function check_his_ref(nn) {
    var d = document.getElementsByClassName('ex_history');
    for(var b = 0; b < d.length; b++){
        if(d[b].id == 'ex_' + nn){
            $("#" + d[b].id).slideDown();
            document.getElementById(d[b].id).style.display = 'grid';

        }
        else{
            $("#" + d[b].id).slideUp();
        }
    }
}