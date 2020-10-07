import kivy, random

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

#color codes
red = [1,0,0,1]
green = [0,1,0,1]
blue =  [0,0,1,1]
purple = [1,0,1,1]

#Example app using horizontal box layout
class MyApp(App):
	def build(self):
		layout = BoxLayout(padding=10, spacing=5)
		colors = [red, green, blue, purple]
		for i in range(5):
			btn = Button(text=f"Button {i+1}",background_color=random.choice(colors))
			btn.bind(on_press=self.print_val)
			
			layout.add_widget(btn)
		return layout
	def print_val(self, instance):
		instance.text="Pressed"
		return
		
if __name__ == "__main__":
	MyApp().run()