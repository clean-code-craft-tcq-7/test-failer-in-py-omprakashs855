
def size(cms):
    if cms < 38:
        return 'S'
    elif cms > 38 and cms < 42:
        return 'M'
    else:
        return 'L'


assert(size(37) == 'S')
assert(size(40) == 'M')
assert(size(43) == 'L')
# 38 cms size is left unchecked
assert(size(38) == 'S' or size(38) == 'M')
print("All is well (maybe!)\n")
