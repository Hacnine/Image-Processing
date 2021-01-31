from skimage import io, filters, img_as_ubyte
import cv2
img = io.imread('images/noisy/noisy_salt_peakle.jpg')

gaussian_img = filters.gaussian(img, sigma=3)
# io.imsave('gaussian-blur.tif', gaussian_img)

gaussian_img_8bit = img_as_ubyte(gaussian_img)
io.imsave('gaussian-blur2.tif', gaussian_img_8bit)

# cv2.imwrite('gaussian-blur3.jpg', gaussian_img_8bit)
gaussian_img_8bit_RGB = cv2.cvtColor(gaussian_img_8bit, cv2.COLOR_BGR2RGB)
cv2.imwrite('gaussian-blur3_COLOR_BGR2RGB.jpg', gaussian_img_8bit_RGB)



