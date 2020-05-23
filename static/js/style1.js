//hide the buttons noy used
 function fade23Btns() {
  var btn2 = document.getElementById("btn2")
  var btn3 = document.getElementById("btn3");
  if (btn2.style.display === "none" && btn3.style.display === "none") {
    btn2.style.display = "block";
    btn3.style.display = "block";
  } else {
    btn2.style.display = "none";
    btn3.style.display = "none";
  }
}



