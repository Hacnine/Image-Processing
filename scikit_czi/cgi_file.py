import czifile

img = czifile.imread('../Osteosarcoma_01.czi')
print(img.shape)

img1 = img[0, 0, :, :, :, 0]
print(img1.shape)

# Next, let us extract each channel image.
img2 = img1[0, :, :]  # First channel, Red
img3 = img1[1, :, :]  # Second channel, Green
img4 = img1[2, :, :]  # Third channel, Blue DAPI

from matplotlib import pyplot as plt

fig = plt.figure(figsize=(10, 10))

ax1 = fig.add_subplot(2, 2, 1)
ax1.imshow(img2, cmap='hot')
ax1.title.set_text('1st channel')
# plt.savefig('redish1.jpg')

ax2 = fig.add_subplot(2, 2, 2)
ax2.imshow(img3, cmap='hot')
ax2.title.set_text('2nd channel')

ax3 = fig.add_subplot(2, 2, 3)
ax3.imshow(img4, cmap='hot')
ax3.title.set_text('3rd channel')
plt.savefig('redish.jpg')
plt.show()
