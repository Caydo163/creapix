from PIL import Image
import numpy as np
from pathlib import Path
import os

DIR = Path(__file__).resolve().parent / 'media/uploads'
COLORS = {
    'black': (0,0,0),
    'white': (255,255,255),
}

def open_image(filename):
    return Image.open(DIR / filename)

def save_image(image):
    image.save(DIR / 'output.png')

def path_image(filename):
    return '/media/uploads/' + filename

def grayscale(image):
    return image.convert('L')
