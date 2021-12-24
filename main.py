import cv2
import easyocr
from logs_init import logger
from db_appliance import createTable, insertResult
from get_timestamp import getCurrentTime, getCurrentDate

# Resource path
img_path = "Resources/image5.jpg"
clasiffier_path = "Resources/haarcascade_russian_plate_number.xml"

frameWidth = 640
frameHeight = 480
minArea = 500
color = (0, 255, 0)
count = 0


def loadClassifier(clasiffier_path):
    try:
        np_cascade = cv2.CascadeClassifier(clasiffier_path)
    except cv2.error as e:
        logger.error("Failed to load cascade clasiffier")
    finally:
        return np_cascade


def loadPicture(img_path):
    try:
        data_img = cv2.imread(img_path)
    except:
        logger.error("Failed to load image")
    finally:
        return data_img


logger.info("INITIAL RECORD")
nPlateCascade = loadClassifier(clasiffier_path)
img = loadPicture(img_path)
cv2.imshow("IMG", img)
cv2.waitKey(0)

# Main image processing
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
numberPlates = nPlateCascade.detectMultiScale(imgGray, 1.1, 10)
for (x, y, w, h) in numberPlates:
    area = w * h
    if area > minArea:
        imgPlate = img[y : y + h, x : x + w]
        cv2.imshow("PLATE", imgPlate)
        cv2.waitKey(0)
        logger.info("CONFIRMED NUMPLATE PRESENCE")
    else:
        logger.error("No numplates was found")
# Registration number recognition
try:
    reader = easyocr.Reader(["en"])
    result = reader.readtext(imgPlate)
    logger.info("SUCCESSFUL NUMBER RECOGNITION")
except:
    logger.error("Failed to recognize digits")

# Placing text result on image
text = result[0][-2]
res = cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)
res = cv2.putText(img, text, (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)
cv2.imshow("RES", res)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Add the result to the database
try:
    createTable(getCurrentDate())
    insertResult(getCurrentDate(), getCurrentTime(), img_path, text)
    logger.info("RESULTS APPENDED TO DATABASE\n")
except:
    logger.error("Failed to append results\n")
