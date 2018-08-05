$(document).ready(function() {
	sessionStorage.hostname = "http://127.0.0.1";
	sessionStorage.port = ":5000/";
	$("form").submit(false);
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
	console.log($(this).attr("id"));
	$(".grid_element").attr("value", $(this).attr("id"));
})

$(document).on("click", ".grid_element.unlocked", function() {
	fadeOutAll(300);
	$("#question_box").fadeIn(300);
	$("#player").fadeIn(600);
	$("#enemy").fadeIn(600);

	initGame(0.1, $(this).attr("value") + String(parseInt($(this).attr("id").split("_")[1]) - 1));
})

/* AJAX Requests */

var solution;

function getQuestion(route) {
	$.ajax({
		method: "GET",
		dataType: "json",
		url: sessionStorage.hostname + sessionStorage.port + route,
		success: function(data) {
			console.log(route);
			console.log(data);
			$("#question").empty();
			$("#equation").empty();
			let values = data.params.split(",");
			$("#answer").attr("value", values[values.length - 1]);
			console.log($("#answer").attr("value"));
			switch (data.type) {
				case "fin":
					$("#question").text(values[0]);
					console.log(values[values.length - 1]);
					break;
				case "grad":
					$("#equation").text("Find the gradient of the line given by the equation " + values[0]);
					break;
				case "eq":
					$("#equation").text("Solve for x in the equation " + values[0]);
					break;
				case "add":
					$("#equation").text(values[0] + " + " + values[1]);
					break;
				case "ind1":
					$("#equation").append(values[0]);
					$("#equation").append("<sup>" + values[1] + "</sup>");
					break;
				case "ind2":
					$("#equation").append(values[0]);
					$("#equation").append("<sup>" + values[1] + "</sup>");
					$("#equation").append(" x ");
					$("#equation").append(values[2]);
					$("#equation").append("<sup>" + values[3] + "</sup>");
					break;
				default:
					console.log("Uncaught! " + data.type);
					break;
			}
		},
		error: function(jqXHR, textStatus, errorThrown) {
			console.log(jqXHR.responseText);
		}
	})
}

/* Utility */

function fadeOutAll(time) {
	$("#status_menu").fadeOut(time);
	$("#quests_menu").fadeOut(time);
	$("#quests_grid").fadeOut(time);
	$("#question_box").fadeOut(time);
	$("#player").fadeOut(time);
	$("#enemy").fadeOut(time);
}

var start;
var end;
var player_health;
var enemy_health;

var answer;
var q;

function resetGame(minutes) {
	start = true;
	player_health = 100;
	enemy_health = 100;
	q = 0;
	$("#player .hp_foreground").animate({"width": "100%"});
	$("#enemy .hp_foreground").animate({"width": "100%"});
	end = Date.now() + minutes * 60 * 1000;
	$("#ans_form").css("display", "block");
}

function initGame(minutes, route) {
	resetGame(minutes);
	getQuestion(route);
	$(document).off("keydown");
	$(document).on("keydown", function(e) {
		let key = (e.keyCode ? e.keyCode : e.which);
		if (key == 13) { // Enter key
			if (start) {
				checkAnswer(minutes, route);
			}
		}
		else if (key == 32) { // Space Key
			if (start) {
				skip(a, b, c, d);
			}
			else {
				$(document).off("keydown");
				init(minutes, a, b, c, d);
			}
		}
		return 0;
	});
	updateTimer(minutes);
}	

function endGame() {
	let t = $("#timer");
	if (player_health <= 0) {
		t.empty();
		t.append("Game Over!")
	}
	else if (enemy_health <= 0) {
		t.empty();
		t.append("You Win!")
	}
}

function checkAnswer(minutes, route) {
	if ($("#input_answer").val() == $("#answer").attr("value")) {
		end = Date.now() + minutes * 60 * 1000;
		getQuestion(route);
		dealDamage(25);
	}
	else {
		receiveDamage(5);
	}
	$("#input_answer").val("");
}

function updateTimer(minutes) {	
	var id = setInterval(function() {
		if (player_health <= 0 || enemy_health <= 0) {
			clearInterval(id);
		}
		let now = Date.now();
		if (now > end - 200) {
			receiveDamage(30);
			if (player_health > 0 && enemy_health > 0) {
				end = Date.now() + minutes * 60 * 1000;
			}
			else {
				clearInterval(id);
			}
		}
		let t = $("#timer");
		t.empty();
		t.append(Math.floor((end - now) / 1000));
		endGame();

	}, 100);
}

function receiveDamage(dmg) {
	player_health -= dmg;		
	$("#player .hp_foreground").animate({"width": String(player_health) + "%"});
}

function dealDamage(dmg) {
	enemy_health -= dmg;
	$("#enemy .hp_foreground").animate({"width": String(enemy_health) + "%"});
}
