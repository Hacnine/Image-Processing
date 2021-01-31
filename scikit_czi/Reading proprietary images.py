import tifffile
from skimage import io

img = tifffile.imread("tiff_file.tiff")
import numpy as np
print(np.shape(img))
img = io.imread('tiff_file.tiff')
print(img.shape)