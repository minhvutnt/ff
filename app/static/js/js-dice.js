let allVal = {
  x: 0,
  y: 0,
  z: 0
};

//每一面的旋轉數值
const perFace = [[-0.1, 0.3, -1], [-0.1, 0.6, -0.4], [-0.85, -0.42, 0.73], [-0.8, 0.3, -0.75], [0.3, 0.45, 0.9], [-0.16, 0.6, 0.18]];

//獲取數值
const getVal = () => {
  $.each(allVal, (i, n) => {
    //取得數值
    n = Math.cos($(`#r${i}`).val() / 100 * 3.142).toFixed(3);
    //輸出數值
    $(`#n${i}`).html(n);
    //改變allVal各值
    Object.defineProperty(allVal, i, {
      value: n
    });
  });
};

//設定數值
const setVal = num => {
  $(".dice").css("transform", `rotate3d(${perFace[num - 1]}, 180deg)`);
};

//設定骰子
const setDice = () => {
  getVal();
  $(".dice").css("transform", `rotate3d(${Object.values(allVal)}, 180deg)`);
};

//按鈕動作
$(".controller input[type=range]").on("change", () => {
  setDice();
});
