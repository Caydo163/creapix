from PIL import Image
import numpy as np
from pathlib import Path
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
