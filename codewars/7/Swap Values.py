def swap_values(args): 
    # tmp = args[0]
    # args[0] = args[1]
    # args[1] = tmp
    args[0], args[1] = args[1], args[0]
    return args

arr = [1, 2]
swap_values(arr)    # [2, 1]