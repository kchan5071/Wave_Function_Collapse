import numpy as np
import copy
import MapNode

class Model:
    def __init__(self, width, height, num_patterns):
        """
        Initialize the model with grid dimensions and number of patterns.
        """
        self.width = width
        self.height = height
        self.num_patterns = num_patterns
        self.wave = np.ones((height, width, num_patterns), dtype=bool)  # Tracks allowed patterns per tile

    def update_allowed_patterns(self, temp_wave, row, col, patterns, pattern_index):
        """
        Update neighboring tiles' allowed patterns based on edge matching.
        """
        pattern = patterns[pattern_index]
        right_edge, bottom_edge = pattern.get_east(), pattern.get_south()

        # Update the tile below
        if row + 1 < self.height:
            for idx, neighbor_pattern in enumerate(patterns):
                if neighbor_pattern.get_north() != bottom_edge:
                    temp_wave[row + 1, col, idx] = False

        # Update the tile to the right
        if col + 1 < self.width:
            for idx, neighbor_pattern in enumerate(patterns):
                if neighbor_pattern.get_west() != right_edge:
                    temp_wave[row, col + 1, idx] = False

    def find_pattern_for_square(self, row, col, wave, patterns):
        """
        Recursively assign valid patterns to each tile, backtracking if needed.
        """
        allowed_patterns = wave[row, col]
        if not np.any(allowed_patterns):  # No valid patterns
            return []

        temp_wave = copy.deepcopy(wave)  # Preserve current state for backtracking

        for pattern_index in range(self.num_patterns):
            if allowed_patterns[pattern_index]:
                # Choose this pattern and update the wave
                temp_wave[row, col] = np.zeros(self.num_patterns, dtype=bool)
                temp_wave[row, col, pattern_index] = True
                self.update_allowed_patterns(temp_wave, row, col, patterns, pattern_index)

                # Move to the next tile
                next_col = (col + 1) % self.width
                next_row = row + (col + 1) // self.width
                if next_row == self.height:  # Grid filled
                    return temp_wave

                # Recurse to the next tile
                result = self.find_pattern_for_square(next_row, next_col, temp_wave, patterns)
                if result:
                    return result  # Solution found

        return []  # Backtrack if no valid configuration is possible

    def run(self, patterns):
        """
        Start the Wave Function Collapse process and return the final wave.
        """
        result = self.find_pattern_for_square(0, 0, self.wave, patterns)
        if not result:
            print("Wave Function Collapse failed: no valid solution found.")
            return None
        return result