while True:
    try:

        n = int(input())
        l = []

        for i in range(n):
            l.append(int(input()))

        lo = sorted((l))

        for i in range(n):
            print("%04d" %lo[i])

    except EOFError:
        break