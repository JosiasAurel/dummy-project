
module.exports = (app) => {
    
    const notes = require("../controllers/note.controller.js")
    
    //Note create endpoint
    app.post("/notes", notes.create)
    
    // retrieve notes
    app.get("/notes", notes.findAll)
    
    //Retrieve single note with id
    app.get("/notes/:noteId", notes.findOne
    )
    
    //Update note with id
    app.put("/notes/:noteId", notes.update)
    
    //Delete note with id
    app.delete("/notes/noteId", notes.delete)
        
    
}