import matplotlib.pyplot as plt
from skimage import io

from math import sqrt

from data_import import get_img_list


source_folder = 'DB1'
dest_folder = 'DB1_medallion'

affichage = False

img_list = get_img_list('\\' + source_folder)

# img = io.imread('DB1\DB1_1_018.png')
# img = io.imread('DB1\DB1_9_027.png')
# img = io.imread('DB1\DB1_22_002.png')

size = 1024
offset = size / 2

for nom in img_list.file_name:
    if nom.__contains__('_018.'):
        rayon = 200

    elif nom.__contains__('_027.'):
        rayon = 250

    elif nom.__contains__('_002.'):
        rayon = 230

    img = io.imread('DB1\\' + nom)

    img_medallion = img.copy()

    for x in range(size):
        for y in range(size):
            x_p = x - offset
            y_p = y - offset
        
            dist = sqrt(x_p ** 2 + y_p ** 2)

            if dist > rayon:
                img_medallion[x][y] = 0

    io.imsave(dest_folder + '\\' + nom, img_medallion)


# Affichage des images

if affichage:
        
    plt.figure(figsize=(5, 5))
    ax = plt.subplot(1, 2, 1)
    io.imshow(img)
    plt.title('ORIGINAL')
    plt.axis("off")

    ax = plt.subplot(1, 2, 2)
    io.imshow(img_medallion)
    plt.title('MEDALLION')
    plt.axis("off")

    plt.show()