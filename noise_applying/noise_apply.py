
import cv2
import numpy as np
from skimage.util import random_noise

# Load the image
img = cv2.imread("../images/Osteosarcoma_01.tif")

# Add salt-and-pepper noise to the image.
noise_img = random_noise(img, mode='s&p', amount=0.01)
# noise_img = random_noise(img, mode='speckle', seed=None, clip=True)


# The above function returns a floating-point image
# on the range [0, 1], thus we changed it to 'uint8'
# and from [0,255]
noise_img = np.array(255 * noise_img, dtype='uint8')

# Display the noise image
cv2.imshow('blur', noise_img)
from skimage import io
io.imsave('images/noisy/noisy_salt_peakle.jpg', noise_img)
cv2.waitKey(0)