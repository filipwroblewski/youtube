def enough(cap, on, wait):
    if cap - on - wait >= 0:
        return 0
    else:
        return (cap - on - wait)*(-1)


enough(10, 5, 5) # 0
enough(100, 60, 50)  # 10
enough(20, 5, 5) # 0