import cv2
import numpy as np

# Load the image
image = cv2.imread('/Users/alvinkwabena/Documents/Alvin Ashiatey/Class/Code and Interfaces - ART 754/Workshops/OpenCV/img.png', cv2.IMREAD_GRAYSCALE)

# Apply Gaussian Blur to smooth the image and reduce noise
blurred_image = cv2.GaussianBlur(image, (5, 5), 0)

# Perform Canny edge detection
edges = cv2.Canny(blurred_image, threshold1=100, threshold2=200)

# Display the original and the edge-detected images
cv2.imshow('Original Image', image)
cv2.imshow('Canny Edge Detection', edges)

cv2.waitKey(0)
cv2.destroyAllWindows()
