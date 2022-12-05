from __init__ import *

def catch_last_index():
    global alligment_list
    last_index = alligment_list[-1]
    return last_index

def calculate_allignment_value():
    global major_index_counter, minor_index_counter
    return major_index_counter * 5 + minor_index_counter + 1

def print_allignment(major, minor):
    global major_index_counter, minor_index_counter
    print(f'{calculate_allignment_value()} | {major} | {minor}')
    return calculate_allignment_value()

def print_color_map():
    global major_index_counter, minor_index_counter, alligment_list
    for major in major_colors:
        for minor in minor_colors:
            major_index_counter, minor_index_counter = major_colors.index(major), minor_colors.index(minor)
            alligment_list.append(print_allignment(major, minor))
    return len(major_colors) * len(minor_colors), catch_last_index()

result, last_index_mul = print_color_map()
assert(result == last_index_mul)
print("All is well (maybe!)\n")
