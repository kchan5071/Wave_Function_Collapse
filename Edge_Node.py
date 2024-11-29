class Edge_Node:
    def __init__(self, edges, tile):
        self.NORTH = edges[0]
        self.EAST = edges[1]
        self.SOUTH = edges[2]
        self.WEST = edges[3]
        self.edges = edges
        self.tile = tile

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
        return self.tile
