from PIL import Image
import numpy as np
from pathlib import Path
from datetime import datetime

DIR_UPLOADS = Path(__file__).resolve().parent / 'media/uploads'
DIR_OUTPUTS = Path(__file__).resolve().parent / 'media/outputs'

def open_image(filename):
    return Image.open(DIR_UPLOADS / filename)

def save_image(image, type):
    date = datetime.now().strftime('%Y%m%d%H%M%S')
    extension = "gif" if type == "gif" else "png"
    filename = f"output_{type}_{date}.{extension}"

    if type != "gif":
        image.save(DIR_OUTPUTS / filename)

    return filename

def path_output_image(filename):
    return '/media/outputs/' + filename

def grayscale(image):
    return image.convert('L')

def fusion(image1, image2, ratio, x, y):
    size = (max(image1.size[0], image2.size[0] + x), max(image1.size[1], image2.size[1] + y))
    
    new_image1 = Image.new('RGBA', size, (0, 0, 0, 0))  # Création d'une image vide
    new_image1.paste(image1.convert('RGBA'), (0, 0))  # On colle l'image1 dans l'image vide (en haut à gauche)

    new_image2 = Image.new('RGBA', size, (0, 0, 0, 0))  # Création d'une image vide
    new_image2.paste(image2.convert('RGBA'), (x, y))  # On colle l'image2 dans l'image vide (en bas à droite)

    # On fusionne les deux images
    fusion_images = ratio*np.array(new_image1) + (1-ratio)*np.array(new_image2)
    fusion_images = fusion_images.astype(np.uint8)

    return Image.fromarray(fusion_images)

def resize(image, size):
    return image.resize(size)

def black_and_white(image):
    image = np.array(image.convert('L'))
    threshold = 128
    image = ((image > threshold) * 255).astype(np.uint8)

    return Image.fromarray(image)

def alignment(images, horizontal=True):
    images = [image.convert('RGB') for image in images ] # On convertit les images en RGB pour éviter les problèmes de compatibilité
    size = images[0].size
    images = [image.resize(size) for image in images ] # On redimensionne les images pour qu'elles aient toutes la même taille

    size_new_image = (len(images)*size[0], size[1]) if horizontal else (size[0], len(images)*size[1])
    new_image = Image.new('RGB', size_new_image, (250, 250, 250))
    for i in range(len(images)):
        co = (size[0]*i, 0) if horizontal else (0, size[1]*i)
        new_image.paste(images[i], co)

    return new_image

def animation(images, duration):
    # images = [image.convert('RGBA') for image in images ] # Garde transparence mais résultat pas top
    images = [image.convert('RGB') for image in images ] # On convertit les images en RGB pour éviter les problèmes de compatibilité
    size = images[0].size
    images = [image.resize(size) for image in images ] # On redimensionne les images pour qu'elles aient toutes la même taille

    filename = save_image(images, "gif")
    images[0].save(DIR_OUTPUTS / filename, save_all=True, append_images=images[1:], duration=duration, loop=0)

    return filename