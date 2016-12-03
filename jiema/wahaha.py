import cv2
import numpy as np

image = cv2.imread('12.png',1)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

gradX = cv2.Sobel(gray, ddepth = cv2.cv.CV_32F, dx = 1, dy = 0, ksize = -1)
gradY = cv2.Sobel(gray, ddepth = cv2.cv.CV_32F, dx = 0, dy = 1, ksize = -1)

gradient = cv2.subtract(gradX, gradY)
gradient = cv2.convertScaleAbs(gradient)
cv2.imshow('gray',gradient)
#blurred = cv2.GaussianBlur(gray,(5,5),0)

blurred = cv2.blur(gradient, (9, 9),0)
ret,th1= cv2.threshold(blurred, 255, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
cv2.imshow('th1',th1)

# xiaochu fengxi
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 6))
# bi yun suan
closed = cv2.morphologyEx(th1, cv2.MORPH_CLOSE, kernel)
#closed = cv2.morphologyEx(th1, cv2.MORPH_OPEN, kernel)

#dilation = cv2.dilate(th1,kernel,iterations = 1)
#erosion = cv2.erode(th1,kernel,iterations = 1)

# fushi  pengzhang
closed = cv2.erode(closed, kernel, iterations = 4)
closed = cv2.dilate(closed, kernel, iterations = 4)
cv2.imshow('closed',closed)


cnts,hierarchy = cv2.findContours(closed.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
c = sorted(cnts, key = cv2.contourArea, reverse = True)[0]
rect = cv2.minAreaRect(c)
box = np.int0(cv2.cv.BoxPoints(rect))
print box

cv2.waitKey(0)
cv2.destroyAllWindows()
'''
cap = cv2.VideoCapture(0)
while(True):
    #
    ret,frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
'''
