def initialize_hex_values(pattern_size):
    hex_values = []
    for i in range(0, 4):
        hex_values.append([])
    return hex_values

def rgb_to_hex(rgb):
    return '#{:02x}{:02x}{:02x}'.format(rgb[0], rgb[1], rgb[2])

def encode_bitmap_edges(bitmap, pattern_size):
    #bitmap is a 2d array of rgb values
    hex_values = initialize_hex_values(pattern_size)
    #do three sample points on each edge
    for i in range(0, 4):
        hex_values[i].append(rgb_to_hex(bitmap[0][i]))
        hex_values[i].append(rgb_to_hex(bitmap[pattern_size // 2][i]))
        hex_values[i].append(rgb_to_hex(bitmap[pattern_size - 1][i]))



    return hex_values

def convert_image_to_bitmap(image):
    bitmap = []
    for i in range(0, image.width):
        bitmap.append([])
        for j in range(0, image.height):
            bitmap[i].append(image.getpixel((i, j)))
    return bitmap

