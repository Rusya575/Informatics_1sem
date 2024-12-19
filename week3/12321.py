def tri(size, symb, cur = 1):
    if size == 0:
        return
    print(min(cur, size)*symb)
    return tri(size-1, symb, cur+1)
tri(int(input()), input(), 1)
