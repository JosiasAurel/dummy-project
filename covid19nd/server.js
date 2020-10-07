const express = require('express')
const app = express()
const logrocket = require('logrocket')

 app.use(express.static('public'))
 
app.get('/', (req, res)=> {
   res.sendFile('index.html')
})


logrocket.init('hj2a2l/rocket');
