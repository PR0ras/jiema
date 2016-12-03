import cv2
import numpy as np

def detect(image):
    # from rgb to hsv
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    #creat the hsv's image X and Y
    # scharr need to use ksize = -1
    gradX = cv2.Sobel(gray, ddepth = cv2.cv.CV_32F, dx = 1, dy = 0, ksize = -1)
    gradY = cv2.Sobel(gray, ddepth = cv2.cv.CV_32F, dx = 0, dy = 1, ksize = -1)
    #from x - y
    gradient = cv2.subtract(gradX, gradY)
    gradient = cv2.convertScaleAbs(gradient)
    # er zhi hua
    blurred = cv2.blur(gradient, (9, 9),0)
    ret,th1 = cv2.threshold(blurred, 225, 255, cv2.THRESH_BINARY)
    # xing tai xue cao zuo

    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 6))
    closed = cv2.morphologyEx(th1, cv2.MORPH_CLOSE, kernel)
    # fushi and pengzhang

    closed = cv2.erode(closed, None, iterations = 4)
    closed = cv2.dilate(closed, None, iterations = 4)
    # find contours
    (cnts, _) = cv2.findContours(closed.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    if len(cnts) == 0:
        return None
    #
    c = sorted(cnts, key = cv2.contourArea, reverse = True)[0]
    rect = cv2.minAreaRect(c)
    #
    box = np.int0(cv2.cv.BoxPoints(rect))
    #
    return box
