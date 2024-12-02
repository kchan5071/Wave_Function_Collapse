from PIL import Image
import os
import numpy as np

def get_images(file_path):
    # Load all PNG images from the specified directory
    images = []
    for file in os.listdir(file_path):
        if file.endswith(".png"):  # Check for PNG files
            images.append(Image.open(file_path + file))  # Open and append to list
    return images

def split_image(image, pattern_size):
    # Split the image into smaller tiles of the given pattern size
    images = []
    print("Image Size: ", image.width, image.height)
    if image.width == pattern_size and image.height == pattern_size:
        # If the image matches the pattern size, add original and rotated versions
        images.append(image)
        images.append(image.rotate(90))  # Rotate 90 degrees
        images.append(image.rotate(180))  # Rotate 180 degrees
        images.append(image.rotate(270))  # Rotate 270 degrees
        return images
    
    # Split the image into pattern_size x pattern_size tiles
    for i in range(0, image.width // pattern_size):  # Iterate over rows
        for j in range(0, image.height // pattern_size):  # Iterate over columns
            images.append(
                image.crop((i * pattern_size, j * pattern_size, (i + 1) * pattern_size, (j + 1) * pattern_size))
            )

    # Add rotated versions of each tile
    for i in range(0, len(images)):
        images.append(images[i].rotate(90))
        images.append(images[i].rotate(180))
        images.append(images[i].rotate(270))
    return images
