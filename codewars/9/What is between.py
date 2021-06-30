def between(a,b):
    arr = []
    for i in range(a, b+1, 1):
        arr.append(i)
    return arr

between(1, 4)   # [1, 2, 3, 4]
between(-2, 2)  # [-2, -1, 0, 1, 2]