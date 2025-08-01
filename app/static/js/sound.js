audioCtx = new(window.AudioContext || window.webkitAudioContext)();

// function show() {
//   frequency = document.getElementById("fIn").value;
//   switch (document.getElementById("tIn").value * 1) {
//     case 0: type = 'sine'; break;
//     case 1: type = 'square'; break;
//     case 2: type = 'sawtooth'; break;
//     case 3: type = 'triangle'; break;
//   }
//   volume = document.getElementById("vIn").value / 100;
//   duration = document.getElementById("dIn").value;
// }

function beep(volume, frequency, type, duration) {
  var oscillator = audioCtx.createOscillator();
  var gainNode = audioCtx.createGain();

  oscillator.connect(gainNode);
  gainNode.connect(audioCtx.destination);

  gainNode.gain.value = volume;
  oscillator.frequency.value = frequency;
  oscillator.type = type;

  oscillator.start();

  setTimeout(
    function() {
      oscillator.stop();
    },
    duration
  );
};

function sound_order_success(){
	var count = 0;
    var sou = setInterval(function () {
      	count += 1;
        if(count == 1){beep(0.2, 2033, 'sawtooth', 80);}
        if(count == 2){beep(0.1, 3333, 'sine', 100);};
        if(count == 3){beep(0.2, 4333, 'sine', 180);}
        if(count == 4){clearInterval(sou);};

    }, 100);
}