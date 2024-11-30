from typing import List

import numpy as np

import copy

import MapNode


class Model:
    # num_patterns: number of NxN patterns obtained from the input image
    def __init__(self, width, height, num_patterns):
        self.width = width
        self.height = height
        self.num_patterns = num_patterns

        # Keeps track of which patterns are still possible for each tile in the output to have
        self.wave = np.ones((height, width, num_patterns), dtype=bool)

    # patterns is an array of MapNode containing every possible pattern
    def find_pattern_for_square(self, row, col, wave, patterns):
        # len(patterns) = len(allowed_patterns)
        num_patterns = len(patterns)
        allowed_patterns = wave[row, col]
        temp_wave = copy.deepcopy(wave)

        for pattern_index in range(num_patterns - 1):
            if allowed_patterns[pattern_index]:
                # This pattern is allowed, try using it
                new_allowed_patterns = [False for _ in range(num_patterns - 1)]
                new_allowed_patterns[pattern_index] = True

                # Update allowed patterns for tiles to the right and below
                pattern = patterns[pattern_index]
                right_edge = pattern.get_east()
                bottom_edge = pattern.get_south()

                # TODO: Move this to a function to make the code cleaner
                # Check every pattern on the tile below this one
                # If the top edge of the pattern does not match the bottom edge of the pattern
                # chosen for the current tile, then that pattern cannot be used
                if row != self.height - 1:
                    bottom_tile_patterns = temp_wave[row + 1, col]
                    for bottom_pattern_index in range(num_patterns - 1):
                        pattern_to_check = patterns[bottom_pattern_index]
                        if pattern_to_check.get_north() != bottom_edge:
                            bottom_tile_patterns[bottom_pattern_index] = False

                if col != self.width - 1:
                    right_tile_patterns = temp_wave[row, col + 1]
                    for right_pattern_index in range(num_patterns - 1):
                        pattern_to_check = patterns[right_pattern_index]
                        if pattern_to_check.get_west() != right_edge:
                            right_tile_patterns[right_pattern_index] = False
                # TODO: Finish this function
                # This function should recursively call itself to fill in the next tile based on temp_wave
                # Fill in output from left to right, top to bottom
                # If it becomes impossible to continue, backtrack until we reach a point where a different pattern can be tried
        print(temp_wave)

    def run(self, patterns):
        self.find_pattern_for_square(0, 0, self.wave, patterns)