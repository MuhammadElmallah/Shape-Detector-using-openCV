import cv2
from shapeDetector import ShapeDetector

img = cv2.imread('shapes_and_colors.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (5, 5), 0)
thresh = cv2.threshold(blur, 60, 255, cv2.THRESH_BINARY)[1]

(cnts, _) = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

sd = ShapeDetector()

e = 10e-6
for c in cnts:
    M = cv2.moments(c)
    CX = int(M['m10'] / (M['m00'] + e))
    CY = int(M['m01'] / (M['m00'] + e))
    shape = sd.detect(c)
    cv2.drawContours(img, [c], -1, (255, 255, 255), 3)
    cv2.circle(img, (CX, CY), 3, (255, 255, 255), -1)
    cv2.putText(img, shape, (CX + 10, CY + 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)

cv2.imshow("Final Output", img)
cv2.waitKey(0)
