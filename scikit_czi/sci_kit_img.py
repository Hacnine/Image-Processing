import cv2
from skimage import io, img_as_float

img = io.imread('win_sky.jpg')
# print(img.shape)
io.imshow(img)
# io.show()

img_float = img_as_float(img)
# print(img_float)

# img_np = img.astype(np.float)

# img_8bit = img_as_ubyte(img_float)

# grey image
img_cv = cv2.imread('../win_sky.jpg')
io.imshow(img_cv)
cv2.imwrite('../grey.jpg', img_cv)
io.show()

# black and white
grey_img_cv2 = cv2.imread('../win_sky.jpg', 0)
io.imshow(grey_img_cv2)
# io.show()

color_img_cv2 = cv2.imread('../win_sky.jpg', 3)
io.imshow(color_img_cv2)
# io.show()
