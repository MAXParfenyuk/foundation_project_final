document.getElementById("myBtn").addEventListener("click", function() {
    document.getElementById("myModal").style.display = "block";
});

document.getElementsByClassName("close")[0].addEventListener("click", function() {
    document.getElementById("myModal").style.display = "none";
});
document.getElementById("toggleTheme").addEventListener("click", function() {
    document.body.classList.toggle("dark-mode");
    localStorage.setItem("dark-mode", document.body.classList.contains("dark-mode"));
});

if (localStorage.getItem("dark-mode") === "true") {
    document.body.classList.add("dark-mode");
} else {
    document.body.classList.remove("dark-mode");
}


