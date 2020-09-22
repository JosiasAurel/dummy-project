
// Import deps
const express = require("express")

const bodyParser = require("express")

const mongoose = require("mongoose")

mongoose.Promise = global.Promise


// import database configuration
const dbConfig = require('./config/database.config.js')

//Connecting to the database
mongoose.connect(dbConfig.url, {
    useNewUrlParser: true
}).then(() => console.log("Successfully connnected")).catch(err => console.log(err))

//initialize app Object
const app = express()


//Extend app with request parsing url-encoded
app.use(bodyParser.urlencoded({extended: true}))

//Extend app with JSON parsing ability
app.use(bodyParser.json())


app.get("/", (request, response) => {
    response.json({"info": "Hello World"})
})


// Load the routes/endpoints hand
const routes = require("./app/routes/note.routes.js")(app)


app.listen(3000, () => console.log("Listening on port 3000"))


