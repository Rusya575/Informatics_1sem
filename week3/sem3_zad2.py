def sf(n, a = []):
    for i in range(2, n):
        if n % i == 0:
            a.append(i)
            return sf(n//i, a)
    a.append(n)
    return a

print(sf(int(input())))
