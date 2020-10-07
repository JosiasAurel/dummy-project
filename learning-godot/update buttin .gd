extends Panel

var s
var my_new_scene = load("res://play-test.tscn")
var new_node = my_new_scene.instance()
func _ready():
	s = Sprite.new()
	add_child(s)
	print(s)
	s.queue_free()
	print(s)
	add_child(new_node)
	get_node("Button").connect("pressed", self, "_on_mybutton_pressed")

func _on_mybutton_pressed():
	get_node("Label").text = "you clicked me ! screw you ;"



