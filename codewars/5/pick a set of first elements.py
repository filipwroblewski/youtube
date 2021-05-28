def first(seq, n=1): 
    if n == 0:
        return []

    new_seq = []
    for i in range(len(seq)):
        if i < n:
            new_seq.append(seq[i])
    return new_seq


seq = ['a', 'b', 'c', 'd', 'e']
first(seq)  # ['a'])
first(seq, 0)   # []);
first(seq, 1)   # ['a']);
first(seq, 2)   # ['a', 'b']);
first(seq, 10)   # ['a', 'b', 'c', 'd', 'e'])