import numpy as np

import copy

def propagate(row, col, wave, patterns, selected_pattern):
    # Update allowed patterns for tiles to the right and below
    right_edge = selected_pattern.get_east()
    bottom_edge = selected_pattern.get_south()
    num_patterns = len(patterns)

    # Check every pattern on the tile below this one
    # If the top edge of the pattern does not match the bottom edge of the pattern
    # chosen for the current tile, then that pattern cannot be used
    if row != len(wave) - 1:
        bottom_tile_patterns = wave[row + 1, col]
        for bottom_pattern_index in range(num_patterns - 1):
            pattern_to_check = patterns[bottom_pattern_index]
            if pattern_to_check.get_north() != bottom_edge:
                bottom_tile_patterns[bottom_pattern_index] = False

    if col != len(wave[0]) - 1:
        right_tile_patterns = wave[row, col + 1]
        for right_pattern_index in range(num_patterns - 1):
            pattern_to_check = patterns[right_pattern_index]
            if pattern_to_check.get_west() != right_edge:
                right_tile_patterns[right_pattern_index] = False

# patterns is an array of MapNode containing every possible pattern
# This function should recursively call itself to fill in the next tile based on temp_wave
# Fill in output from left to right, top to bottom
# If it becomes impossible to continue, backtrack until we reach a point where a different pattern can be tried
def find_pattern_for_square(height, width, row, col, wave, patterns, patterns_chosen):
    # len(patterns) = len(allowed_patterns)
    num_patterns = len(patterns)
    allowed_patterns = wave[row, col]
    temp_wave = copy.deepcopy(wave)

    # TODO: introduce randomness in pattern selection to make more interesting outputs
    for pattern_index in range(num_patterns - 1):
        if allowed_patterns[pattern_index]:
            # This pattern is allowed, try using it
            new_allowed_patterns = [False for _ in range(num_patterns)]
            new_allowed_patterns[pattern_index] = True
            temp_wave[row, col] = new_allowed_patterns
            patterns_chosen[row][col] = pattern_index

            propagate(row, col, temp_wave, patterns, patterns[pattern_index])

            next_col = col + 1
            next_row = row
            if next_col == width:
                next_row += 1
                next_col = 0
                if next_row == height:
                    # This square is the last square in the output
                    return patterns_chosen

            next_result = find_pattern_for_square(height, width, next_row, next_col, temp_wave, patterns, patterns_chosen)

            if len(next_result) != 0:
                return next_result
    # If the function reaches this point then no solution is possible
    return []

def run(height, width, patterns):
    wave = np.ones((height, width, len(patterns)), dtype=bool)
    patterns_chosen = [[-1 for _ in range(width)] for _ in range(height)]
    return find_pattern_for_square(height, width, 0, 0, wave, patterns, patterns_chosen)