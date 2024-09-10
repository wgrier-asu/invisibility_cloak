'''
Capture and save an image from the device's default video camera
'''
import cv2
import time
import numpy as np 

# Initialize webcam
#   OpenCV VideoCapture Documentation
#   https://docs.opencv.org/3.4/d8/dfe/classcv_1_1VideoCapture.html#a5d5f5dacb77bbebdcbfb341e3d4355c1 
cam = cv2.VideoCapture(0) # VideoCapture(string filename, int apiPreference: 0=default camera)

# Wait for camera to stabilize
time.sleep(3)

# Capture 60 frames, use last frame
for i in range(60):
    success, image = cam.read()

if not success:
    print('ERROR: VideoCapture failed!')
    exit()

# Flip background horizontally
background = np.flip(image, axis=1)

# Save background image
cv2.imwrite('background.jpg', background)

# Release the webcam
cam.release()