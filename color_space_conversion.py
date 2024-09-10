'''
Demonstrate color space conversion from BGR to HSV using cv2 Library.
'''

import cv2
import urllib.request
import numpy as np 

# Download image
url = "https://tinypng.com/images/social/website.jpg"
resp = urllib.request.urlopen(url)
image_array = np.array(bytearray(resp.read()), dtype=np.uint8)

# Covert image array to an OpenCV image type
image = cv2.imdecode(image_array, -1)

# Download local image
# image = cv2.imread('path/to/your/local_image.jpg')

# Image is in RGB color space by default
# Covert from RGB/BGR color space to HSV color space
# RGB: red green blue
# HSV: hue saturation value/brightness
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Display results
cv2.imshow('Original', image)
cv2.imshow('HSV Image', hsv_image)
cv2.waitKey(0)
cv2.destroyAllWindows()