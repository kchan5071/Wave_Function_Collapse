from PIL import Image
import os
import numpy as np


def get_images(file_path):
    images = []
    for file in os.listdir(file_path):
        if file.endswith(".png"):
            images.append(Image.open(file_path + file))
    return images

def get_image(file_path):
    if file_path.endswith(".png"):
        return Image.open(file_path)
    if os.path.isdir(file_path):
        if len(get_images(file_path)) == 0:
            print("No images found in directory")
            exit()
        return get_images(file_path)[0]
    return Image.open(file_path)

def split_image(image, pattern_size):
    images = []
    print("Image Size: ", image.width, image.height)
    if image.width == pattern_size and image.height == pattern_size:
        images.append(image)
        #add rotation of images
        images.append(image.rotate(90, expand=True))
        images.append(image.rotate(180, expand=True))
        images.append(image.rotate(270, expand=True))
        return images
    
    #split image into pattern_size x pattern_size images
    for i in range(0, image.width // pattern_size):
        for j in range(0, image.height // pattern_size):
            box = (i * pattern_size, j * pattern_size, (i + 1) * pattern_size, (j + 1) * pattern_size)
            images.append(image.crop(box))

    #add rotation of images
    for i in range(0, len(images)):
            images.append(images[i].rotate(90, expand=True))
            images.append(images[i].rotate(180, expand=True))
            images.append(images[i].rotate(270, expand=True))
    return images

