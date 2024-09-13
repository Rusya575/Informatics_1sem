f, m, n, f = open('input.txt'), [], [], []

for i in f:
    m = m.split()
    break
for i in f:
    f.append(i)
f = f[-1:]
for i in range(len(m)):
    m[i] = int(m[i], int(f))
for i in f:
    n.append(i)
n = n[-2:]

if n == '+':
    print(sum(m))
elif n == '-':
    s = 0
    for i in m[1]:
        s -= i
    print(s + m[i])
else:
    s = 1
    for i in m:
        s *= i
    print(s)
f = open('output.txt', 'w')
f.write(str(s))
