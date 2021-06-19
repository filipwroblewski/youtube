def reverse_seq(n):
    arr=[]
    for i in range(n):
        arr.append(i+1)
    return arr[::-1]

reverse_seq(5)  # [5,4,3,2,1]