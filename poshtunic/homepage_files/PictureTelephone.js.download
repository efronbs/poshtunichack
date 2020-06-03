const picTelUrl = "/PictureTelephone";

const Color = {
	RED:0,
	ORANGE:1,
	YELLOW:2,
	LIGHTGREEN:3,
	DARKGREEN:4,
	TEAL:5,
	LIGHTBLUE:6,
	DARKBLUE:7,
	PURPLE:8,
	PINK:9,
	BLACK:10,
	BROWN:11,
	LIGHTGREY:12,
	DARKGREY:13,
	MAX:14
}

const TurnAction = {
	WAITING:0,
	FIRST_WRITE:1,
	WRITE:2,
	DRAW:3,
	RESULTS:4
}

const SubmissionType = {
	EMPTY:0,
	PROMPT:1,
	DRAWING:2
}

//___________________________________
// Initialization
//___________________________________
window.onload = function() {
	document.getElementById("firstPrompt_prompt")
	.addEventListener("keyup", function(event) {
		event.preventDefault();
		if (event.keyCode === 13) { // 13 is the Enter button
			document.getElementById("firstPrompt_submit").click();
		}
	});

	document.getElementById("write_prompt")
	.addEventListener("keyup", function(event) {
		event.preventDefault();
		if (event.keyCode === 13) { // 13 is the Enter button
			document.getElementById("write_submit").click();
		}
	});
}

//___________________________________
// Main Menu
//___________________________________

function mainMenu_createGame() {
	const url = picTelUrl + "/create_game";
	postJson(url,{})
	.then((data) => {
		document.getElementById("mainPage").style.display = "none";
		createGame_onCreate(data.id);
	});
}

function mainMenu_joinGame() {
	document.getElementById("mainPage").style.display = "none";
	joinGame_onCreate();
}

function mainMenu_showInstructions() {
	document.getElementById("mainPage").style.display = "none";
	document.getElementById("instructionsPage").style.display = "block";
}

//___________________________________
// Instructions
//___________________________________

function instructions_back() {
	document.getElementById("instructionsPage").style.display = "none";
	document.getElementById("mainPage").style.display = "block";
}

//___________________________________
// Create Game Page
//___________________________________

// True when the left mouse is button is down
var createGame_clicking = false;

var createGame_selectedColor = Color.RED;

var createGame_prevX = 0;
var createGame_prevY = 0;
var createGame_currX = 0;
var createGame_currY = 0;

function createGame_onCreate(gameId) {
	document.getElementById("createGamePage").style.display = "block";
	document.getElementById("createGame_gameId").innerHTML = gameId;

	var canvas = document.getElementById('createGame_canvas');

	// Clear the previous image if there was one
	clearCanvas(canvas);

	canvas.addEventListener("mousemove", createGame_onMouseMove, false);
	canvas.addEventListener("touchmove", createGame_onTouchMove, false);

	canvas.addEventListener("mousedown", createGame_onMouseDown, false);
	canvas.addEventListener("touchstart", createGame_onTouchDown, false);

	canvas.addEventListener("mouseup", createGame_onCursorUp, false);
	canvas.addEventListener("mouseout", createGame_onCursorUp, false);
	canvas.addEventListener("touchend", createGame_onCursorUp, false);

	// Add a border to the default selected color
	createGame_selectedColor = Color.RED;
	document.getElementById('createGame_redBox').style.border = "4px solid #ABABD9";
	for (var i=Color.ORANGE; i<Color.MAX; i++) {
		document.getElementById(createGame_getDivIdFromColor(i)).style.border = "4px solid #D3D3E8";
	}

	// Clear the error if there previously was one
	document.getElementById("createGame_error").innerHTML = "";
}

function createGame_onMouseMove(event) {
	createGame_onCursorMove(event.offsetX, event.offsetY);
}

function createGame_onTouchMove(event) {
	var touch = event.touches[0];
	var canvas = document.getElementById('createGame_canvas');
	const rect = canvas.getBoundingClientRect();
	createGame_onCursorMove(touch.clientX - rect.left,touch.clientY - rect.top);
}

function createGame_onCursorMove(offsetX, offsetY) {
	if (createGame_clicking) {
		var canvas = document.getElementById('createGame_canvas');
		createGame_prevX = createGame_currX;
		createGame_prevY = createGame_currY;
		createGame_currX = offsetX;
		createGame_currY = offsetY;
		context = canvas.getContext("2d");
		draw(context,
			createGame_prevX,
			createGame_prevY,
			createGame_currX,
			createGame_currY,
			colorEnumToHex(createGame_selectedColor))
	}
}

function createGame_onMouseDown(event) {
	createGame_onCursorDown(event.offsetX, event.offsetY);
}

function createGame_onTouchDown(event) {
	var touch = event.touches[0];
	var canvas = document.getElementById('createGame_canvas');
	const rect = canvas.getBoundingClientRect();
	createGame_onCursorDown(touch.clientX - rect.left,touch.clientY - rect.top);
}

function createGame_onCursorDown(offsetX, offsetY) {
	var canvas = document.getElementById('createGame_canvas');
	createGame_prevX = createGame_currX;
	createGame_prevY = createGame_currY;
	createGame_currX = offsetX;
	createGame_currY = offsetY;

	createGame_clicking = true;

	// Draw a dot where the mouse was clicked
	context = canvas.getContext("2d");
	context.beginPath();
	context.fillStyle = colorEnumToHex(createGame_selectedColor);
	context.fillRect(createGame_currX, createGame_currY, 6, 6);
	context.closePath();
}

function createGame_onCursorUp(event) {
	createGame_clicking = false;
}

function createGame_changeColor(div) {
	// Remove the border from the previously selected color
	var previousColorDivId = createGame_getDivIdFromColor(createGame_selectedColor);
	document.getElementById(previousColorDivId).style.border = "4px solid #D3D3E8";

	// Update the selected color
	createGame_selectedColor = createGame_getColorFromDivId(div.id);

	// Add a border to the newly selected color
	div.style.border = "4px solid #ABABD9";

	// Change the color of all the pixels that the user already drew on
	createGame_changeDrawingColor(createGame_selectedColor);
}

function createGame_getColorFromDivId(divId) {
	switch(divId) {
	case "createGame_redBox":
		return Color.RED;
	case "createGame_yellowBox":
		return Color.YELLOW;
	case "createGame_lightgreenBox":
		return Color.LIGHTGREEN;
	case "createGame_lightblueBox":
		return Color.LIGHTBLUE;
	case "createGame_pinkBox":
		return Color.PINK;
	case "createGame_lightgreyBox":
		return Color.LIGHTGREY;
	case "createGame_brownBox":
		return Color.BROWN;
	case "createGame_orangeBox":
		return Color.ORANGE;
	case "createGame_tealBox":
		return Color.TEAL;
	case "createGame_darkgreenBox":
		return Color.DARKGREEN;
	case "createGame_darkblueBox":
		return Color.DARKBLUE;
	case "createGame_purpleBox":
		return Color.PURPLE;
	case "createGame_darkgreyBox":
		return Color.DARKGREY;
	case "createGame_blackBox":
		return Color.BLACK;
	}
}

function createGame_getDivIdFromColor(color) {
	switch(color) {
	case Color.RED:
		return "createGame_redBox";
	case Color.YELLOW:
		return "createGame_yellowBox";
	case Color.LIGHTGREEN:
		return "createGame_lightgreenBox";
	case Color.LIGHTBLUE:
		return "createGame_lightblueBox";
	case Color.PINK:
		return "createGame_pinkBox";
	case Color.LIGHTGREY:
		return "createGame_lightgreyBox";
	case Color.BROWN:
		return "createGame_brownBox";
	case Color.ORANGE:
		return "createGame_orangeBox";
	case Color.TEAL:
		return "createGame_tealBox";
	case Color.DARKGREEN:
		return "createGame_darkgreenBox";
	case Color.DARKBLUE:
		return "createGame_darkblueBox";
	case Color.PURPLE:
		return "createGame_purpleBox";
	case Color.DARKGREY:
		return "createGame_darkgreyBox";
	case Color.BLACK:
		return "createGame_blackBox";
	}
}

function createGame_changeDrawingColor(color) {
	var hexColor = colorEnumToHex(color);
	var canvas = document.getElementById('createGame_canvas');
	var context = canvas.getContext("2d");
	var imageData = context.getImageData(0, 0, canvas.width, canvas.height);
	for (var i=0;i< imageData.data.length;i+=4) {
		var pixelIsWhite = ((imageData.data[i] == 0xFF) && (imageData.data[i+1] == 0xFF) && (imageData.data[i+2] == 0xFF))
		if (!pixelIsWhite) {
			imageData.data[i] = parseInt("0x" + (hexColor.substr(1,2)), 16);
			imageData.data[i+1] = parseInt("0x" + (hexColor.substr(3,2)), 16);
			imageData.data[i+2] = parseInt("0x" + (hexColor.substr(5,2)), 16);
		}
	}
	context.putImageData(imageData,0,0);
}

function createGame_create() {
	// Create a new multipart form
	var formData = new FormData();

	// Add the Game ID to the form
	const gameId = document.getElementById("createGame_gameId").innerHTML;
	formData.append("gameId",gameId);

	// Add the color to the form
	formData.append("color", createGame_selectedColor);

	// Add the drawing to the form
	var canvas = document.getElementById('createGame_canvas');
	const dataURL = canvas.toDataURL("image/png");
	formData.append("playerImage", dataURItoBlob(dataURL));
	const url = picTelUrl + "/add_player";
	postMultipartForm(url,formData)
	.then((data) => {
		if (data.error == 0) {
			createGame_onDestroy();
			hostLobby_onCreate(gameId, createGame_selectedColor);
		}
		else {
			showError("createGame_error", data.error);
		}
	});
}

function createGame_back() {
	createGame_onDestroy();
	document.getElementById("mainPage").style.display = "block";
}

function createGame_onDestroy() {
	var canvas = document.getElementById("createGame_canvas");
	canvas.removeEventListener("mousemove", createGame_onMouseMove, false);
	canvas.removeEventListener("touchmove", createGame_onTouchMove, false);
	canvas.removeEventListener("mousedown", createGame_onMouseDown, false);
	canvas.removeEventListener("touchstart", createGame_onTouchDown, false);
	canvas.removeEventListener("mouseup", createGame_onCursorUp, false);
	canvas.removeEventListener("mouseout", createGame_onCursorUp, false);
	canvas.removeEventListener("touchend", createGame_onCursorUp, false);

	document.getElementById("createGamePage").style.display = "none";
}

//___________________________________
// Host Lobby
//___________________________________

var hostLobby_playerColor = Color.RED;
var hostLobby_playerRequestTimerId;
var hostLobby_colorsInTable = [];

function hostLobby_onCreate(gameId, playerColor) {
	document.getElementById("hostLobbyPage").style.display = "block";
	document.getElementById("hostLobby_gameId").innerHTML = gameId;

	hostLobby_playerColor = playerColor;

	// Clear the error if there previously was one
	document.getElementById("hostLobby_error").innerHTML = "";

	// Clear the table that holds the player images
	document.getElementById("hostLobby_playerContainer").innerHTML = ""

	// Start the periodic requests for players
	hostLobby_playerRequestTimerId = setInterval(hostLobby_requestPlayers, 1000, gameId);

	// Clear colorsInTable
	hostLobby_colorsInTable = [];
}

function hostLobby_requestPlayers(gameId) {
	var url = picTelUrl + "/players?gameId=" + gameId + "&color=" + hostLobby_playerColor;
	getJson(url)
	.then((data) => {
		var playerListHasChanged = checkIfPlayerListHasChanged(data.players, hostLobby_colorsInTable);

		if (playerListHasChanged) {
			playerContainer = document.getElementById("hostLobby_playerContainer");
			playerContainer.innerHTML = "";
			hostLobby_colorsInTable = [];
			for (const player of data.players) {
				hostLobby_colorsInTable.push(player.color);
				var imageUrl = formDrawingFileUrl(gameId, getColorString(player.color));
				img = document.createElement("img");
				img.id = "hostLobby_" + getColorString(player.color) + "PlayerImage";
				img.className = "playerImage";
				img.src = imageUrl;
				img.alt = getColorString(player.color) + " player";
				playerContainer.appendChild(img);
			}
		}
	})
}

function hostLobby_start() {
	const gameName = document.getElementById("hostLobby_gameId").innerHTML;
	const gameToStart = {gameId: gameName};
	const url = picTelUrl + "/start_game";
	postJson(url,gameToStart)
	.then((data) => {
		if (data.error == 0) {
			hostLobby_onDestroy();
			showNextTurnPage(gameName, hostLobby_playerColor);
		} else {
			showError("hostLobby_error", data.error);
		}
	});
}

function hostLobby_onDestroy() {
	document.getElementById("hostLobbyPage").style.display = "none";
	clearInterval(hostLobby_playerRequestTimerId);
}

//___________________________________
// Join Game Page
//___________________________________

// True when the left mouse is button is down
var joinGame_clicking = false;

var joinGame_selectedColor = Color.RED;

var joinGame_prevX = 0;
var joinGame_prevY = 0;
var joinGame_currX = 0;
var joinGame_currY = 0;

function joinGame_onCreate() {
	document.getElementById("joinGamePage").style.display = "block";

	var canvas = document.getElementById('joinGame_canvas');

	// Clear the previous image if there was one
	clearCanvas(canvas);

	canvas.addEventListener("mousemove", joinGame_onMouseMove, false);
	canvas.addEventListener("touchmove", joinGame_onTouchMove, false);

	canvas.addEventListener("mousedown", joinGame_onMouseDown, false);
	canvas.addEventListener("touchstart", joinGame_onTouchDown, false);

	canvas.addEventListener("mouseup", joinGame_onCursorUp, false);
	canvas.addEventListener("mouseout", joinGame_onCursorUp, false);
	canvas.addEventListener("touchend", joinGame_onCursorUp, false);

	// Add a border to the default selected color
	joinGame_selectedColor = Color.RED;
	document.getElementById('joinGame_redBox').style.border = "4px solid #ABABD9";
	for (var i=Color.ORANGE; i<Color.MAX; i++) {
		document.getElementById(joinGame_getDivIdFromColor(i)).style.border = "4px solid #D3D3E8";
	}

	// Clear the error
	document.getElementById("joinGame_error").innerHTML = "";

	document.getElementById("joinGame_gameId").value = "";
}

function joinGame_onMouseMove(event) {
	joinGame_onCursorMove(event.offsetX, event.offsetY);
}

function joinGame_onTouchMove(event) {
	var touch = event.touches[0];
	var canvas = document.getElementById('joinGame_canvas');
	const rect = canvas.getBoundingClientRect();
	joinGame_onCursorMove(touch.clientX - rect.left,touch.clientY - rect.top);
}

function joinGame_onCursorMove(offsetX, offsetY) {
	if (joinGame_clicking) {
		var canvas = document.getElementById('joinGame_canvas');
		joinGame_prevX = joinGame_currX;
		joinGame_prevY = joinGame_currY;
		joinGame_currX = offsetX;
		joinGame_currY = offsetY;
		context = canvas.getContext("2d");
		draw(context,
			joinGame_prevX,
			joinGame_prevY,
			joinGame_currX,
			joinGame_currY,
			colorEnumToHex(joinGame_selectedColor))
	}
}

function joinGame_onMouseDown(event) {
	joinGame_onCursorDown(event.offsetX, event.offsetY)
}

function joinGame_onTouchDown(event) {
	var touch = event.touches[0];
	var canvas = document.getElementById('joinGame_canvas');
	const rect = canvas.getBoundingClientRect();
	joinGame_onCursorDown(touch.clientX - rect.left,touch.clientY - rect.top);
}

function joinGame_onCursorDown(offsetX, offsetY) {
	var canvas = document.getElementById('joinGame_canvas');
	joinGame_prevX = joinGame_currX;
	joinGame_prevY = joinGame_currY;
	joinGame_currX = offsetX;
	joinGame_currY = offsetY;

	joinGame_clicking = true;

	// Draw a dot where the mouse was clicked
	context = canvas.getContext("2d");
	context.beginPath();
	context.fillStyle = colorEnumToHex(joinGame_selectedColor);
	context.fillRect(joinGame_currX, joinGame_currY, 6, 6);
	context.closePath();
}

function joinGame_onCursorUp(event) {
	joinGame_clicking = false;
}

function joinGame_changeColor(div) {
	// Remove the border from the previously selected color
	var previousColorDivId = joinGame_getDivIdFromColor(joinGame_selectedColor);
	document.getElementById(previousColorDivId).style.border = "4px solid #D3D3E8";

	// Update the selected color
	joinGame_selectedColor = joinGame_getColorFromDivId(div.id);

	// Add a border to the newly selected color
	div.style.border = "4px solid #ABABD9";

	// Change the color of all the pixels that the user already drew on
	joinGame_changeDrawingColor(joinGame_selectedColor);
}

function joinGame_getColorFromDivId(divId) {
	switch(divId) {
	case "joinGame_redBox":
		return Color.RED;
	case "joinGame_yellowBox":
		return Color.YELLOW;
	case "joinGame_lightgreenBox":
		return Color.LIGHTGREEN;
	case "joinGame_lightblueBox":
		return Color.LIGHTBLUE;
	case "joinGame_pinkBox":
		return Color.PINK;
	case "joinGame_lightgreyBox":
		return Color.LIGHTGREY;
	case "joinGame_brownBox":
		return Color.BROWN;
	case "joinGame_orangeBox":
		return Color.ORANGE;
	case "joinGame_tealBox":
		return Color.TEAL;
	case "joinGame_darkgreenBox":
		return Color.DARKGREEN;
	case "joinGame_darkblueBox":
		return Color.DARKBLUE;
	case "joinGame_purpleBox":
		return Color.PURPLE;
	case "joinGame_darkgreyBox":
		return Color.DARKGREY;
	case "joinGame_blackBox":
		return Color.BLACK;
	}
}

function joinGame_getDivIdFromColor(color) {
	switch(color) {
	case Color.RED:
		return "joinGame_redBox";
	case Color.YELLOW:
		return "joinGame_yellowBox";
	case Color.LIGHTGREEN:
		return "joinGame_lightgreenBox";
	case Color.LIGHTBLUE:
		return "joinGame_lightblueBox";
	case Color.PINK:
		return "joinGame_pinkBox";
	case Color.LIGHTGREY:
		return "joinGame_lightgreyBox";
	case Color.BROWN:
		return "joinGame_brownBox";
	case Color.ORANGE:
		return "joinGame_orangeBox";
	case Color.TEAL:
		return "joinGame_tealBox";
	case Color.DARKGREEN:
		return "joinGame_darkgreenBox";
	case Color.DARKBLUE:
		return "joinGame_darkblueBox";
	case Color.PURPLE:
		return "joinGame_purpleBox";
	case Color.DARKGREY:
		return "joinGame_darkgreyBox";
	case Color.BLACK:
		return "joinGame_blackBox";
	}
}

function joinGame_changeDrawingColor(color) {
	var hexColor = colorEnumToHex(color);
	var canvas = document.getElementById('joinGame_canvas');
	var context = canvas.getContext("2d");
	var imageData = context.getImageData(0, 0, canvas.width, canvas.height);
	for (var i=0;i< imageData.data.length;i+=4) {
		var pixelIsWhite = ((imageData.data[i] == 0xFF) && (imageData.data[i+1] == 0xFF) && (imageData.data[i+2] == 0xFF))
		if (!pixelIsWhite) {
			imageData.data[i] = parseInt("0x" + (hexColor.substr(1,2)), 16);
			imageData.data[i+1] = parseInt("0x" + (hexColor.substr(3,2)), 16);
			imageData.data[i+2] = parseInt("0x" + (hexColor.substr(5,2)), 16);
		}
	}
	context.putImageData(imageData,0,0);
}

function joinGame_join() {
	// Create a new multipart form
	var formData = new FormData();

	// Add the Game ID to the form
	const gameId = document.getElementById("joinGame_gameId").value;
	formData.append("gameId",gameId);

	// Add the color to the form
	formData.append("color", joinGame_selectedColor);

	// Add the drawing to the form
	var canvas = document.getElementById('joinGame_canvas');
	const dataURL = canvas.toDataURL("image/png");
	formData.append("playerImage", dataURItoBlob(dataURL));
	const url = picTelUrl + "/add_player";
	postMultipartForm(url,formData)
	.then((data) => {
		if (data.error == 0) {
			joinGame_onDestroy();
			joinerLobby_onCreate(gameId, joinGame_selectedColor);
		}
		else {
			showError("joinGame_error", data.error);
		}
	});
}

function joinGame_back() {
	joinGame_onDestroy();
	document.getElementById("mainPage").style.display = "block";
}

function joinGame_onDestroy() {
	var canvas = document.getElementById("joinGame_canvas");
	canvas.removeEventListener("mousemove", joinGame_onMouseMove, false);
	canvas.removeEventListener("touchmove", joinGame_onTouchMove, false);
	canvas.removeEventListener("mousedown", joinGame_onMouseDown, false);
	canvas.removeEventListener("touchstart", joinGame_onTouchDown, false);
	canvas.removeEventListener("mouseup", joinGame_onCursorUp, false);
	canvas.removeEventListener("mouseout", joinGame_onCursorUp, false);
	canvas.removeEventListener("touchend", joinGame_onCursorUp, false);

	document.getElementById("joinGamePage").style.display = "none";
}

//___________________________________
// Joiner Lobby
//___________________________________

var joinerLobby_playerColor = Color.RED;
var joinerLobby_playerRequestTimerId;
var joinerLobby_gameStatusTimerId;
var joinerLobby_colorsInTable = [];

function joinerLobby_onCreate(gameId, playerColor) {
	document.getElementById("joinerLobbyPage").style.display = "block";
	document.getElementById("joinerLobby_gameId").innerHTML = gameId;

	joinerLobby_playerColor = playerColor;

	// Clear the table that holds the player images
	document.getElementById("joinerLobby_playerContainer").innerHTML = ""

	// Start the periodic requests for players
	joinerLobby_playerRequestTimerId = setInterval(joinerLobby_requestPlayers, 1000, gameId);

	// Start the periodic requests for the game status
	joinerLobby_gameStatusTimerId = setInterval(joinerLobby_requestGameStatus, 1000, gameId);

	// Clear colorsInTable
	joinerLobby_colorsInTable = [];
}

function joinerLobby_requestPlayers(gameId) {
	var url = picTelUrl + "/players?gameId=" + gameId + "&color=" + joinerLobby_playerColor;
	getJson(url)
	.then((data) => {
		var playerListHasChanged = checkIfPlayerListHasChanged(data.players, joinerLobby_colorsInTable);

		if (playerListHasChanged) {
			playerContainer = document.getElementById("joinerLobby_playerContainer");
			playerContainer.innerHTML = "";
			joinerLobby_colorsInTable = [];
			for (const player of data.players) {
				joinerLobby_colorsInTable.push(player.color);
				var imageUrl = formDrawingFileUrl(gameId, getColorString(player.color));
				img = document.createElement("img");
				img.id = "joinerLobby_" + getColorString(player.color) + "PlayerImage";
				img.className = "playerImage";
				img.src = imageUrl;
				img.alt = getColorString(player.color) + " player";
				playerContainer.appendChild(img);
			}
		}
	})
}

function joinerLobby_requestGameStatus(gameId) {
	var url = picTelUrl + "/game_status?gameId=" + gameId;
	getJson(url)
	.then((data) => {
		if (data.gameStarted) {
			joinerLobby_onDestroy();
			gameId = document.getElementById("joinerLobby_gameId").innerHTML;
			showNextTurnPage(gameId, joinerLobby_playerColor);
		}
	})
}

function joinerLobby_onDestroy() {
	document.getElementById("joinerLobbyPage").style.display = "none";
	clearInterval(joinerLobby_playerRequestTimerId);
	clearInterval(joinerLobby_gameStatusTimerId);
}

//___________________________________
// First Prompt Page
//___________________________________

var firstPrompt_playerColor;
var firstPrompt_gameId;
var firstPrompt_heartbeatTimer;

function firstPrompt_onCreate(gameId, playerColor, targetColor) {
	document.getElementById("firstPromptPage").style.display = "block";

	firstPrompt_playerColor = playerColor;
	firstPrompt_gameId = gameId;

	// Set the target image
	document.getElementById("firstPrompt_targetImage").src = formDrawingFileUrl(gameId, targetColor);

	document.getElementById("firstPrompt_error").innerHTML = "";

	document.getElementById("firstPrompt_prompt").value = "";

	// Start the periodic posting of heartbeats
	firstPrompt_heartbeatTimer = setInterval(postHeartbeat, 1000, gameId, firstPrompt_playerColor);
}

// TODO this is where guesses are submitted
function firstPrompt_submit() {
	// Create a new multipart form
	var formData = new FormData();

	// Add the Game ID to the form
	formData.append("gameId", firstPrompt_gameId);

	// Add the color to the form
	formData.append("color", firstPrompt_playerColor);

	// Add the prompt to the form
	formData.append("prompt", document.getElementById("firstPrompt_prompt").value);

	// Add the submission type to the form
	formData.append("type", SubmissionType.PROMPT);

	const url = picTelUrl + "/submit";
	postMultipartForm(url,formData)
	.then((data) => {
		if (data.error == 0) {
			firstPrompt_onDestroy();
			showNextTurnPage(firstPrompt_gameId, firstPrompt_playerColor);
		}
		else {
			showError("firstPrompt_error", data.error);
		}
	});
}

function firstPrompt_onDestroy() {
	document.getElementById("firstPromptPage").style.display = "none";
	clearInterval(firstPrompt_heartbeatTimer);
}

//___________________________________
// Waiting Page
//___________________________________

var waiting_playerStatusTimerId
var waiting_nextTurnTimerId;
var waiting_tableInitialized = false;

function waiting_onCreate(gameId, color) {
	// Clear the player status table
	clearTable("waiting_playerTable");
	waiting_tableInitialized = false;

	document.getElementById("waitingPage").style.display = "block";

	// Start the periodic requests for the player status
	waiting_playerStatusTimerId = setInterval(waiting_requestPlayerStatus, 1000, gameId, color);

	// Start the periodic requests for the next turn
	waiting_nextTurnTimerId = setInterval(waiting_requestNextTurn, 1000, gameId, color);
}

function waiting_requestPlayerStatus(gameId, color) {
	const getPlayersUrl = picTelUrl + "/players?gameId=" + gameId + "&color=" + color;
	getJson(getPlayersUrl)
	.then((data) => {
		playerTable = document.getElementById("waiting_playerTable");
		if (!waiting_tableInitialized) {
			var rowIndex = 1;
			for (const player of data.players) {
				var newRow = playerTable.insertRow(rowIndex);

				// Insert the player Image
				var playerImageCell = newRow.insertCell(0);
				img = document.createElement("img");
				var imageUrl = formDrawingFileUrl(gameId, getColorString(player.color));
				img.id = "waiting_" + getColorString(player.color) + "PlayerImage";
				img.className = "playerImage";
				img.src = imageUrl;
				img.alt = getColorString(player.color) + " player";
				playerImageCell.appendChild(img);

				// Insert the connected status
				var connectedCell = newRow.insertCell(1);
				if (player.connected) {
					connectedCell.innerHTML = "yes";
				} else {
					connectedCell.innerHTML = "no";
				}

				// Insert the screen
				var screenCell = newRow.insertCell(2);
				screenCell.innerHTML = getTurnActionText(player.turnAction);

				rowIndex++;
			}

			waiting_tableInitialized = true;
		} else {
			var rowIndex = 1;
			for (const player of data.players) {
				var row = playerTable.rows[rowIndex];

				// Update the connected status
				if (player.connected) {
					row.cells[1].innerHTML = "yes";
				} else {
					row.cells[1].innerHTML = "no";
				}

				// Update the screen status
				row.cells[2].innerHTML = getTurnActionText(player.turnAction);

				rowIndex++;
			}
		}
	});
}

function waiting_requestNextTurn(gameId, color) {
	nextTurnUrl =  picTelUrl + "/next_turn?gameId=" + gameId + "&color=" + color;
	getJson(nextTurnUrl)
	.then((data) => {
		if (data.turnAction != TurnAction.WAITING) {
			waiting_onDestroy();

			switch (data.turnAction) {
			case TurnAction.FIRST_WRITE:
				firstPrompt_onCreate(gameId, color, data.text);
				break;
			case TurnAction.WRITE:
				write_onCreate(gameId, color, data.text);
				break;
			case TurnAction.DRAW:
				draw_onCreate(gameId, color, data.text);
				break;
			case TurnAction.RESULTS:
				results_onCreate(gameId, color);
				break;
			}
		}
	});
}

function waiting_onDestroy() {
	document.getElementById("waitingPage").style.display = "none";
	clearInterval(waiting_nextTurnTimerId);
	clearInterval(waiting_playerStatusTimerId);
}

//___________________________________
// Write Page
//___________________________________

var write_gameId;
var write_playerColor;
var write_heartbeatTimer;

function write_onCreate(gameId, color, imageUrl) {
	// Show the passed image
	document.getElementById("write_passedImage").src = imageUrl;

	write_gameId = gameId;
	write_playerColor = color;

	// Clear the error if there previously was one
	document.getElementById("write_error").innerHTML = "";

	document.getElementById("write_prompt").value = "";

	document.getElementById("writePage").style.display = "block";

	// Start the periodic posting of heartbeats
	write_heartbeatTimer = setInterval(postHeartbeat, 1000, gameId, write_playerColor);
}

function write_submit() {
	// Create a new multipart form
	var formData = new FormData();

	// Add the Game ID to the form
	formData.append("gameId", write_gameId);

	// Add the color to the form
	formData.append("color", write_playerColor);

	// Add the submission type to the form
	formData.append("type", SubmissionType.PROMPT);

	// Add the prompt to the form
	formData.append("prompt", document.getElementById("write_prompt").value);

	const url = picTelUrl + "/submit";
	postMultipartForm(url,formData)
	.then((data) => {
		if (data.error == 0) {
			write_onDestroy();
			showNextTurnPage(write_gameId, write_playerColor);
		}
		else {
			showError("write_error", data.error);
		}
	});
}

function write_onDestroy() {
	document.getElementById("writePage").style.display = "none";
	clearInterval(write_heartbeatTimer);
}

//___________________________________
// Draw Page
//___________________________________
var draw_clicking = false;
var draw_playerColor = false;
var draw_gameId;
var draw_heartbeatTimer;

var draw_prevX = 0;
var draw_prevY = 0;
var draw_currX = 0;
var draw_currY = 0;

function draw_onCreate(gameId, color, promptText) {
	var canvas = document.getElementById('draw_canvas');

	// Clear the previous image if there was one
	clearCanvas(canvas);

	document.getElementById("drawPage").style.display = "block";
	document.getElementById("draw_passedPrompt").innerHTML = promptText;

	document.getElementById("draw_error").innerHTML = "";

	draw_gameId = gameId;
	draw_playerColor = color;

	canvas.addEventListener("mousemove", draw_onMouseMove, false);
	canvas.addEventListener("touchmove", draw_onTouchMove, false);

	canvas.addEventListener("mousedown", draw_onMouseDown, false);
	canvas.addEventListener("touchstart", draw_onTouchDown, false);

	canvas.addEventListener("mouseup", draw_onCursorUp, false);
	canvas.addEventListener("mouseout", draw_onCursorUp, false);
	canvas.addEventListener("touchend", draw_onCursorUp, false);

	// Start the periodic posting of heartbeats
	draw_heartbeatTimer = setInterval(postHeartbeat, 1000, gameId, draw_playerColor);
}

function draw_onMouseMove(event) {
	draw_onCursorMove(event.offsetX, event.offsetY)
}

function draw_onTouchMove(event) {
	var touch = event.touches[0];
	var canvas = document.getElementById('draw_canvas');
	const rect = canvas.getBoundingClientRect();
	draw_onCursorMove(touch.clientX - rect.left,touch.clientY - rect.top);
}

function draw_onCursorMove(offsetX, offsetY) {
	if (draw_clicking) {
		var canvas = document.getElementById('draw_canvas');
		draw_prevX = draw_currX;
		draw_prevY = draw_currY;
		draw_currX = offsetX;
		draw_currY = offsetY;
		context = canvas.getContext("2d");
		draw(context,
			draw_prevX,
			draw_prevY,
			draw_currX,
			draw_currY,
			colorEnumToHex(draw_playerColor));
	}
}

function draw_onMouseDown(event) {
	draw_onCursorDown(event.offsetX, event.offsetY)
}

function draw_onTouchDown(event) {
	var touch = event.touches[0];
	var canvas = document.getElementById('draw_canvas');
	const rect = canvas.getBoundingClientRect();
	draw_onCursorDown(touch.clientX - rect.left,touch.clientY - rect.top);
}

function draw_onCursorDown(offsetX, offsetY) {
	var canvas = document.getElementById('draw_canvas');
	draw_prevX = draw_currX;
	draw_prevY = draw_currY;
	draw_currX = offsetX;
	draw_currY = offsetY;

	draw_clicking = true;

	// Draw a dot where the mouse was clicked
	context = canvas.getContext("2d");
	context.beginPath();
	context.fillStyle = colorEnumToHex(draw_playerColor);
	context.fillRect(draw_currX, draw_currY, 6, 6);
	context.closePath();
}

function draw_onCursorUp() {
	draw_clicking = false;
}

function draw_submit() {
	// Create a new multipart form
	var formData = new FormData();

	// Add the Game ID to the form
	formData.append("gameId", draw_gameId);

	// Add the color to the form
	formData.append("color", draw_playerColor);

	// Add the submission type to the form
	formData.append("type", SubmissionType.DRAWING);

	// Add the drawing to the form
	var canvas = document.getElementById('draw_canvas');
	const dataURL = canvas.toDataURL("image/png");
	formData.append("drawing", dataURItoBlob(dataURL));
	const url = picTelUrl + "/submit";
	postMultipartForm(url,formData)
	.then((data) => {
		if (data.error == 0) {
			draw_onDestroy();
			showNextTurnPage(draw_gameId, draw_playerColor);
		}
		else {
			showError("joinGame_error", data.error);
		}
	});
}

function draw_onDestroy() {
	var canvas = document.getElementById("draw_canvas");
	canvas.removeEventListener("mousemove", draw_onMouseMove, false);
	canvas.removeEventListener("touchmove", draw_onTouchMove, false);
	canvas.removeEventListener("mousedown", draw_onMouseDown, false);
	canvas.removeEventListener("touchstart", draw_onTouchDown, false);
	canvas.removeEventListener("mouseup", draw_onCursorUp, false);
	canvas.removeEventListener("mouseout", draw_onCursorUp, false);
	canvas.removeEventListener("touchend", draw_onCursorUp, false);

	document.getElementById("drawPage").style.display = "none";

	clearInterval(draw_heartbeatTimer);
}

//___________________________________
// Results Page
//___________________________________

function results_onCreate(gameId) {
	document.getElementById("resultsPage").style.display = "block";

	// Clear the results
	document.getElementById("results_results").innerHTML = "";

	const resultsUrl = picTelUrl + "/results?gameId=" + gameId;
	getJson(resultsUrl)
	.then((data) => {
		results_show(data);
	});
}

function results_show(results) {
	// Clear the results
	document.getElementById("results_results").innerHTML = "";

	results.forEach(function(row) {
		var newDiv = document.createElement("div");
		newDiv.style.display = "flex";
		newDiv.style.margin = "auto";
		newDiv.style.alignItems = "center";
		newDiv.style.overflow = "auto";
		for (var submissionIndex = 0; submissionIndex < row.length; submissionIndex++) {
			var submission = row[submissionIndex];
			if (submission.SubmissionType == SubmissionType.PROMPT) {
				var label = document.createElement("LABEL");
				label.innerHTML = submission.Text;
				label.style.minWidth = "200px"
				newDiv.appendChild(label);
			}
			else if (submission.SubmissionType == SubmissionType.DRAWING) {
				var image = document.createElement("img");
				image.src = submission.Text;
				image.classList.add("playerImage");
				newDiv.appendChild(image);
			}

			// Add the right arrow after the submission
			if (submissionIndex != (row.length - 1)) {
				var arrowSpan = document.createElement("SPAN");
				arrowSpan.innerHTML = "→";
				arrowSpan.classList.add("rightArrow");
				newDiv.appendChild(arrowSpan);
			}
		}

		resultsPage = document.getElementById("results_results");
		resultsPage.appendChild(newDiv);
		resultsPage.appendChild(document.createElement("br"));
	});
}

function results_newGame() {
	document.getElementById("resultsPage").style.display = "none";
	document.getElementById("mainPage").style.display = "block";
}

//___________________________________
// Utils
//___________________________________

function showNextTurnPage(gameId, color) {
	nextTurnUrl =  picTelUrl + "/next_turn?gameId=" + gameId + "&color=" + color;
	getJson(nextTurnUrl)
	.then((data) => {
		switch (data.turnAction) {
		case TurnAction.WAITING:
			waiting_onCreate(gameId, color);
			break;
		case TurnAction.FIRST_WRITE:
			firstPrompt_onCreate(gameId, color, data.text);
			break;
		case TurnAction.WRITE:
			write_onCreate(gameId, color, data.text);
			break;
		case TurnAction.DRAW:
			draw_onCreate(gameId, color, data.text);
			break;
		case TurnAction.RESULTS:
			results_onCreate(gameId);
			break;
		}
	});
}

async function getJson(url = '') {
	const response = await fetch(url);
	return await response.json();
}

async function getMultipartForm(url = "") {
	return await fetch(url);
}

async function postJson(url = '', data = {}) {
	// Default options are marked with *
	const response = await fetch(url, {
		method: 'POST', // *GET, POST, PUT, DELETE, etc.
		mode: 'cors', // no-cors, *cors, same-origin
		cache: 'no-cache', // *default, no-cache, reload, force-cache, only-if-cached
		credentials: 'same-origin', // include, *same-origin, omit
		headers: {
			'Content-Type': 'application/json'
			// 'Content-Type': 'application/x-www-form-urlencoded',
		},
		redirect: 'follow', // manual, *follow, error
		referrerPolicy: 'no-referrer', // no-referrer, *client
		body: JSON.stringify(data) // body data type must match "Content-Type" header
	});
	return await response.json(); // parses JSON response into native JavaScript objects
}

async function postMultipartForm(url,formData) {
	const response = await fetch(url, {
		method: 'POST',
		body: formData
	});
	return await response.json(); // parses JSON response into native JavaScript objects
}

function colorEnumToHex(color) {
	switch (color) {
	case Color.RED:
		return "#FF0000";
	case Color.ORANGE:
		return "#FFAA17";
	case Color.YELLOW:
		return "#E3E632";
	case Color.LIGHTGREEN:
		return "#89F51D";
	case Color.DARKGREEN:
		return "#0CC74A";
	case Color.TEAL:
		return "#27E8A5";
	case Color.LIGHTBLUE:
		return "#19E7FA";
	case Color.DARKBLUE:
		return "#1B34F2";
	case Color.PURPLE:
		return "#861DF0";
	case Color.PINK:
		return "#F06CDC";
	case Color.BLACK:
		return "#000000";
	case Color.BROWN:
		return "#AB7A1A";
	case Color.LIGHTGREY:
		return "#B5B5B5";
	case Color.DARKGREY:
		return "#737373";
	}
}

function draw(context, previousX, previousY, currentX, currentY, hexColor) {
	context.beginPath();
	context.moveTo(previousX, previousY);
	context.lineTo(currentX, currentY);
	context.strokeStyle = hexColor;
	context.lineWidth = 6;
	context.stroke();
	context.closePath();
}

function dataURItoBlob(dataURI) {
	// convert base64 to raw binary data held in a string
	// doesn't handle URLEncoded DataURIs - see SO answer #6850276 for code that does this
	var byteString = atob(dataURI.split(',')[1]);

	// separate out the mime component
	var mimeString = dataURI.split(',')[0].split(':')[1].split(';')[0];

	// write the bytes of the string to an ArrayBuffer
	var ab = new ArrayBuffer(byteString.length);
	var ia = new Uint8Array(ab);
	for (var i = 0; i < byteString.length; i++) {
		ia[i] = byteString.charCodeAt(i);
	}

	//New Code
	return new Blob([ab], {type: mimeString});
}

function showError(labelId, error)
{
	switch (error)
	{
		case 1:
			document.getElementById(labelId).innerHTML = "Game does not exist";
			break;
		case 2:
			document.getElementById(labelId).innerHTML = "Game already started";
			break;
		case 3:
			document.getElementById(labelId).innerHTML = "Not enough players to start game";
			break;
		case 4:
			document.getElementById(labelId).innerHTML = "Game has not been started";
			break;
		case 5:
			document.getElementById(labelId).innerHTML = "Player is not in this game";
			break;
		case 6:
			document.getElementById(labelId).innerHTML = "Color already taken";
			break;
		case 7:
			document.getElementById(labelId).innerHTML = "Unexpected submission";
			break;
		case 8:
			document.getElementById(labelId).innerHTML = "Unexpected submission type";
			break;
		case 9:
			document.getElementById(labelId).innerHTML = "Image read failure";
			break;
		default:
			break;
	}
}

function formDrawingFileUrl(gameId, colorString) {
	return picTelUrl + "/drawing/" + gameId + "/player_" + colorString +".png";
}

function getColorString(color) {
	switch (color) {
	case Color.RED:
		return "red";
	case Color.ORANGE:
		return "orange";
	case Color.YELLOW:
		return "yellow";
	case Color.LIGHTGREEN:
		return "lightgreen";
	case Color.DARKGREEN:
		return "darkgreen";
	case Color.TEAL:
		return "teal";
	case Color.LIGHTBLUE:
		return "lightblue";
	case Color.DARKBLUE:
		return "darkblue";
	case Color.PURPLE:
		return "purple";
	case Color.PINK:
		return "pink";
	case Color.BLACK:
		return "black";
	case Color.BROWN:
		return "brown";
	case Color.LIGHTGREY:
		return "lightgrey";
	case Color.DARKGREY:
		return "darkgrey";
	}
	return "";
}

function getTurnActionText(turnAction) {
	switch (turnAction) {
	case TurnAction.WAITING:
		return "Waiting";
	case TurnAction.FIRST_WRITE:
		return "First Write";
	case TurnAction.WRITE:
		return "Writing";
	case TurnAction.DRAW:
		return "Drawing";
	case TurnAction.RESULTS:
		return "Viewing Results";
	}
	return "";
}

function clearCanvas(canvas) {
	var context = canvas.getContext("2d");
    const w = canvas.width;
    const h = canvas.height;
	context.clearRect(0, 0, w, h);
}

function checkIfPlayerListHasChanged(receivedPlayerList, storedColorList) {
	if (receivedPlayerList.length != storedColorList.length) {
		return true;
	}
	for ( var i=0; i<receivedPlayerList.length; i++) {
		if (receivedPlayerList[i].color != storedColorList[i]) {
			return true;
		}
	}
	return false;
}

function clearTable(tableId) {
	while (document.getElementById(tableId).rows.length > 1) {
		document.getElementById(tableId).deleteRow(1)
	}
}

function postHeartbeat(gameName, playerColor) {
	const dataToPost = {gameId: gameName, color: playerColor};
	const url = picTelUrl + "/heartbeat";
	postJson(url, dataToPost)
	.then((data) => {
		// Do Nothing
	});
}
