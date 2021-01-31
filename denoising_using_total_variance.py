import cv2
from matplotlib import pyplot as plt
from skimage import io, img_as_float
from skimage.restoration import denoise_tv_chambolle

img = img_as_float(io.imread('images/noisy/noisy_gaussian.jpg'))

# plt.hist(img.flat, bins=100, range=(0, 1))

# plt.show()

denoise_img = denoise_tv_chambolle(img, weight=0.1, eps=0.0002, n_iter_max=200, multichannel=True)
io.imsave('images/chambolle_denois.jpg', denoise_img)

plt.hist(denoise_img.flat, bins=100, range=(0, 1))  # .flat returns the flattened numpy array (1D)

cv2.imshow("Original", img)
cv2.imshow("TV Filtered", denoise_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
