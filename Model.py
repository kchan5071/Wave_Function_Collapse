import numpy as np

class Model:
    # num_patterns: number of NxN patterns obtained from the input image
    def __init__(self, width, height, num_patterns):
        self.width = width
        self.height = height
        self.num_patterns = num_patterns

        # Keeps track of which patterns are still possible for each tile in the output to have
        self.wave = np.ones((height, width, num_patterns), dtype=bool)