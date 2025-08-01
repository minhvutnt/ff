const pointerDrag = (el) => {

  const move = (ev) => {
    el.style.left = `${el.offsetLeft + ev.movementX}px`
    el.style.top = `${el.offsetTop + ev.movementY}px`
  };
  
  const dragStart = (ev) => el.setPointerCapture(ev.pointerId);
  const drag      = (ev) => el.hasPointerCapture(ev.pointerId) && move(ev);
  const dragEnd   = (ev) => el.releasePointerCapture(ev.pointerId);
  
  el.addEventListener("pointerdown", dragStart);
  el.addEventListener("pointermove", drag);
  el.addEventListener("pointerup", dragEnd);
};

// Use like:
document.querySelectorAll(".move_box").forEach(pointerDrag);
//class
// .move_box {
//   position: absolute;
//   width: 50px; height: 50px;
//   background: red;
//   user-select: none; /* prevent text selection */
//   touch-action: none; /* fixes drag on touch devices */
// }