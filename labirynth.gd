extends Node2D

func _on_label_draw():
	pass # Replace with function body.


func _on_button_pressed():
	get_tree().change_scene_to_file("res://node_2d.tscn")
