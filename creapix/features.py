from PIL import Image
import numpy as np
from pathlib import Path

DIR_UPLOADS = Path(__file__).resolve().parent / 'media/uploads'
DIR_OUTPUTS = Path(__file__).resolve().parent / 'media/outputs'

def open_image(filename):
    return Image.open(DIR_UPLOADS / filename)

def save_image(image):
    image.save(DIR_OUTPUTS / 'output.png')

def path_output_image(filename):
    return '/media/outputs/' + filename

def grayscale(image):
    return image.convert('L')

def fusion(image1, image2, ratio):
    image1 = np.array(image1)
    image2 = np.array(image2.resize(image1.shape[1::-1]))

    fusion_images = ratio*image1 + (1-ratio)*image2

    fusion_images = fusion_images.astype(np.uint8)

    return Image.fromarray(fusion_images)

def resize(image, size):
    return image.resize(size)

def black_and_white(image):
    image = np.array(image.convert('L'))
    threshold = 128
    image = ((image > threshold) * 255).astype(np.uint8)

    return Image.fromarray(image)

def animation(images, duration):
    images = [open_image('image1.jpg'), open_image('image2.jpg')] # A supprimer
    images = [np.array(image) for image in images]
    images = [Image.fromarray(image) for image in images]

    images[0].save(DIR_OUTPUTS / 'output.gif', save_all=True, append_images=images[1:], duration=duration, loop=0)

    return images[0]