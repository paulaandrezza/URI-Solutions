while True:
    n = int(input())
    if n == 0:
        break

    l = list(range(1, n+1))
    discard = []

    while len(l) > 1:
        discard.append(l.pop(0))
        t = l.pop(0)
        l.append(t)

    print("Discarded cards:", end= "")
    if len(discard) == 0:
        print()
    else:
        for e in discard:
            if e == discard[-1]:
                print(" %d" %e)
            else:
                print(" %d," %e, end="")

    print("Remaining card:", l[0])