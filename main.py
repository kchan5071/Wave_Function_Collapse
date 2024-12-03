import argparse
import os
import cv2
import numpy as np
import hashlib
from PIL import Image

import Image_Parser
import Bitmap_Edge_Encoder
from Edge_Image_Pair import Edge_Image_Pair
from Wave_Function_Collapse import Model

def get_args():
    default_output_path = os.getcwd()
    default_input_path = os.getcwd() + "/Assets/"
    default_pattern_size = 16
    default_size = 5
    parser = argparse.ArgumentParser(description='Wave Function Collapse')
    parser.add_argument('-n', type=int, default=default_pattern_size, help='Pattern size')
    parser.add_argument('-o', type=str, default=default_output_path, help='Output path')
    parser.add_argument('-i', type=str, default=default_input_path, help='Input path')
    parser.add_argument('-s', type=int, default=default_size, help='Size of the output image')
    parser.add_argument('-v', type=bool, default=False, help='View the output image')
    parser.add_argument('-p', type=bool, default=False, help='Print debug info')
    args = parser.parse_args()
    return args

def get_initial_size(bitmap):
    return bitmap.width, bitmap.height

def get_image_hash(image):
    return hashlib.md5(image.tobytes()).hexdigest()

def main():
    args = get_args()
    width = args.s
    height = args.s
    current_directory = args.i
    output_path = args.o
    pattern_size = args.n
    print ("Pattern Size: ", pattern_size)
    print ("Output Path: ", output_path)
    print ("Input Path: ", current_directory)
    print ("Size of the output image: ", width, height)

    # parse the image
    image = Image_Parser.get_image(current_directory)
    split_images = Image_Parser.split_image(image, pattern_size)
        
    # #remove duplicate images
    unique_images = []
    unique_hashes = []
    for i in range(0, len(split_images)):
        image_hash = get_image_hash(split_images[i])
        if image_hash not in unique_hashes:
            unique_images.append(split_images[i])
            unique_hashes.append(image_hash)

    split_images = unique_images
    print("Number of Tiles in set: ", len(split_images))

    #initialize edges
    edges = []
    for i in range(0, len(split_images)):
        bitmap = Bitmap_Edge_Encoder.convert_image_to_bitmap(split_images[i])
        edge = Bitmap_Edge_Encoder.encode_bitmap_edges(bitmap, pattern_size)
        edges.append(edge)

    print("Number of Edges: ", len(edges))

    #initialize edge image pairs
    image_edge_dictionary = []
    index = 0
    for i in range(0, len(split_images)):
        image_edge_dictionary.append(Edge_Image_Pair(edges[index], split_images[i]))
        index += 1

    if width > 10 or height > 10:
        print("large image, may take a while to process")

    #initialize map
    saved_bitmap = None
    while saved_bitmap is None:
        model = Model(width, height, pattern_size, split_images, image_edge_dictionary, args.p)
        saved_bitmap = model.run()

    #enlarge the image
    scale_percent = 200
    width = int(saved_bitmap.width * scale_percent / 100)
    height = int(saved_bitmap.height * scale_percent / 100)
    dim = (width, height)
    saved_image = None
    saved_image = saved_bitmap.resize(dim, cv2.INTER_AREA)

    #show the final image
    if args.v:
        #convert to bgr
        saved_image = cv2.cvtColor(np.array(saved_image), cv2.COLOR_RGB2BGR)

        cv2.imshow("Image", saved_image)
        cv2.waitKey(0)

    #save the final image
    cv2.imwrite(output_path + "/output.png", np.array(saved_image))
    #save bitmap to output path
    saved_bitmap.save(output_path + "/output.bmp")
    Image
    print("Image saved to: ", output_path + "/output.png")

if __name__ == "__main__":
    main()