from PIL import Image
import numpy as np
from pathlib import Path
import matplotlib.pyplot as plt
import os

DIR_UPLOADS = Path(__file__).resolve().parent / 'media/uploads'
DIR_OUTPUTS = Path(__file__).resolve().parent / 'media/outputs'
COLORS = {
    'black': (0,0,0),
    'white': (255,255,255),
}

def open_image(filename):
    return Image.open(DIR_UPLOADS / filename)

def save_image(image):
    image.save(DIR_OUTPUTS / 'output.png')

def path_output_image(filename):
    return '/media/outputs/' + filename

def grayscale(image):
    return image.convert('L')

def fusion(image1, image2, ratio):
    image1 = np.array(open_image('image1.jpg')) # A supprimer
    image2 = np.array(open_image('image2.jpg')) # A supprimer

    fusionImage = ratio*image1 + (1-ratio)*image2

    fusionImage = fusionImage.astype(np.uint8)

    return Image.fromarray(fusionImage)

def resize(image, size):
    return image.resize(size)

def black_and_white(image): 
    image = open_image('image1.jpg') # A supprimer

    image = np.array(image.convert('L'))
    threshold = 128
    image = ((image > threshold) * 255).astype(np.uint8)

    return Image.fromarray(image)

def animation(image, images, duration):
    images = [open_image('image1.jpg'), open_image('image2.jpg')] # A supprimer
    images = [np.array(image) for image in images]
    images = [Image.fromarray(image) for image in images]

    images[0].save(DIR_OUTPUTS / 'output.gif', save_all=True, append_images=images[1:], duration=duration, loop=0)

    return images[0]