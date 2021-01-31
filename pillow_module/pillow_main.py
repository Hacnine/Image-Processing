import os

from PIL import Image, ImageFilter


file_300 = (250, 250)
# os.mkdir('300_image')
for file in os.listdir('..'):
    if file.endswith('.jpg') or file.endswith('.png'):
        open_images = Image.open(file)
        file_name, file_extension = os.path.splitext(file)

        # open_images.resize(file_300)
        open_images.thumbnail(file_300)
        open_images.save(f'300_image/{file_name}{file_extension}')


# change extension
for file in os.listdir('..'):
    if file.endswith('.jpg') or file.endswith('.png'):
        # print(file)
        open_images = Image.open(file)
        file_name, file_extension = os.path.splitext(file)
        # print(file_extension)
        # open_images.save(f'pngs/{file_name}.png')


image1 = Image.open('F 44426.jpg')
# image1.rotate(90).save('rotate_wint_sky.png')
image1.convert(mode='L').save('F44426h.jpg')
image1.filter(ImageFilter.GaussianBlur()).save('blur.jpg')
# to copy one image many times
# to delete many image just loop
# image1 = Image.open('img.jpg')
# for i in range(1, 11):
    # image1.save(f'quran{i}.jpg')
    # os.remove(f'quran{i}.jpg')
