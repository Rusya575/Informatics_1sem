a, k = list(map(int, input().split())), 1
for i in a:
    k *= i
print(k**(1/len(a)))
