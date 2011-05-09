function onLoad() {
	x$(document.body).setStyle('height', screen.height + 'px');
	document.addEventListener("deviceready", onDeviceReady, false);
}

function onDeviceReady() {
	x$(document.body).inner('onDeviceReady()');
}
