def size(cms):
    if isinstance(cms, int) or isinstance(cms, float):
        if cms > 0 and cms < 38:
            return 'S'
        elif cms >= 38 and cms < 42:
            return 'M'
        elif cms >= 42:
            return 'L'
        elif cms <= 0:
            print("[warning] {} not possible !!!".format(cms))
            return 'NA'
    else:
        print("[warning] {} is not a measured size".format(cms))
        return 'NA'

def tshirt_size_check():
    assert(size(37.5) == 'S')
    assert(size(40) == 'M')
    assert(size(43) == 'L')
    # Lets assume 38 cms to be Medium, 42 cms to be Large
    assert(size(38) == 'M')
    assert(size(38.5) == 'M')
    # Checking all boundary values
    assert(size(42) == 'L')
    assert(size(42.5) == 'L')
    # Checking not possible sizes
    assert(size(0) == 'NA')
    assert(size(-3) == 'NA')
    assert(size("ABC") == 'NA')
    # Returning True as no assert error until end
    return True

if tshirt_size_check():
    print("All is well\n")