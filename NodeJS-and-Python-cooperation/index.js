const {spawn} = require("child_process");

const dataOut = spawn("python", ['app.py']);

var info;

dataOut.stdout.on("data", (data) => {
	console.log(data.toString());
})


