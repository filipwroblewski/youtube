def check(seq, elem):
    if elem in seq:
        return True
    else:
        return False



check([66, 101], 66)    # True
check([66, 101], 1)    # False
check(["anyone", "want", "to", "hire", "me?"], "me?")   # True