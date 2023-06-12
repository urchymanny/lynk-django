let selectField = document.getElementById("id_item_type");
let text_form = document.querySelector(".text-el-form");
let web_form = document.querySelector(".web-el-form");
let yt_form = document.querySelector(".yt-el-form");

selectField.addEventListener("change", function () {
  if (selectField.value === "text") {
    text_form.style.display = "flex";
    web_form.style.display = "none";
    yt_form.style.display = "none";
  } else if (selectField.value === "link") {
    text_form.style.display = "none";
    web_form.style.display = "flex";
    yt_form.style.display = "none";
  } else if (selectField.value === "youtube") {
    text_form.style.display = "none";
    web_form.style.display = "none";
    yt_form.style.display = "flex";
  } else {
    text_form.style.display = "none";
    web_form.style.display = "none";
    yt_form.style.display = "none";
  }
});
