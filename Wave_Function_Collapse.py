from Map import Map
from MapNode import MapNode

class Model:
    def __init__(self, width, height, pattern_size, map_node,split_images):
        self.map = Map(width, height, pattern_size, map_node, split_images)
    
    def run(self):
        #print entropy map
        self.map.print_entropy()
        #find the lowest entropy
        lowest_entropy = self.map.find_lowest_entropy()
        print("Lowest Entropy: ", lowest_entropy)
        print("done")
