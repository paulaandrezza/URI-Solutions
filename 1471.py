while True:
    try:

        n, r = [int(i) for i in input().split()]
        vr = [int(i) for i in input().split()]

        l = list(range(1, n+1))
        l2 = []

        for e in l:
            if e not in vr:
                l2.append(e)

        if len(l2) != 0:
            for e in l2:
                print("%d " %e, end="")
        else:
            print("*", end="")

        print()

    except EOFError:
        break