'''
Create a red color mask of an input image
'''
import cv2
import time
import numpy as np 

# Initialize webcam
#   OpenCV VideoCapture Documentation
#   https://docs.opencv.org/3.4/d8/dfe/classcv_1_1VideoCapture.html#a5d5f5dacb77bbebdcbfb341e3d4355c1 
cam = cv2.VideoCapture(0) # VideoCapture(string filename, int apiPreference: 0=default camera)

# Wait for camera to stabilize
cv2.waitKey(1000)

# Capture 60 frames, use last frame
for i in range(60):
    success, image = cam.read()

if not success:
    print('ERROR: VideoCapture failed!')
    exit()

cam.release()

# Convert color space to HSV
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Color (Hue) Masks [Hue, Saturation, Value]
lower_red = np.array([0, 120, 5])
upper_red = np.array([20, 255, 255])
mask1 = cv2.inRange(hsv, lower_red, upper_red)

lower_red = np.array([160, 120, 40])
upper_red = np.array([180, 255, 255])
mask2 = cv2.inRange(hsv, lower_red, upper_red)

# Combine masks
mask = mask1 + mask2
# Improve Mask Quality
kernel = np.ones((5,5),np.uint8)
mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel) # Noise removal
mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel) # Close holes within mask
mask = cv2.morphologyEx(mask, cv2.MORPH_DILATE, kernel, iterations=4) # Expand mask


# Show the mask for red color detection
cv2.imshow("Red Color Mask", mask)
cv2.imshow("HSV Image", hsv)
cv2.waitKey(10000)
cv2.destroyAllWindows()
