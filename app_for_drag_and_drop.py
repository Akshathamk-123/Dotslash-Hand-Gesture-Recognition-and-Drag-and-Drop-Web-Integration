import cv2
from cvzone.HandTrackingModule import HandDetector
import cvzone
import os
import math

cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

detector = HandDetector(detectionCon=0.8)


def calculate_distance(lmList, point1, point2):
    x1, y1 = lmList[point1][1], lmList[point1][2]
    x2, y2 = lmList[point2][1], lmList[point2][2]
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return distance


class DragImg():
    def __init__(self, path, posOrigin, imgType):

        self.posOrigin = posOrigin
        self.imgType = imgType
        self.path = path

        if self.imgType == 'png':
            self.img = cv2.imread(self.path, cv2.IMREAD_UNCHANGED)
        else:
            self.img = cv2.imread(self.path)

        self.size = self.img.shape[:2]

    def update(self, cursor):
        ox, oy = self.posOrigin
        h, w = self.size

        if ox < cursor[0] < ox + w and oy < cursor[1] < oy + h:
            self.posOrigin = cursor[0] - w // 2, cursor[1] - h // 2

    def draw(self, img):
        h, w = self.size
        ox, oy = self.posOrigin

        if self.imgType == "png":
            img = cvzone.overlayPNG(img, self.img, [ox, oy])
        else:
            img[oy:oy + h, ox:ox + w] = self.img

        return img


path = "ImagesPNG"
myList = os.listdir(path)

listImg = []
for x, pathImg in enumerate(myList):
    if 'png' in pathImg:
        imgType = 'png'
    else:
        imgType = 'jpg'
    listImg.append(DragImg(f'{path}/{pathImg}', [50 + x * 300, 50], imgType))

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    hands, img = detector.findHands(img, flipType=False)

    if hands:
        lmList = hands[0]['lmList']
        length = calculate_distance(lmList, 8, 12)

        if length < 60:
            cursor = lmList[8]
            for imgObject in listImg:
                imgObject.update(cursor)

    for imgObject in listImg:
        img = imgObject.draw(img)

    cv2.imshow("Image", img)
    cv2.waitKey(1)
