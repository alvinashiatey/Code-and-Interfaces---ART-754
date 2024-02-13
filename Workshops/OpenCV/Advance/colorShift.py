import cv2
import numpy as np


def shift_channel(c, amount):
    if amount > 0:
        c = np.roll(c, amount, axis=0)
    elif amount < 0:
        c = np.roll(c, amount, axis=1)
    if amount != 0:
        c[:amount, :] = 0
        c[:, :amount] = 0
    return c


# Load the image
image = cv2.imread('/Users/alvinkwabena/Documents/Alvin Ashiatey/Class/Code and Interfaces - ART 754/Workshops/OpenCV/img.png')

# Split the image into its channel components
b, g, r = cv2.split(image)

# Shift the channels
b_shifted = shift_channel(b, -5)  # Shift blue channel to the left
r_shifted = shift_channel(r, 5)   # Shift red channel to the right

# Reconstruct the shifted image
glitch_image = cv2.merge([b_shifted, g, r_shifted])

# Display the original and glitched images
cv2.imshow('Original Image', image)
cv2.imshow('Glitch Art', glitch_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
