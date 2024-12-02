class Edge_Image_Pair:
    def __init__(self, edges, image):
        # Initialize the edges and the image associated with this pair
        self.NORTH = edges[0]
        self.EAST = edges[1]
        self.SOUTH = edges[2]
        self.WEST = edges[3]
        self.image = image

    def get_edges(self):
        # Return all edges as a tuple (NORTH, EAST, SOUTH, WEST)
        return self.NORTH, self.EAST, self.SOUTH, self.WEST

    def get_image(self):
        # Return the image associated with this pair
        return self.image
