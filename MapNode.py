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
        # Remove tiles that do not have the correct edge, part of the propagation process
        # to make it easier
        # North(0), East(1), South(2), West(3)
        if self.collapsed:
            return
        tiles_to_remove = []
        for tile in self.valid_tiles:
            tile_edges = tile.get_edges()
            if self.NORTH is not None and self.NORTH != tile_edges[0] and tile in self.valid_tiles:
                tiles_to_remove.append(tile)
                continue
            if self.EAST is not None and self.EAST != tile_edges[1] and tile in self.valid_tiles:
                tiles_to_remove.append(tile)
                continue
            if self.SOUTH is not None and self.SOUTH != tile_edges[2] and tile in self.valid_tiles:
                tiles_to_remove.append(tile)
                continue
            if self.WEST is not None and self.WEST != tile_edges[3]and tile in self.valid_tiles:
                tiles_to_remove.append(tile)
                continue

        for tile in tiles_to_remove:
            self.valid_tiles.remove(tile)

        # If there are no valid tiles, there is a contradiction
        # print the edges of the node that caused the contradiction
        if len(self.valid_tiles) is 0:
            print("CONTRADICTION")
            print("NORTH: " + str(self.NORTH))
            print("EAST: " + str(self.EAST))
            print("SOUTH: " + str(self.SOUTH))
            print("WEST: " + str(self.WEST))

    def get_entropy(self):
        return len(self.valid_tiles)
    
    def get_image(self):
        return self.tile_image