import random

class MapNode:
    def __init__(self, edge_image_dictionary):
        self.NORTH = None
        self.EAST = None
        self.SOUTH = None
        self.WEST = None
        self.valid_tiles = edge_image_dictionary.copy()
        self.edge_dictionary = edge_image_dictionary
        self.collapsed = False
        self.tile_image = None

    #getters
    def get_north(self):
        return self.NORTH
    
    def get_east(self):
        return self.EAST
    
    def get_south(self):
        return self.SOUTH
    
    def get_west(self):
        return self.WEST
    


    def get_edges(self):
        return self.NORTH, self.EAST, self.SOUTH, self.WEST
    
    def get_tile(self):
        return self.tile_image
    
    
    #setters
    def set_north(self, edge):
        self.NORTH = edge

    def set_east(self, edge):
        self.EAST = edge

    def set_south(self, edge):
        self.SOUTH = edge

    def set_west(self, edge):
        self.WEST = edge

    def collapse(self):
        # Randomly choose a tile from the valid tiles
        # also works with one tile
        random_tile = random.choice(self.valid_tiles)
        random_tile_edges = random_tile.get_edges()
        # Set the edges of the node to the edges of the random tile
        self.NORTH = random_tile_edges[0]
        self.EAST = random_tile_edges[1]
        self.SOUTH = random_tile_edges[2]
        self.WEST = random_tile_edges[3]

        # Set the tile image to the image of the random tile
        self.tile_image = random_tile.get_image()

        # Set the node to collapsed
        self.collapsed = True

        #set the valid tiles to the random tile
        self.valid_tiles = [random_tile]
    
    def remove_invalid_states(self):
        # If already collapsed, no need to process
        if self.collapsed:
            return

        # Iterate through valid tiles and remove invalid ones
        self.valid_tiles = [
            tile for tile in self.valid_tiles
            if (self.NORTH is None or self.NORTH == tile.get_edges()[0]) and
            (self.EAST is None or self.EAST == tile.get_edges()[1]) and
            (self.SOUTH is None or self.SOUTH == tile.get_edges()[2]) and
            (self.WEST is None or self.WEST == tile.get_edges()[3])
        ]

    def get_entropy(self):
        return len(self.valid_tiles)
    
    def get_image(self):
        return self.tile_image
    
    def is_collapsed(self):
        return self.collapsed
    
    def print_edges(self):
        print("NORTH: ", self.NORTH)
        print("EAST: ", self.EAST)
        print("SOUTH: ", self.SOUTH)
        print("WEST: ", self.WEST)