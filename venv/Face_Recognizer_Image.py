import cv2

f_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
image = cv2.imread('1.jpg')

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

faces = f_cascade.detectMultiScale(gray_image, scaleFactor=1.05, minNeighbors=5)

print(type(faces))
print(faces)

for x, y, w, h in faces:
    image = cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 3)

cv2.imshow("Example", image)

cv2.waitKey(0)

cv2.destroyAllWindows()
