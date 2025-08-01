function openclose_switch(btn, des, father=null){
    if(father === 'dice'){
        var list_room_game = document.getElementsByClassName('dice-game-room-mini-data');
        for (var i = 0; i < list_room_game.length; i++){
            $("#" + list_room_game[i].id).slideUp();
        }
    }

    var btn_click = document.getElementById(btn);
    var descript = document.getElementById(des);
    if(descript.style.display === 'none'){
        $("#" + des).slideDown();
        btn_click.classList.remove('openswitch');
        btn_click.classList.add('closeswitch');
    }
    else{
        
        $("#" + des).slideUp();
        btn_click.classList.remove('closeswitch');
        btn_click.classList.add('openswitch');
    }
}
