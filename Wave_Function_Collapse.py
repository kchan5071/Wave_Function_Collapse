from Map import Map
from MapNode import MapNode
from PIL import Image
import random

class Model:
    def __init__(self, width, height, pattern_size, map_node,split_images):
        self.map = Map(width, height, pattern_size, map_node, split_images)

    def collapse_node(self, position):
        x, y = position
        self.map.tiles[x][y].collapse()

    def propagate_entropy(self, position):
        x, y = position
        # set south edge of node above to north edge of current node
        north_node = self.map.get_node(x, y - 1)
        if north_node is not None:
            north_node.set_south(self.map.tiles[x][y].get_north())
            north_node.remove_invalid_states()

        # set west edge of node to the east edge of the node to the left
        west_node = self.map.get_node(x - 1, y)
        if west_node is not None:
            west_node.set_east(self.map.tiles[x][y].get_west())
            west_node.remove_invalid_states()

        # set north edge of node below to south edge of current node
        south_node = self.map.get_node(x, y + 1)
        if south_node is not None:
            south_node.set_north(self.map.tiles[x][y].get_south())
            south_node.remove_invalid_states()

        # set east edge of node to the west edge of the node to the right
        east_node = self.map.get_node(x + 1, y)
        if east_node is not None:
            east_node.set_west(self.map.tiles[x][y].get_east())
            east_node.remove_invalid_states()

    def build_map_image(self):
        width, height = (self.map.width, self.map.height)
        image = Image.new("RGB", (width * self.map.pattern_size, height * self.map.pattern_size))
        for i in range(0, width):
            for j in range(0, height):
                tile_image = self.map.tiles[i][j].get_tile()
                for x in range(0, self.map.pattern_size):
                    for y in range(0, self.map.pattern_size):
                        image.putpixel((i * self.map.pattern_size + x, j * self.map.pattern_size + y), tile_image.getpixel((x, y)))
        return image

    
    def run(self):
        #collapse random node
        random_node = (random.randint(0, self.map.width - 1), random.randint(0, self.map.height - 1))
        self.collapse_node(random_node)

        #propagate entropy
        self.propagate_entropy(random_node)

        while self.map.find_highest_entropy() > 1 and self.map.find_lowest_entropy() != 0:
            #find node with lowest entropy
            lowest_entropy = self.map.find_next_node()
            #collapse node
            self.collapse_node(lowest_entropy)
            #propagate entropy
            self.propagate_entropy(lowest_entropy)

        if self.map.find_lowest_entropy() == 0:
            print("CONTRADICTION")
            exit(1)

        return self.build_map_image()

