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


def get_args():
    default_output_path = os.getcwd()
    default_pattern_size = 32
    parser = argparse.ArgumentParser(description='Wave Function Collapse')
    parser.add_argument('-n', type=int, default=default_pattern_size, help='Pattern size')
    parser.add_argument('-o', type=str, default=default_output_path, help='Output path')
    args = parser.parse_args()
    return args


def get_initial_size(bitmap):
    return bitmap.width, bitmap.height


def main():
    args = get_args()
    width = 10  # Width of the output map
    height = 10  # Height of the output map
    current_directory = os.getcwd()
    output_path = args.o
    pattern_size = args.n  # Size of individual pattern tiles
    print("Pattern Size: ", pattern_size)

    # Load images from the Assets folder
    images = Image_Parser.get_images(current_directory + "/Assets/")
    if not images:
        print("No images found in the 'Assets/' folder. Please add valid .png files.")
        return

    split_images = Image_Parser.split_image(images[0], pattern_size)
    print("Split Images: ", len(split_images))

    # Encode edges of each split image for pattern matching
    edges = []
    for split_image in split_images:
        bitmap = Bitmap_Edge_Encoder.convert_image_to_bitmap(split_image)
        edge = Bitmap_Edge_Encoder.encode_bitmap_edges(bitmap, pattern_size)
        edges.append(edge)

    print("Edges encoded for patterns: ", len(edges))

    # Initialize edge-image pairs for the Wave Function Collapse algorithm
    image_edge_dictionary = []
    for i, split_image in enumerate(split_images):
        image_edge_dictionary.append(Edge_Image_Pair(edges[i], split_image))

    # Initialize the Wave Function Collapse model
    model = Model(width, height, pattern_size, split_images, image_edge_dictionary)
    save_bitmap = model.run()  # Run the WFC algorithm

    # Check if the WFC algorithm failed
    if save_bitmap is None:
        print("Wave Function Collapse failed to generate a valid output. Please check the input data.")
        return

    # Enlarge the generated output image for better visualization
    scale_percent = 200  # Scale factor for resizing
    output_width = int(save_bitmap.width * scale_percent / 100)
    output_height = int(save_bitmap.height * scale_percent / 100)
    dim = (output_width, output_height)
    save_bitmap = save_bitmap.resize(dim, cv2.INTER_AREA)

    # Save and display the final generated image
    output_file_path = os.path.join(output_path, "output.png")
    save_bitmap.save(output_file_path)
    print(f"Output saved to: {output_file_path}")

    # Show the final generated image
    cv2.imshow("Generated Image", np.array(save_bitmap))
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
