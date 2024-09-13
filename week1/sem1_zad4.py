f, m, n = open('input.txt'), [], ''

for i in f:
    m = list(map(int, i.split()))
    break
for i in f:
    n += i
n = n[-1]
f.close()

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
f.close()
