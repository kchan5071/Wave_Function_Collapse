import random

class MapNode:
    def __init__(self, edge_image_dictionary):
        # Initialize the node with edges and valid tiles
        self.NORTH = None
        self.EAST = None
        self.SOUTH = None
        self.WEST = None
        self.valid_tiles = edge_image_dictionary.copy()  # Copy of possible tiles
        self.edge_dictionary = edge_image_dictionary  # Reference to all edges
        self.collapsed = False  # Tracks if the node is collapsed
        self.tile_image = None  # Image for the selected tile

    # Getters for edges and tiles
    def get_north(self):
        return self.NORTH

    def get_east(self):
        return self.EAST

    def get_south(self):
        return self.SOUTH

    def get_west(self):
        return self.WEST

    def get_edges(self):
        # Return all edges as a tuple
        return self.NORTH, self.EAST, self.SOUTH, self.WEST

    def get_tile(self):
        # Return the image of the tile
        return self.tile_image

    # Setters for edges
    def set_north(self, edge):
        self.NORTH = edge

    def set_east(self, edge):
        self.EAST = edge

    def set_south(self, edge):
        self.SOUTH = edge

    def set_west(self, edge):
        self.WEST = edge

    def collapse(self):
        # Randomly select a valid tile to collapse this node
        random_tile = random.choice(self.valid_tiles)
        random_tile_edges = random_tile.get_edges()

        # Set the edges and image to match the selected tile
        self.NORTH = random_tile_edges[0]
        self.EAST = random_tile_edges[1]
        self.SOUTH = random_tile_edges[2]
        self.WEST = random_tile_edges[3]
        self.tile_image = random_tile.get_image()

        # Mark the node as collapsed and restrict valid tiles
        self.collapsed = True
        self.valid_tiles = [random_tile]

    def remove_invalid_states(self):
        # Remove tiles that do not match the current edge constraints
        if self.collapsed:  # Skip if already collapsed
            return
        tiles_to_remove = []
        for tile in self.valid_tiles:
            tile_edges = tile.get_edges()
            # Check each edge and mark tiles for removal if invalid
            if self.NORTH is not None and self.NORTH != tile_edges[0]:
                tiles_to_remove.append(tile)
                continue
            if self.EAST is not None and self.EAST != tile_edges[1]:
                tiles_to_remove.append(tile)
                continue
            if self.SOUTH is not None and self.SOUTH != tile_edges[2]:
                tiles_to_remove.append(tile)
                continue
            if self.WEST is not None and self.WEST != tile_edges[3]:
                tiles_to_remove.append(tile)

        for tile in tiles_to_remove:  # Remove invalid tiles
            self.valid_tiles.remove(tile)

        if len(self.valid_tiles) == 0:  # Handle contradictions
            print("CONTRADICTION")
            print("NORTH: " + str(self.NORTH))
            print("EAST: " + str(self.EAST))
            print("SOUTH: " + str(self.SOUTH))
            print("WEST: " + str(self.WEST))

    def get_entropy(self):
        # Return the number of valid tiles as entropy
        return len(self.valid_tiles)

    def get_image(self):
        # Return the image associated with the node
        return self.tile_image
