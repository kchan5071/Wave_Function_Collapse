import argparse
import os
import cv2
import numpy as np

import Image_Parser
import Bitmap_Edge_Encoder
import MapNode
from Map import Map
from Edge_Image_Pair import Edge_Image_Pair
from Wave_Function_Collapse import Model
# from Model import Model

def get_args():
    default_output_path = os.getcwd()
    default_pattern_size = 3
    parser = argparse.ArgumentParser(description='Wave Function Collapse')
    parser.add_argument('-n', type=int, default=default_pattern_size, help='Pattern size')
    parser.add_argument('-o', type=str, default=default_output_path, help='Output path')
    args = parser.parse_args()
    return args

def get_initial_size(bitmap):
    return bitmap.width, bitmap.height

def main():
    args = get_args()
    width = 4
    height = 4
    current_directory = os.getcwd()
    output_path = args.o
    pattern_size = args.n
    print ("Pattern Size: ", pattern_size)

    images = Image_Parser.get_images(current_directory + "/Assets/")
    split_images = Image_Parser.split_image(images[0], pattern_size)
    print("Split Images: ", len(split_images))

    #save split_images in test
    # for i in range(0, len(split_images)):
    #     cv2.imwrite("test" + str(i) + ".png", np.array(split_images[i]))

    edges = []
    for i in range(0, len(split_images)):
        bitmap = Bitmap_Edge_Encoder.convert_image_to_bitmap(split_images[i])
        edge = Bitmap_Edge_Encoder.encode_bitmap_edges(bitmap, pattern_size)
        edges.append(edge)

    print("Edges: ", len(edges))

    #show the split images
    # for i in range(0, len(split_images)):
    #         print("NORTH: ", edges[i][0])
    #         print("EAST: ", edges[i][1])
    #         print("SOUTH: ", edges[i][2])
    #         print("WEST: ", edges[i][3])
    #         cv2.imshow("Image", np.array(split_images[i]))
    #         cv2.waitKey(0)


    #initialize edge image pairs
    image_edge_dictionary = []
    index = 0
    for i in range(0, len(split_images)):
        image_edge_dictionary.append(Edge_Image_Pair(edges[index], split_images[i]))
        index += 1

    #initialize map
    model = Model(width, height, pattern_size, split_images, image_edge_dictionary)
    save_bitmap = model.run()

    #enlarge the image
    scale_percent = 200
    width = int(save_bitmap.width * scale_percent / 100)
    height = int(save_bitmap.height * scale_percent / 100)
    dim = (width, height)
    save_bitmap = save_bitmap.resize(dim, cv2.INTER_AREA)

    #show the final image
    cv2.imshow("Image", np.array(save_bitmap))
    cv2.waitKey(0)
    

    # model = Model(5, 5, len(map_nodes), len(map_nodes[0]), map_nodes)
    # model.run()

if __name__ == "__main__":
    main()