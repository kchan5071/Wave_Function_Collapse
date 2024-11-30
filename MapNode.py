class MapNode:
    def __init__(self, edges, tile_image):
        self.NORTH = edges[0]
        self.EAST = edges[1]
        self.SOUTH = edges[2]
        self.WEST = edges[3]
        self.valid_west = []
        self.valid_south = []
        self.valid_east = []
        self.valid_north = []
        self.edges = edges
        self.tile_image = tile_image

    def get_north(self):
        return self.NORTH
    
    def get_east(self):
        return self.EAST
    
    def get_south(self):
        return self.SOUTH
    
    def get_west(self):
        return self.WEST
    
    def get_edges(self):
        return self.edges
    
    def get_tile(self):
        return self.tile_image
    
    def check_node_for_adjacency(self, node):
        # check north
        if self.NORTH == node.get_south():
            self.valid_north.append(node)
        # check east
        if self.EAST == node.get_west():
            self.valid_east.append(node)
        # check south
        if self.SOUTH == node.get_north():
            self.valid_south.append(node)
        # check west
        if self.WEST == node.get_east():
            self.valid_west.append(node)

    def check_all_nodes_for_adjacency(self, nodes):
        for i in range(0, len(nodes)):
            for j in range(0, len(nodes[0])):
                self.check_node_for_adjacency(nodes[i][j])

    def get_valid_adjacent_tiles(self):
        return self.valid_north, self.valid_east, self.valid_south, self.valid_west