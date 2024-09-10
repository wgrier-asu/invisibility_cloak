'''
Test out your red invisibility cloak!
'''
import cv2
import time
import numpy as np 

MAX_TIME_S = 10 # maximum video length in seconds
OUT_FILE = 'output.avi'
# For writing output video
fourcc = cv2.VideoWriter_fourcc(*'XVID') # Codec for the video compression
out = cv2.VideoWriter(OUT_FILE, fourcc, 20.0, (640, 480)) # Output video file

# Initialize webcam
#   OpenCV VideoCapture Documentation
#   https://docs.opencv.org/3.4/d8/dfe/classcv_1_1VideoCapture.html#a5d5f5dacb77bbebdcbfb341e3d4355c1 
cam = cv2.VideoCapture(0) # VideoCapture(string filename, int apiPreference: 0=default camera)

# Wait for camera to stabilize
time.sleep(2)

# Capture background image
for i in range(60):
    success, background = cam.read()

if not success:
    print('ERROR: VideoCapture failed!')
    exit()
else:
    print('Background Image Captured.\nStarting Capture...')

start = time.time()
count = 0
while cam.isOpened():
    now = time.time()
    if (now-start) > MAX_TIME_S:
        break
    success, image = cam.read()

    if not success:
        print('ERROR: VideoCapture failed!')
        break

    count +=1 

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

    mask_inv = cv2.bitwise_not(mask) # Inverted mask

    res1 = cv2.bitwise_and(image, image, mask=mask_inv) # Retain non-red areas of the image

    res2 = cv2.bitwise_and(background, background, mask=mask) # Replace red areas with background

    # Generating the final output and writing it to the video file
    finalOutput = cv2.addWeighted(res1, 1, res2, 1.2, 0) # Combine both images to create the invisibility effect
    out.write(finalOutput) # Write the output to the video file

print('Capture Complete!')
print(f'Video saved to {OUT_FILE}')
# Release the webcam and output file, and close all OpenCV windows
cam.release()
out.release()
cv2.destroyAllWindows()
