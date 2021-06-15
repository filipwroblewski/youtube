def make_negative( number ):
    if number <= 0:
        return number
    else:
        return (-1)*number

make_negative(42)   # -42
make_negative(-9)   # -9
make_negative(0)    # 0