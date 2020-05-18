a = int(input())

print('0 1 1 ', end="")

p = [1, 1]

for i in range(3, a):
    n = int(p[0]) + int(p[1])
    if (i != a-1):
        print('%d ' %n, end="")
        p[0] = int(p[1])
        p[1] = n
    else:
        print('%d' %n)