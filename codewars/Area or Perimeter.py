def area_or_perimeter(l , w):
    if(l == w):
        print(l**2)
        return l**2
    else:
        print(2 * l + 2 * w)
        return 2 * l + 2 * w


area_or_perimeter(4, 4)# 16
area_or_perimeter(6, 10)# 32