var form = document.getElementById("searchForm");
var msg = document.getElementById("warn");

if (form) {
  form.addEventListener("keydown", function (e) {
    if (e.key === "Enter") {
      e.preventDefault();
      msg.style.display = "block";
    }
  });
}