extends Node

signal created

# Called when the node enters the scene tree for the first time.
func _ready():
	emit_signal("created")
	$Timer.connect("timeout", self, "_on_Timer_timeout")

# Called every frame. 'delta' is the elapsed time since the previous frame.
#func _process(delta):
#	pass


func _on_Timer_timeout():
	$Sprite.visible = !$Sprite.visible
