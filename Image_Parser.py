from PIL import Image
import os

def convert_image_to_bitmap(image, base_name, file_path, output_path):
    index = 0
    for file in os.listdir(file_path):
        if file.endswith(".png"):
            image = Image.open(file_path + file)
            image.save(output_path + base_name + "_" + str(index) + ".bmp")
            index += 1

def get_bitmaps(image_path):
    bitmaps = []
    for file in os.listdir(image_path):
        if file.endswith(".bmp"):
            bitmaps.append(file)
    return bitmaps

def main():
    current_directory = os.getcwd()
    image_path = current_directory + "/Assets/";
    output_path = image_path + "/Bitmaps/";
    convert_image_to_bitmap(image_path, "test", image_path, output_path)

if __name__ == "__main__":
    main()

