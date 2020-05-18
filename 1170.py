n = int(input())
c = 0

while c<n:
    d = 0

    a = float(input())

    while a>1:
        a /= 2
        d += 1

    print("%d dias" %d)

    c += 1