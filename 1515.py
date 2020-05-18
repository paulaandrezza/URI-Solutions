while True:

    n = int(input())

    if n == 0: break

    c = 0
    y = 2115

    while c < n:
        a = input().split()

        b = int(a[1]) - int(a[2])

        if b < y:
            y = b
            p = a[0]

        c += 1
    print(p)
