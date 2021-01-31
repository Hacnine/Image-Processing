from skimage.feature import blob_log
from math import sqrt
import glob
from skimage.io import imread
import glob
from math import sqrt

from skimage.feature import blob_log
from skimage.io import imread

example_file = glob.glob("wint_sky.png")[0]
im = imread(example_file, )
# plt.imshow(im, cmap=cm.gray)
# plt.show()
blobs_log = blob_log(im, max_sigma=30, num_sigma=10, threshold=.1)
# Compute radii in the 3rd column.
blobs_log[:, 2] = blobs_log[:, 2] * sqrt(2)
numrows = len(blobs_log)
print("Number of stars counted : ", numrows)
# fig, ax = plt.subplots(1, 1)
# plt.imshow(im, cmap=cm.gray)
# for blob in blobs_log:
#     y, x, r = blob
#     c = plt.Circle((x, y), r+5, color='lime', linewidth=2, fill=False)
#     ax.add_patch(c)
