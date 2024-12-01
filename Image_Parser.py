from PIL import Image
import os
import numpy as np


def get_images(file_path):
    images = []
    for file in os.listdir(file_path):
        if file.endswith(".png"):
            images.append(Image.open(file_path + file))
    return images

def split_image(image, pattern_size):
    images = []
    for i in range(0, image.width // pattern_size):
        for j in range(0, image.height // pattern_size):
            images.append(image.crop((i * pattern_size, j * pattern_size, (i + 1) * pattern_size, (j + 1) * pattern_size)))

    #add rotation of images
    for i in range(0, len(images)):
            images.append(images[i].rotate(90))
            images.append(images[i].rotate(180))
            images.append(images[i].rotate(270))
    return images

