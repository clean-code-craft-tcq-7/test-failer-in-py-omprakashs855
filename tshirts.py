
def size(cms):
    if cms < 38:
        return 'S'
    elif cms >= 38 and cms < 42:
        return 'M'
    elif cms >= 42:
        return 'L'


assert(size(37) == 'S')
assert(size(40) == 'M')
assert(size(43) == 'L')
# 38 cms size is left unchecked
# Lets assume 38 cms to be Medium, and lets assume 42cms to be in Large
assert(size(38) == 'M')
# Checking all boundary values
assert(size(42) == 'L')
print("All is well\n")
