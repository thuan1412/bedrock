import cv2
import math
import numpy as np

img = cv2.imread('001.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 80, 120)
lines = cv2.HoughLinesP(edges, 1, math.pi/2, 2, None, 30, 1)

# get text block
def block_text(line, height=20, width=200):
    y_max = line[1]
    x_max = line[0]
    x_min = x_max - width
    y_min = y_max - height
    if x_min < 30:
        x_min = 30
    return ((x_max, y_max), (x_min, y_min))

def remove_noise(lines):
    arr = []
    for i in range(len(lines)-1):
        for j in range(i+1, len(lines)):
            if abs(lines[i][1] - lines[j][1]) <5 and abs(lines[i][0]-lines[j][0])<20:
                arr.append(i)
    pre = np.delete(lines, arr, axis=0)
    return pre

if isinstance(lines, np.ndarray):
    lines = lines.reshape(-1, 4)
    lines = remove_noise(lines)
    for i in lines:
        pass
    for line in lines:
        pt1 = (line[0], line[1])
        pt2 = (line[2], line[3])
        # cv2.line(img, pt1, pt2, (0, 0, 255), 1)
        cv2.rectangle(img, block_text(line)[0], block_text(line)[1], (0, 0, 255), 1)
cv2.imshow('img', img)
cv2.waitKey()
cv2.destroyAllWindows()