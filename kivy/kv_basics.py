
from kivy.app import App
from kivy.uix.button import Button

class ButtonApp(App):
	def build(self):
		return Button()
		
	def do_something(self):
		with open("work.txt", "w") as w:
			w.write("You pressed the button")
			
		
"""
Kivy automatically looks for a file (with *.kv) with the same name as the class without the 'App' part of the class and in lowercase. This means in this case that it will load 'button.kv'
"""	
		

if __name__ == "__main__":
	ButtonApp().run()