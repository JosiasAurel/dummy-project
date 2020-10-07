from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.image import Image

class MyApp(App):
	def build(self):
		"""label = Label(text="Hello World from kivy",
		size_hint=(.5,.5),
		pos_hint={"center_x":.5,"center_y":.5})"""
		image = Image()
		return label
		
if __name__ == "__main__":
		MyApp().run()
		
	