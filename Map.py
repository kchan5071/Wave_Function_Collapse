import Bitmap_Edge_Encoder
from MapNode import MapNode

class Map: 
    def __init__(self, width, height, pattern_size, tiles, edge_image_dictionary):
        self.width = width
        self.height = height
        self.pattern_size = pattern_size
        self.tile_images = tiles
        self.edges = []
        self.tiles = []
        self.edge_image_dictionary = edge_image_dictionary

        self.initialize_empty_map()

    def get_node(self, x, y):
        if self.is_out_of_bounds(x, y):
            return None
        return self.tiles[x][y]
    
    def is_out_of_bounds(self, x, y):
        if x < 0 or x >= self.width:
            return True
        if y < 0 or y >= self.height:
            return True
        return False

    def get_initial_size(self):
        return self.width, self.height
    
    def initialize_empty_map(self):
        self.tiles = []
        for i in range(0, self.width):
            self.tiles.append([])
            for j in range(0, self.height):
                self.tiles[i].append(MapNode(self.edge_image_dictionary))

    def find_lowest_entropy(self):
        lowest_entropy = self.tiles[0][0].get_entropy()
        for i in range(0, self.width):
            for j in range(0, self.height):
                if self.tiles[i][j].get_entropy() < lowest_entropy:
                    lowest_entropy = self.tiles[i][j].get_entropy()
        return lowest_entropy
    
    def print_entropy(self):
        for i in range(0, self.width):
            print_string = ""
            for j in range(0, self.height):
                print_string += str(self.tiles[i][j].get_entropy()) + " "
            print(print_string)

    def print_all_edges(self):
        for i in range(0, self.width):
            print_string = ""
            for j in range(0, self.height):
                print_string += str(self.tiles[i][j].get_edges()) + " "
            print(print_string)

    


    
    
    


