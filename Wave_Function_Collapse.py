import Image_Parser
import os

def main():
    current_directory = os.getcwd()
    output_path = current_directory + "/Assets/Bitmaps/";
    bitmaps = Image_Parser.get_bitmaps(output_path);
    print(bitmaps)

if __name__ == "__main__":
    main()