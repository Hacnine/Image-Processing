from skimage.feature import blob_log
from skimage.io import imread

img = imread('images/men2.gif', as_gray=True)
blobe_log = blob_log(img, max_sigma=30, num_sigma=10, threshold=.4)
numrows = len(blobe_log)
print(numrows)

#  4344 1265
