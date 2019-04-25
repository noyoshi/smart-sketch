// SETTING ALL VARIABLES

var isMouseDown = false;
var canvas = document.createElement("canvas");
var body = document.getElementById("container_col");
var ctx = canvas.getContext("2d");
var linesArray = [];
currentSize = 5;
var currentColor = "#759edf";
var currentBg = "white";
var myBoard = new DrawingBoard.Board("zbeubeu", {
  controls: [
    { Size: { type: "dropdown" } },
    { DrawingMode: { filler: false } },
    "Navigation",
    "Download"
  ]
});

myBoard.clearWebStorage();

// INITIAL LAUNCH

// createCanvas();

// BUTTON EVENT HANDLERS

jQuery(document).ready(function($) {
  $color_list = [
    { color: "#384f83", title: "sea" },
    { color: "#efefef", title: "cloud" },
    { color: "#2c1e16", title: "dirt" },
    { color: "#5d6e32", title: "bush" },
    { color: "#b7d24e", title: "grass" },
    { color: "#3c3b4b", title: "mountain" },
    { color: "#987e6a", title: "road" },
    { color: "#759edf", title: "sky-other" },
    { color: "#352613", title: "tree" },
    { color: "#636363", title: "pavement" },
    { color: "#e670b6", title: "flower" },
    { color: "#c1c3c9", title: "fog" },
    { color: "#776c2d", title: "hill" },
    { color: "#bf602c", title: "leaves" },
    { color: "#32604d", title: "river" },
    { color: "#fafafa", title: "snow" },
    { color: "#7CFC00", title: "airplane" },
    { color: "#D2D2D2", title: "boat" },
    { color: "#D2691E", title: "bridge" },
    { color: "#8B0000", title: "roof*" },
    { color: "#DEB887", title: "house*" },
    { color: "#00CED1", title: "window-other*" },
    { color: "#B22222", title: "wall-brick*" },
    { color: "#8B4513", title: "branch" }
    // { color: "#FF3232", title: "fire" }
  ];

  $(".color-picker").wrap('<div class="color-picker-wrap"></div>');

  $(".color-picker-wrap").each(function() {
    var self = $(this);

    if (self.children(".color-picker").hasClass("cp-sm")) {
      self.addClass("cp-sm");
    } else if (self.children(".color-picker").hasClass("cp-lg")) {
      self.addClass("cp-lg");
    }

    self.append('<ul></ul><input type="color" style="display:none;" />');

    var $foundactive = false;

    for (var i = 0; i < $color_list.length; i++) {
      var $active = "";

      if (self.children(".color-picker").val() == $color_list[i].color) {
        $active = 'class="active"';

        $foundactive = true;
      }

      self
        .children("ul")
        .append(
          "<li " +
            $active +
            ' style="background-color:' +
            $color_list[i].color +
            '" title="' +
            $color_list[i].title +
            '">&nbsp&nbsp' +
            $color_list[i].title +
            "&nbsp&nbsp</li>"
        );
    }

    if (!$foundactive && self.children(".color-picker").val() != "") {
      self
        .children("ul")
        .append(
          '<li class="active" title="Custom Color ' +
            self.children(".color-picker").val() +
            '" style="background-color:' +
            self.children(".color-picker").val() +
            '"></li>'
        );

      if (self.children(".color-picker").hasClass("cp-show")) {
        self.children("small").remove();

        self.append(
          "<small>Selected Color: <code>" +
            self.children(".color-picker").val() +
            "</code></small>"
        );
      }
    }

    // self.children('ul').append('<li class="add_new" title="Add New">+</li>');
  });

  $(".color-picker-wrap ul").on("click", "li", function() {
    console.log("1");

    var self = $(this);

    // if (!self.hasClass('add_new')) {

    if (!self.hasClass("active")) {
      self.siblings().removeClass("active");

      // var color = rgb2hex(self.css("backgroundColor"));
      var color = self.css("backgroundColor");

      console.log(color);

      currentColor = color;
      myBoard.ctx.strokeStyle = color; // Sets he board color

      self
        .parents(".color-picker-wrap")
        .children(".color-picker")
        .val(color);

      self.addClass("active");
    }
    // } else {
    //   self.parents('.color-picker-wrap').children("input[type='color']").trigger('click');
    // }
  });

  $(".color-picker-wrap input[type='color']").on("change", function() {
    var self = $(this);

    self
      .parents(".color-picker-wrap")
      .children("ul")
      .children("li")
      .removeClass("active");

    // self.parents('.color-picker-wrap').children('ul').children('li.add_new').remove();

    self
      .parents(".color-picker-wrap")
      .children("ul")
      .append(
        '<li class="active" title="Custom Color ' +
          self.val() +
          '" style="background-color:' +
          self.val() +
          '"></li>'
      );

    self
      .parents(".color-picker-wrap")
      .children(".color-picker")
      .val(self.val());

    // self.parents('.color-picker-wrap').children('ul').append('<li class="add_new" title="Add New">+</li>');

    if (
      self
        .parents(".color-picker-wrap")
        .children(".color-picker")
        .hasClass("cp-show")
    ) {
      self
        .parents(".color-picker-wrap")
        .children("small")
        .remove();

      self
        .parents(".color-picker-wrap")
        .append(
          "<small>Selected Color: <code>" + self.val() + "</code></small>"
        );
    }
  });

  var hexDigits = new Array(
    "0",
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "a",
    "b",
    "c",
    "d",
    "e",
    "f"
  );

  function rgb2hex(rgb) {
    rgb = rgb.match(/^rgb\((\d+),\s*(\d+),\s*(\d+)\)$/);

    return "#" + hex(rgb[1]) + hex(rgb[2]) + hex(rgb[3]);
  }

  function hex(x) {
    return isNaN(x) ? "00" : hexDigits[(x - (x % 16)) / 16] + hexDigits[x % 16];
  }
});

// document.getElementById('colorpicker').addEventListener('change', function () {
//   console.log("hihihi");
//   currentColor = this.value;
// });
// document.getElementById('bgcolorpicker').addEventListener('change', function () {
//   ctx.fillStyle = this.value;
//   ctx.fillRect(0, 0, canvas.width, canvas.height);
//   redraw();
//   currentBg = ctx.fillStyle;
// });
// document.getElementById("controlSize").addEventListener("change", function() {
//   currentSize = this.value;
//   document.getElementById("showSize").innerHTML = this.value;
// });
document.getElementById("uploadimage").addEventListener(
  "click",
  function() {
    upload("canvas");
  },
  false
);
// document.getElementById("eraser").addEventListener("click", eraser);
// document.getElementById("clear").addEventListener("click", createCanvas);

// REDRAW

function redraw() {
  for (var i = 1; i < linesArray.length; i++) {
    ctx.beginPath();
    ctx.moveTo(linesArray[i - 1].x, linesArray[i - 1].y);
    ctx.lineWidth = linesArray[i].size;
    ctx.lineCap = "round";
    ctx.strokeStyle = linesArray[i].color;
    ctx.lineTo(linesArray[i].x, linesArray[i].y);
    ctx.stroke();
  }
}

// DRAWING EVENT HANDLERS

// canvas.addEventListener("mousedown", function() {
//   mousedown(canvas, event);
// });
// canvas.addEventListener("mousemove", function() {
//   mousemove(canvas, event);
// });
// canvas.addEventListener("mouseup", mouseup);

// CREATE CANVAS

// function createCanvas() {
//   canvas.id = "canvas";
//   let x = document.getElementById("image").width;
//   // TODO figure out how to get this to be 100% of parent...
//   canvas.width = x;
//   canvas.height = x;
//   // canvas.style.zIndex = 8;
//   canvas.style.position = "absolute";
//   canvas.style.border = "1px solid";
//   ctx.fillStyle = currentBg;
//   ctx.fillRect(0, 0, canvas.width, canvas.height);
//   body.appendChild(canvas);
// }

// DOWNLOAD CANVAS

// function downloadCanvas(link, canvas, filename) {
//   link.href = document.getElementById(canvas).toDataURL();
//   link.download = filename;
// }

// UPLOAD CANVAS

function upload(canvas) {
  // TODO change
  // var dataURL = document.getElementById(canvas).toDataURL("image/png");
  var dataURL = myBoard.getImg();
  console.log(dataURL);
  let img = document.getElementById("image");
  img.src = "/img/loading.gif"; // TODO fix this to use a better gif

  fetch("/upload", {
    method: "POST",
    body: dataURL
  })
    .then(response => response.json())
    .then(r => {
      let x = r.location;
      let img = document.getElementById("image");
      console.log("img", img.src);
      img.src = "/" + x;
      console.log(img.src);
    });
}

// function eraser() {
//   currentSize = 50;
//   currentColor = ctx.fillStyle;
// }

// GET MOUSE POSITION

// function getMousePos(canvas, evt) {
//   var rect = canvas.getBoundingClientRect();
//   return {
//     x: evt.clientX - rect.left,
//     y: evt.clientY - rect.top
//   };
// }

// ON MOUSE DOWN

function mousedown(canvas, evt) {
  var mousePos = getMousePos(canvas, evt);
  isMouseDown = true;
  var currentPosition = getMousePos(canvas, evt);
  ctx.moveTo(currentPosition.x, currentPosition.y);
  ctx.beginPath();
  ctx.lineWidth = currentSize;
  ctx.lineCap = "round";
  ctx.strokeStyle = currentColor;
}

// ON MOUSE MOVE

function mousemove(canvas, evt) {
  if (isMouseDown) {
    var currentPosition = getMousePos(canvas, evt);
    // if (currentPosition.x > canvas.width || currentPosition.y > canvas.height) {
    //   console.log("far off");
    //   isMouseDown = false;
    //   return;
    // }
    ctx.lineTo(currentPosition.x, currentPosition.y);
    ctx.stroke();
    store(currentPosition.x, currentPosition.y, currentSize, currentColor);
  }
}

// STORE DATA

function store(x, y, s, c) {
  var line = {
    x: x,
    y: y,
    size: s,
    color: c
  };
  linesArray.push(line);
}

// ON MOUSE UP

function mouseup() {
  isMouseDown = false;
  store();
}

function sky() {
  currentColor = "rgba(117,158,223)";
}
function sand() {
  currentColor = "rgba(44,30,22)";
}
function sea() {
  currentColor = "rgba(56,79,131)";
}

console.log(myBoard.color);
