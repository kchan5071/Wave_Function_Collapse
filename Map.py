import Bitmap_Edge_Encoder
import Edge_Node

class Map: 
    def __init__(self, width, height, pattern_size, edge_nodes, tiles):
        self.width = width
        self.height = height
        self.pattern_size = pattern_size
        self.tile_images = tiles
        self.edges = []
        edge_nodes = []
        self.entropy_map = []

    def get_initial_size(self):
        return self.width, self.height
    
    def initialize_empty_map(self):
        self.tiles = []
        for i in range(0, self.width):
            self.tiles.append([])
            for j in range(0, self.height):
                self.tiles[i].append(None)

    def initialize_entropy_map(self):
        self.entropy_map = []
        for i in range(0, self.width):
            self.entropy_map.append([])
            for j in range(0, self.height):
                self.entropy_map[i].append(0)

    def find_lowest_entropy(self):
        lowest_entropy = 1000000
        lowest_entropy_index = (0, 0)
        for i in range(0, self.width):
            for j in range(0, self.height):
                if self.entropy_map[i][j] < lowest_entropy:
                    lowest_entropy = self.entropy_map[i][j]
                    lowest_entropy_index = (i, j)
        return lowest_entropy_index
    
    
    


