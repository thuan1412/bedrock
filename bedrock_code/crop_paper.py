from transform_example import four_point_transform
from skimage.filters import threshold_local
import numpy as np
import argparse
import cv2
import imutils

image = cv2.imread('test2.png')
ratio = image.shape[0] / 500
orig = image.copy()
image= imutils.resize(image, height=500)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray, (5, 5), 0)
edged = cv2.Canny(gray, 75, 200)

cnts = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
cnts = imutils.grab_contours(cnts)
for c in cnts:
	# approximate the contour
	peri = cv2.arcLength(c, True)
	approx = cv2.approxPolyDP(c, 0.02 * peri, True)
 
	# if our approximated contour has four points, then we
	# can assume that we have found our screen
	if len(approx) == 4:
		screenCnt = approx
		break

cv2.drawContours(image, [screenCnt], -1, (0, 255, 0), 2)
# cv2.imshow("Image", image)
cv2.imshow("Edged", image)
cv2.waitKey(0)
cv2.destroyAllWindows()