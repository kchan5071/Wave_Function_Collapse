from PIL import Image

def parse_image(image_path):
    image = Image.open(image_path)
    return image

def convert_image_to_bitmap(image, file_name):
    image.save(file_name + ".bmp")


