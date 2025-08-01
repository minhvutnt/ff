const perFace = [[-0.1, 0.3, -1], [-0.1, 0.6, -0.4], [-0.85, -0.42, 0.73], [-0.8, 0.3, -0.75], [0.3, 0.45, 0.9], [-0.16, 0.6, 0.18]];

function number_to_baucua(number) {
  if (number == 1){return '<div class="dice-tomcua-mini div-tom"></div>';}
  else{
    if (number == 2){return '<div class="dice-tomcua-mini div-cua"></div>';}
    else{
      if (number == 3){return '<div class="dice-tomcua-mini div-bau"></div>';}
      else{
        if (number == 4){return '<div class="dice-tomcua-mini div-ca"></div>';}
        else{
          if (number == 5){return '<div class="dice-tomcua-mini div-nai"></div>';}
          else{
            if (number == 6){return '<div class="dice-tomcua-mini div-ga"></div>';}
  }}}}}
}