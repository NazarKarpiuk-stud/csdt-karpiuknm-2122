import cv2
import easyocr

# Resource path

img_path = "Resources/image5.jpg"

frameWidth = 640
frameHeight = 480
nPlateCascade = cv2.CascadeClassifier("Resources/haarcascade_russian_plate_number.xml")
minArea = 500
color = (0, 255, 0)
count = 0

# Main image processing

img = cv2.imread(img_path)
cv2.imshow("IMG", img)
cv2.waitKey(0)

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
numberPlates = nPlateCascade.detectMultiScale(imgGray, 1.1, 10)
for (x, y, w, h) in numberPlates:
    area = w * h
    if area > minArea:
        imgPlate = img[y : y + h, x : x + w]
        cv2.imshow("PLATE", imgPlate)
        cv2.waitKey(0)

# Registration number recognition

reader = easyocr.Reader(["en"])
result = reader.readtext(imgPlate)

# Placing text result on image

text = result[0][-2]
res = cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)
res = cv2.putText(img, text, (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)
cv2.imshow("RES", res)
cv2.waitKey(0)
cv2.destroyAllWindows()