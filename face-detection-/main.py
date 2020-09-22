import cv2

#Load cascade
face_cascade = cv2.CascadeClassifier("face_detector.xml")

# Read image
img = cv2.imread('yourimage.jpg')

faces = face_cascade.detectMultiScale(img, 1.1, 4)

for (x,y,w,h) in faces:
	cv2.rectangle(img, (x, y), (x+w,y+h), (255,0,0), 2)
	
# Export result
cv2.imwrite("detected_face.png", img)
print("Success")