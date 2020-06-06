def maior(l):
    m = len(l[0])

    for i in range(1, len(l)):
        if len(l[i]) > m:
            m = len(l[i])

    return m

n = int(input())

for e in range(n):
    i = input().split()
    s = []
    n = maior(i)

    for f in range(n, 0, -1):
        for g in i:
            if len(g) == f:
                s.append(g)

    print(" ".join(s))