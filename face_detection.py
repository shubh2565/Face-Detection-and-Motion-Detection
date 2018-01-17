import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

img = cv2.imread('mona_lisa.jpg')

img = cv2.resize(img, (int(img.shape[1]/2), int(img.shape[0]/2)))

cv2.imshow('Mona Lisa', img)
cv2.waitKey(2000)
cv2.destroyAllWindows()

gray_image = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

cv2.imshow('Mona Lisa grayscale', gray_image)
cv2.waitKey(2000)
cv2.destroyAllWindows()


faces = face_cascade.detectMultiScale(gray_image, scaleFactor = 1.05, minNeighbors = 5)

for x, y, w , h in faces:
	img = cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 3)

cv2.imshow('Mona Lisa face detected', img)
cv2.waitKey(3000)
cv2.destroyAllWindows()