import cv2

# Load the original image
image = cv2.imread('/Users/alvinkwabena/Documents/Alvin Ashiatey/Class/Code and Interfaces - ART 754/Workshops/OpenCV/img.png')

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply a thermal camera effect
thermal_image = cv2.applyColorMap(gray_image, cv2.COLORMAP_JET)

# Display the original and thermal effect images
cv2.imshow('Original Image', image)
cv2.imshow('Thermal Camera Effect', thermal_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
