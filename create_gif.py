import imageio.v3 as iio
filenames = ['Thank You Lewis Desktop Wallpaper 1.jpg',
'Thank You Lewis Desktop Wallpaper 2.jpg',
'Thank You Lewis Desktop Wallpaper 3.jpg']
images = []

for filename in filenames:
    images.append(iio.imread(filename))
iio.imwrite('Thank You Lewis.gif', images, duration=500, loop = 0)