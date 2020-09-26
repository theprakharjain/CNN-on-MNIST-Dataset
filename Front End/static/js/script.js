window.addEventListener("load", () => {
  console.log("helloooooooooo");
  const canvas = document.querySelector("#canvas");
  const ctx = canvas.getContext("2d");

  canvas.height = 600; //window.innerHeight;
  canvas.width = 600; //window.innerWidth;

  // Variable

  let painting = false;

  function startPos(event) {
    painting = true;
    draw(event);
  }

  function stopPos() {
    painting = false;
    ctx.beginPath();
  }

  function draw(event) {
    if (!painting) return;

    var x = event.clientX;
    var y = event.clientY;

    ctx.lineWidth = 89;
    ctx.lineCap = "round";
    ctx.strokeStyle = "white";

    ctx.lineTo(x, y);
    ctx.stroke();

    ctx.beginPath();
    ctx.moveTo(x, y);
  }

  canvas.addEventListener("mousedown", startPos);
  canvas.addEventListener("mouseup", stopPos);
  canvas.addEventListener("mousemove", draw);
});

function showCoords(event) {
  var x = event.clientX;
  var y = event.clientY;
  var coor = "X coords: " + x + ", Y coords: " + y;
  document.getElementById("demo").innerHTML = coor;
}

function clearCoor() {
  document.getElementById("demo").innerHTML = "Mouse Position";
}

// // var image = canvas.toDataURL("image/jpeg", 1.0);

// function saveimg() {
//   // window.location.href = image;
//   // document.write('<img src="' + image + '"/>');
//   var image = canvas.toDataURL("image/jpeg", 1.0);
// }

function downloaded() {
  var download = document.getElementById("downloader");
  var image = document
    .getElementById("canvas")
    .toDataURL("image/jpeg")
    .replace("image/jpeg", "image/octet-stream");
  download.setAttribute("href", image);
}
