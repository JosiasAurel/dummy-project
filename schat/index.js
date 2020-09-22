
const express = require("express")

const app = express()

const http = require("http").createServer(app)

const io = require("socket.io")(http)

/*
app.get("/", (req, res) => {
    res.sendFile(__dirname + '/public/index.html')
})
*/

app.use(express.static("public"))

io.on("connection", (socket) => {
    console.log("A user connected")
    socket.on("disconnect", () => {
        console.log("A user disconnected")
    })
    socket.on("chat message", (msg) => {
        console.log(msg)
        io.emit("chat message", msg)
    })
})

http.listen(3000, () => {
    console.log("Working on port 3000")
})