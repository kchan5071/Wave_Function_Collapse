from Map import Map
from MapNode import MapNode

class Model:
    def __init__(self, width, height, pattern_size, map_node,split_images):
        self.map = Map(width, height, pattern_size, map_node, split_images)

    def collapse_node(self, x, y):
        self.map.tiles[x][y].collapse()

    def propagate_entropy(self, x, y):
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

    
    def run(self):

        #collapse the first node
        self.collapse_node(0, 0)

        #propagate entropy
        self.propagate_entropy(0, 0)

        #print entropy map
        self.map.print_entropy()

        #print all tiles
        self.map.print_all_edges()

        #find the lowest entropy
        lowest_entropy = self.map.find_lowest_entropy()

        #collapse the node with the lowest entropy
        self.collapse_node(1, 1)

        #propagate entropy
        self.propagate_entropy(1, 1)

        #print entropy map
        self.map.print_entropy()

        #print all tiles
        self.map.print_all_edges()

        #find the lowest entropy
        lowest_entropy = self.map.find_lowest_entropy()

        print("Lowest Entropy: ", lowest_entropy)
        print("done")
