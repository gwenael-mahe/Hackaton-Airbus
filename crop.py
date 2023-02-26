import matplotlib.pyplot as plt
from skimage import io

from data_import import get_img_list


# Réduit la taille de l'image

source_folder = 'DB1'
dest_folder = 'DB1_crop'

affichage = False

img_list = get_img_list('\\' + source_folder)

#img = io.imread('DB1\\3\DB1_1_018.png')
#img = io.imread('DB1\\3\DB1_9_027.png')
#img = io.imread('DB1\\3\DB1_22_002.png')

for nom in img_list.file_name:
    if nom.__contains__('_018.'):
        left = 300
        top = 300
        right = 600
        bottom = 600

        # left = 200
        # top = 200
        # right = 700
        # bottom = 700

    elif nom.__contains__('_027.'):
        left = 300
        top = 450
        right = 600
        bottom = 750

        # left = 250
        # top = 300
        # right = 750
        # bottom = 800

    elif nom.__contains__('_002.'):
        left = 450
        top = 350
        right = 750
        bottom = 650

        # left = 350
        # top = 250
        # right = 850
        # bottom = 750

    img = io.imread(source_folder + '\\' + nom)
    img_crop = img[top:bottom, left:right]
    
    # Filtre noir sur les pixels blancs

    img_crop[img_crop == 65535] = 0

    io.imsave(dest_folder + '\\' + nom, img_crop)


# Affichage des images

if affichage:

    plt.figure(figsize=(5, 5))
    ax = plt.subplot(1, 2, 1)
    io.imshow(img)
    plt.title('ORIGINAL')
    plt.axis("off")

    ax = plt.subplot(1, 2, 2)
    io.imshow(img_crop)
    plt.title('CROP')
    plt.axis("off")

    plt.show()