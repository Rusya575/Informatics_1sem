n, b, c, s = input(), int(input()), int(input()), ''
n = int(n, b)

while n > 0:
    s += str(n%c)
    n //= c
print(s[::-1])
