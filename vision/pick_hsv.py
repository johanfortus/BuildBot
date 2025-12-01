import cv2
import numpy as np

img = cv2.imread("images/sample.png")
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)


def nothing(x):
    pass


# Create window
cv2.namedWindow("HSV Picker")

# Trackbars
cv2.createTrackbar("H min", "HSV Picker", 0, 179, nothing)
cv2.createTrackbar("H max", "HSV Picker", 179, 179, nothing)
cv2.createTrackbar("S min", "HSV Picker", 0, 255, nothing)
cv2.createTrackbar("S max", "HSV Picker", 255, 255, nothing)
cv2.createTrackbar("V min", "HSV Picker", 0, 255, nothing)
cv2.createTrackbar("V max", "HSV Picker", 255, 255, nothing)

while True:
    h_min = cv2.getTrackbarPos("H min", "HSV Picker")
    h_max = cv2.getTrackbarPos("H max", "HSV Picker")
    s_min = cv2.getTrackbarPos("S min", "HSV Picker")
    s_max = cv2.getTrackbarPos("S max", "HSV Picker")
    v_min = cv2.getTrackbarPos("V min", "HSV Picker")
    v_max = cv2.getTrackbarPos("V max", "HSV Picker")

    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])

    mask = cv2.inRange(hsv, lower, upper)
    vis = cv2.bitwise_and(img, img, mask=mask)

    cv2.imshow("HSV Picker", vis)
    if cv2.waitKey(1) & 0xFF == 27:  # ESC
        print("LOWER =", lower)
        print("UPPER =", upper)
        break

cv2.destroyAllWindows()
