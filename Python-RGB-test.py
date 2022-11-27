import cv2
import numpy as np

img = np.ones((512,512,3), np.uint8)

def nothing(x):
    pass
cv2.namedWindow("Image")
cv2.createTrackbar("R", "Image", 0,255,nothing)
cv2.createTrackbar("G", "Image", 0,255,nothing)
cv2.createTrackbar("B", "Image", 0,255,nothing)

while True:
    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == 27:
        break
    r = cv2.getTrackbarPos("R", "Image")
    g = cv2.getTrackbarPos("G", "Image")
    b = cv2.getTrackbarPos("B", "Image")

    img[:] = [b,g,r]


cv2.destroyAllWindows()