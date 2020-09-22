import requests

d = requests.get("https://raw.githubusercontent.com/opencv/opencv/master/data/haarcascades/haarcascade_frontalface_default.xml").content

with open("face_detector.xml", 'wb') as f:
	f.write(d)
	print("Ok")
	