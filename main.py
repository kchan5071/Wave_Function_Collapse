import argparse
import os
import cv2
import numpy as np

import Image_Parser
import Bitmap_Edge_Encoder

def get_args():
    default_output_path = os.getcwd();
    default_pattern_size = 16;
    parser = argparse.ArgumentParser(description='Wave Function Collapse')
    parser.add_argument('-n', type=int, default=default_pattern_size, help='Pattern size')
    parser.add_argument('-o', type=str, default=default_output_path, help='Output path')
    args = parser.parse_args()
    return args

def get_initial_size(bitmap):
    return bitmap.width, bitmap.height

def main():
    args = get_args()
    current_directory = os.getcwd()
    output_path = args.o
    pattern_size = args.n
    print ("Pattern Size: ", pattern_size)

    images = Image_Parser.get_images(current_directory + "/Assets/")
    split_images = Image_Parser.split_image(images[0], pattern_size)
    print(len(split_images), len(split_images[0]))

    #show the split images
    # for i in range(0, len(split_images)):
    #     for j in range(0, len(split_images[0])):
    #         cv2.imshow("Image", np.array(split_images[i][j]))
    #         cv2.waitKey(0)

    edges = []
    for i in range(0, len(split_images)):
        for j in range(0, len(split_images[0])):
            bitmap = Bitmap_Edge_Encoder.convert_image_to_bitmap(split_images[i][j])
            edge = Bitmap_Edge_Encoder.encode_bitmap_edges(bitmap, pattern_size)
            edges.append(edge)

    print(len(edges), len(edges[0]), len(edges[0][0]))

        
    

if __name__ == "__main__":
    main()