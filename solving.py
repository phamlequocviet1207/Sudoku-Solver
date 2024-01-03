import cv2 as cv 
import numpy as np 
from opencv_run import *

pathImage = "image_1.png"
heightImg = 450
widthImg = 450

#### 1. READ THE IMAGE
img = cv.imread(pathImage)
img = cv.resize(img, (widthImg,heightImg))
imgBlank = np.zeros((heightImg, widthImg), dtype='uint8')
imgThreshold = preProcess(img)
# cv.imshow('Thres', imgThreshold)


#### 2. FIND ALL CONTOURS
imgContours = img.copy()
imgBigContour = img.copy()
contours, hierarchy = cv.findContours(imgThreshold, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
print(contours)
#print(hierarchy)
# Draw all detected contours
cv.drawContours(imgContours, contours, -1, (0,255,0), 3)
cv.imshow('Con',imgContours)
# cv.rectangle(imgContours,(115,19), (330,370), (0,0,255), 5)


#### 4. FIND THE BIGGEST CONTOUR AND USE IT AS SUDOKU
biggest, maxArea = biggestContour(contours)
# cv.rectangle(img, (207,32), (586,660), (0,0,255) , 5)
# cv.imshow('Rec', img)
#
# print(biggest)
# print(maxArea)

if biggest.size != 0:
    biggest = reorder(biggest)
    cv.drawContours(imgBigContour, biggest, -1, (0,0,255), 15)
    # cv.imshow('i',imgBigContour)
    pts1= np.float32(biggest)
    pts2 = np.float32([[0,0], [widthImg,0],[0,heightImg],[widthImg,heightImg]])
    matrix = cv.getPerspectiveTransform(pts1,pts2)
    imgWrapColored = cv.warpPerspective(img, matrix, (widthImg, heightImg))
    imgDetectedDigits = imgBlank.copy()

    # cv.imshow('l',imgWrapColored)

    #### Split the image
    imgSolvedDigits = imgBlank.copy()
    boxes = splitBoxes(imgWrapColored)
    # print(len(boxes))
    
cv.waitKey(0)