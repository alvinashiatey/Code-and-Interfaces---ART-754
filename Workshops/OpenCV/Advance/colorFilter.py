import cv2
import numpy as np

# Load the image
image = cv2.imread(
    '/Users/alvinkwabena/Documents/Alvin Ashiatey/Class/Code and Interfaces - ART 754/Workshops/OpenCV/img.png')

# Convert the image to the HSV color space
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Define the range of blue color in HSV
lower_blue = np.array([110, 50, 50])
upper_blue = np.array([130, 255, 255])


# Create a mask that only includes the green parts
mask = cv2.inRange(hsv, lower_blue, upper_blue)

# Bitwise-AND mask and original image to isolate the green color
green_only = cv2.bitwise_and(image, image, mask=mask)

# Display the original and the result side by side
cv2.imshow('Original Image', image)
cv2.imshow('Green Color Filtered', green_only)

cv2.waitKey(0)
cv2.destroyAllWindows()
