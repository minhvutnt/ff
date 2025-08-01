function timeConverter(UNIX_timestamp) {
    // Chuyển sang milliseconds nếu là timestamp 10 chữ số
    var a = (UNIX_timestamp.toString().length >= 13)
        ? new Date(UNIX_timestamp)
        : new Date(UNIX_timestamp * 1000);

    var months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'];
    var year = a.getFullYear();
    var month = months[a.getMonth()];
    var date = a.getDate().toString().padStart(2, '0');
    var hour = a.getHours().toString().padStart(2, '0');
    var min = a.getMinutes().toString().padStart(2, '0');
    var sec = a.getSeconds().toString().padStart(2, '0');

    var time = `${date} ${month} ${year} ${hour}:${min}:${sec}`;
    return time;
}

function timeConverter_short(UNIX_timestamp){
    if(UNIX_timestamp.toString().length >= 13){
        var a = new Date(UNIX_timestamp);
    }
    else{
        var a = new Date(UNIX_timestamp * 1000);
    }
    var months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'];
    var year = a.getFullYear();
    var month = months[a.getMonth()];
    var date = a.getDate();
    var time = date + ' ' + month + ' ' + year;
    return time;
}
function timeConverter_short_number(UNIX_timestamp) {
    var a = (UNIX_timestamp.toString().length >= 13)
            ? new Date(UNIX_timestamp)
            : new Date(UNIX_timestamp * 1000);

    var year = a.getFullYear();
    var month = a.getMonth() + 1;
    var date = a.getDate();

    var formattedDate = (date < 10 ? '0' + date : date) + '/' +
                        (month < 10 ? '0' + month : month);

    return formattedDate;
}
function timeConverter_minute_secon(UNIX_timestamp){
    var a = new Date(UNIX_timestamp);
    // var hour = a.getHours().toString().padStart(2, '0');
    var min = a.getMinutes().toString().padStart(2, '0');
    var sec = a.getSeconds().toString().padStart(2, '0');
    // var min = a.getMinutes();
    // var sec = a.getSeconds();
    let result = min + ":" + sec;
    return result;
}
function countdown_return(time_target, type='hour'){
    var countDownDate = new Date(time_target).getTime();
    var now = new Date().getTime();
    var distance = countDownDate - now;
    var hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
    var seconds = Math.floor((distance % (1000 * 60)) / 1000);
    var text = '';
        if (minutes < 10) {
            minutes = '0' + minutes.toString();
        }
        if (seconds < 10 && type != 'second') {
            seconds = '0' + seconds.toString();
        }
        if (type == 'hour') {
            if (distance <= 0) {
                var text = 'Room closed';
            } else {
                if(Number.isNaN(hours)){
                    var text = "--:--:--";
                }
                else{
                    var text = hours + ":" + minutes + ':' + seconds;
                }
            }
        } else {
            if (type == 'second') {
                if (distance <= 0) {
                } else {
                    var text = seconds;
                }
            }
        }
    return text;
}

function timenow(){
    var countDownDate = new Date(time_target).getTime();
    return countDownDate
}

function date_complete(timefrome){
    var countDownDate = new Date(timefrome).getTime();
    var now = new Date().getTime();
    var distance = now - countDownDate;
    var days = Math.floor(distance / (1000 * 60 * 60 * 24));
    return days;
}