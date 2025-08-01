function switch_tab(class_tab, tab_target){
    var list_tab = document.getElementsByTagName(class_tab);
    var left_tab = null;
    var right_tab = null;
    var last_select = null;

    for(let i = 0; i < list_tab.length; i++){
        if(list_tab[i].id === tab_target){
            if(last_select != null){
                right_tab = list_tab[i];
            }
            else{
                left_tab = list_tab[i];
            }
        }
        var list_class = list_tab[i].className.split(' ');
        if(list_class.includes('tab_select')) {
            last_select = list_tab[i];
        }
    }
    if(left_tab != null){
        if(last_select != null){
            last_select.classList.remove('tab_in-left');
            last_select.classList.remove('tab_in-right');
            last_select.classList.add('tab_out_right');
            left_tab.classList.remove('tab_out_left');
            left_tab.classList.remove('tab_out_right');
            left_tab.classList.add('tab_in_right');
        }
        else{
            left_tab.classList.remove('tab_out_left');
            left_tab.classList.remove('tab_out_right');
            left_tab.classList.add('tab_in_right');
        }
        left_tab.classList.add('tab_select');
    }
    else{
        if(last_select != null){
            last_select.classList.remove('tab_in-left');
            last_select.classList.remove('tab_in-right');
            last_select.classList.add('tab_out_left');
            right_tab.classList.remove('tab_out_left');
            right_tab.classList.remove('tab_out_right');
            right_tab.classList.add('tab_in_left');
        }
        else{
            right_tab.classList.remove('tab_out_left');
            right_tab.classList.remove('tab_out_right');
            right_tab.classList.add('tab_in_left');
        }
        right_tab.classList.add('tab_select');
    }
}