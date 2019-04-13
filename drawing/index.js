// create canvas element and append it to document body
var canvas = document.createElement('canvas');
document.body.appendChild(canvas);

var button = document.createElement('button');
document.body.appendChild(button);

var color = '#000000';

button.onclick = function () {
    color = '#ff0000';
}

// some hotfixes... ( ≖_≖)
document.body.style.margin = 0;
canvas.style.position = 'relative';

// get canvas 2D context and set him correct size
var ctx = canvas.getContext('2d');
resize();

// last known position
var pos = { x: 0, y: 0 };

window.addEventListener('resize', resize);
document.addEventListener('mousemove', draw);
document.addEventListener('mousedown', setPosition);
document.addEventListener('mouseenter', setPosition);

// new position from mouse event
function setPosition(e) {
  pos.x = e.clientX;
  pos.y = e.clientY;
}

// resize canvas
function resize() {
  ctx.canvas.width = window.innerWidth;
  ctx.canvas.height = window.innerHeight;
}

// var color = '#c0392b';

function draw(e) {
  // mouse left button must be pressed
  if (e.buttons !== 1) return;

  ctx.beginPath(); // begin

  ctx.lineWidth = 5;
  ctx.lineCap = 'round';
  // You can check to see if some HTML element is set - and change the color based on that?
  ctx.strokeStyle = color;

  ctx.moveTo(pos.x, pos.y); // from
  setPosition(e);
  ctx.lineTo(pos.x, pos.y); // to

  ctx.stroke(); // draw it!
}