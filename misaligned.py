
def print_color_map():
    major_colors = ["White", "Red", "Black", "Yellow", "Violet"]
    minor_colors = ["Blue", "Orange", "Green", "Brown", "Slate"]
    for i, major in enumerate(major_colors):
        for j, minor in enumerate(minor_colors):
            print(f'{i * 5 + j} | {major} | {minor}')
    last_major_color_index, last_minor_color_index = i, j
    return len(major_colors) * len(minor_colors), last_major_color_index*last_minor_color_index


result, last_index_mul = print_color_map()
assert(result == last_index_mul)
print("All is well (maybe!)\n")
