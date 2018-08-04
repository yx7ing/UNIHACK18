$(document).ready(function() {
	sessionStorage.hostname = "http://127.0.0.1:5000/";
	sessionStorage.port = ":5000";
})

$(document).on("click", "#nav_quests", function() {
	console.log("Hello");
	$("#status_menu").fadeOut(300);
	$("#quests_menu").fadeIn(300);
})
