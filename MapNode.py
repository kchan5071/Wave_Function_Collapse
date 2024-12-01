import random

class MapNode:
    def __init__(self, edge_image_dictionary):
        self.NORTH = None
        self.EAST = None
        self.SOUTH = None
        self.WEST = None
        self.valid_tiles = edge_image_dictionary
        self.edge_dictionary = edge_image_dictionary
        self.collapsed = False
        self.tile_image = None

    def get_north(self):
        return self.NORTH
    
    def get_east(self):
        return self.EAST
    
    def get_south(self):
        return self.SOUTH
    
    def get_west(self):
        return self.WEST
    
    def set_north(self, edge):
        self.NORTH = edge

    def set_east(self, edge):
        self.EAST = edge

    def set_south(self, edge):
        self.SOUTH = edge

    def set_west(self, edge):
        self.WEST = edge

    def get_edges(self):
        return self.edges
    
    def get_tile(self):
        return self.tile_image
    
    def collapse(self):
        # Randomly choose a tile from the valid tiles
        # also works with one tile
        random_tile = random.choice(self.valid_tiles)
        self.NORTH = random_tile.get_north()
        self.EAST = random_tile.get_east()
        self.SOUTH = random_tile.get_south()
        self.WEST = random_tile.get_west()
        self.tile_image = random_tile.get_image()
        self.collapsed = True
    
    def remove_invalid_tiles(self):
        # Remove tiles that do not have the correct edge, part of the propagation process
        # to make it easier
        # North(0), East(1), South(2), West(3)
        for tiles in self.valid_tiles:
            tile_edges = tiles.get_edges()
            if self.NORTH is not None and self.NORTH != tile_edges[0]:
                self.valid_tiles.remove(tiles)
            if self.EAST is not None and self.EAST != tile_edges[1]:
                self.valid_tiles.remove(tiles)
            if self.SOUTH is not None and self.SOUTH != tile_edges[2]:
                self.valid_tiles.remove(tiles)
            if self.WEST is not None and self.WEST != tile_edges[3]:
                self.valid_tiles.remove(tiles)
        
        # If there is only one valid tile, node is collapsed
        if len(self.valid_tiles) is 1:
            self.collapsed = True
            self.tile_image = self.valid_tiles[0].get_image()

    def get_entropy(self):
        return len(self.valid_tiles)
    
    def get_image(self):
        return self.tile_image