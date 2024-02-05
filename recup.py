from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


## Transformation en niveau de gris

image1 = Image.open('images/image1.jpg')

img = np.array(image1.convert('L'))

plt.imshow(img,cmap='gray')
plt.axis('off')
plt.show()

## Transformation noir et blanc


## Redimensionnement d'une image

image = np.asarray(Image.open("Images/quokka.jpg"))
a0,b0,_ = image.shape

a1,b1 = 300,300
ratio_lignes = a0/a1
ratio_colonnes = b0/b1

image_sortie = np.zeros((a1,b1,3),dtype = np.uint8)
for ligne in range(a1):
    for col in range(b1):
        for i in range(3):
            image_sortie[ligne,col,i] = image[int(ligne*ratio_lignes),int(col*ratio_colonnes),i]

plt.imshow(image_sortie)
plt.axis('off')
plt.show()

## Alignement de deux images

imageSize = int((image1.size)[0]/2), int((image1.size)[1]/2)
smallImage = image1.resize(imageSize)
finalImage = Image.new('RGB',image1.size)
finalImage.paste(smallImage, (0,0))
finalImage.paste(smallImage, (imageSize[0],0))
finalImage.paste(smallImage, (0,imageSize[1]))
finalImage.paste(smallImage, (imageSize[0],imageSize[1]))

finalImage.show()

## Fusion d'images

lena = np.array(Image.open('Images/lena.png'))
mandrill = np.array(Image.open('Images/mandrill.png'))
ratio = 0.7

image_melange = ratio*lena.copy() + (1-ratio)*mandrill.copy()

plt.imshow(image_melange,cmap='gray')
plt.axis('off')
plt.show()