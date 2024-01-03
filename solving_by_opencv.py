import cv2 as cv
import numpy as np 


#### READ THE MODEL WEIGHTS



#### 1. Preprocessing Image
def preProcess(img):
    # Convert the image to gray color
    imgGray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    # Blur the gray_img for every 5x5 
    imgBlur = cv.GaussianBlur(imgGray, (5,5), 1)
    # 
    imgThreshold_1 = cv.adaptiveThreshold(imgBlur, 255, 1, 1, 11, 2)
    # imgThreshold_2 = cv.adaptiveThreshold(imgBlur, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 2)
    #cv.imshow('1', imgThreshold_1)
    # cv.imshow('2', imgThreshold_2)
    return imgThreshold_1

# print(cv.ADAPTIVE_THRESH_MEAN_C)
# print( cv.THRESH_BINARY)

def biggestContour(contours):
    biggest = np.array([])
    max_area = 0
    for i in contours:
        print(i)
        print("LEN == ",len(i))
        area = cv.contourArea(i)
        print(area)
        if area > 50:
            peri = cv.arcLength(i, True)
            # print("PERI ==",peri)
            #Approximate the shape of the contours 
            approx = cv.approxPolyDP(i, 0.02 * peri, True)
            if area > max_area and len(approx) == 4:
                biggest = approx
                max_area = area 
    return biggest, max_area

def reorder(myPoints):
    # print(myPoints)
    myPoints = myPoints.reshape((4,2))
    newPoints = np.zeros((4,1,2), dtype=np.int32)

    add = myPoints.sum(1)
    # print(add)
    # Top Left point
    newPoints[0] = myPoints[np.argmin(add)]
    # Bottom Right point
    newPoints[3] = myPoints[np.argmax(add)]

    diff = np.diff(myPoints,axis=1)
    # print(diff)
    # Top Right point
    newPoints[1] = myPoints[np.argmin(diff)]
    # Bottom Left point
    newPoints[2] = myPoints[np.argmax(diff)]
    # print(newPoints)
    return newPoints

def splitBoxes(img):
    res = []
    # Split vertically (by row)
    rows = np.vsplit(img,9)
    for i in rows:
        # Split horizontally (by columns)
        column = np.hsplit(i,9)
        for j in column:
            res.append(j)
    return res
