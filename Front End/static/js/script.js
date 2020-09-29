window.addEventListener("load", () => {
  console.log("helloooooooooo");
  const canvas = document.querySelector("#canvas");
  const ctx = canvas.getContext("2d");

  canvas.height = 500; //window.innerHeight;
  canvas.width = 500; //window.innerWidth;

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

    document.getElementById("loader").style.visibility = "visible";
    document.getElementById("loader_text").style.visibility = "visible";
    document.getElementById("mousepos").style.visibility = "visible";
  }

  canvas.addEventListener("mousedown", startPos);
  canvas.addEventListener("mouseup", stopPos);
  canvas.addEventListener("mousemove", draw);

  inactivityTime();
});

function showCoords(event) {
  var x = event.clientX;
  var y = event.clientY;
  var coor = "Calculating Mouse Position - X coords: " + x + ", Y coords: " + y;
  document.getElementById("mousepos").innerHTML = coor;
}

function clearCoor() {
  document.getElementById("mousepos").innerHTML = "";
}

function downloaded() {
  var download = document.getElementById("downloader");
  var image = document
    .getElementById("canvas")
    .toDataURL("image/jpeg")
    .replace("image/jpeg", "image/octet-stream");
  download.setAttribute("href", image);
}

function link_send() {
  var link_transfer = document.getElementById("link");
  var canvas = document.getElementById("canvas");
  var dataURL = canvas.toDataURL();
  link_transfer.setAttribute("value", dataURL);
}

if (document.getElementById("answer").innerText != "") {
  document.getElementById("loader").style.top = "25%";
} else {
  document.getElementById("loader").style.top = "37%";
}

var inactivityTime = function () {
  var time;

  document.onload = resetTimer;
  document.onmousemove = resetTimer;
  document.onmousedown = resetTimer; // touchscreen presses
  document.ontouchstart = resetTimer;
  document.onclick = resetTimer; // touchpad clicks
  document.onkeypress = resetTimer;
  document.addEventListener("scroll", resetTimer, true); // improved; see comments

  function btn_blink() {
    document.getElementById("submit_link").style.animation = "glowing 1300ms infinite";
    //location.href = 'logout.html'
  }

  function resetTimer() {
    clearTimeout(time);
    time = setTimeout(btn_blink, 6000);
    // 1000 milliseconds = 1 second
  }
};
