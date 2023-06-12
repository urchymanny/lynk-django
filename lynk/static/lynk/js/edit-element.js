let selectField = document.getElementById("id_item_type");
let text_form = document.querySelector(".text-el-form");
let web_form = document.querySelector(".web-el-form");
let yt_form = document.querySelector(".yt-el-form");

selectField.disabled = true;
selectField.value = selectField.value;

if (text_form != null) {
  text_form.style.display = "flex";
}
if (web_form != null) {
  web_form.style.display = "flex";
}
if (yt_form != null) {
  yt_form.style.display = "flex";
}
