
const Note = require("../models/note.model.js")

// Note create handler
exports.create = (req, res) => {
    //Request validator
    if (!req.body.content) {
        return res.status(400).send({
            message: " Note content cant be empty"
        })
    }
    
    //Create note
    const note = new Note({
        title: req.body.title || "Untitled",
        content: req.body.content
        
    })
    
    // Save note
    note.save().then(data => res.send(data)
    ).catch(err => {
        res.status(500).send({
            message: err.message || "An error occured while creating a note"
        })
    })
}

// All notes find handler
exports.findAll = (req, res) => {
    Note.find().then(notes => res.send(notes)).catch(error => {
        res.status(500).send({
            message: error.message || "An error occured while retreiving notes"
        })
    })
}

// single note find handler
exports.findOne = (req, res) => {
    Note.findById(req.params.noteId)
    .then(note => {
        if (!note) {
            res.status(404).send({
                message: "Note not found"
            })
        }
        
        res.send(note)
    }).catch(error => {
        if (error.kind === 'ObjectId') {
            return res.status(404).send({
                message: `No note found with id ${req.params.noteId}`
            })
        }
        
        res.status(500).send({
            message: "Error retreiving Note"
        })
    })
}

// Note update handler
exports.update = (req, res) => {
    // Validate Request
    if (!req.params.content) {
        return res.status(400).send({
            message: "Note content cant be empty"
        })
    }
    
    //Find and update not with new content
    Note.findByIdAndUpdate(req.params.noteId, {
        title: req.body.title || "Untitled",
        content: req.body.content
    }, {new:true}).then(note => {
        if (!note) {
            return res.status(404).send({
                message: "Note not found"
            })
        }
    }).catch(err => {
        if (err.kind === 'ObjectId') {
            return res.status(404).send({
                message: `Nite with id ${req.params.noteId} not found`
            })
        }
        
        return res.status(500).send({
            message: "Error updating note"
        })
    })
    
}

//Note delete handler
exports.delete = (req, res) => {
    Note.findByIdAndRemove(req.params.noteId).then(note => {
        if (!note) {
            return res.status(404).send({
                message: "Note not found"
            })
        }
        
        res.send({
            message: "Not deleted"
        })
    }).catch(err => {
        if (err.kind === 'ObjectId' || err.name === "NotFound") {
            res.status(404).send({
                message: "Note not found"
            })
        }
        
        res.status(500).send({
            message: "Could not delete note"
        })
    })
}

