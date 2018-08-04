$(document).ready(function() {
	sessionStorage.hostname = "http://127.0.0.1:5000/";
	sessionStorage.port = ":5000";
})

$(document).on("click", "#nav_quests", function() {
	fadeOutAll(300);
	$("#quests_menu").fadeIn(300);
})

$(document).on("click", "#nav_eduquest", function() {
	fadeOutAll(300);
	$("#status_menu").fadeIn(300);
})

$(document).on("click", "#quests_menu li", function() {
	fadeOutAll(300);
	$("#quests_grid").fadeIn(300);
	$("#quests_grid h1").text($(this).find("a").text());
})

function fadeOutAll(time) {
	$("#status_menu").fadeOut(time);
	$("#quests_menu").fadeOut(time);
	$("#quests_grid").fadeOut(time);
}
