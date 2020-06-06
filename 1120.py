while True:
    d, n = input().split()
    if d == "0" and n == "0":
        break

    m = ""

    for e in n:
        if e != d:
            m += e

    if len(m) > 0:
        m = int(m)
        print(m)
    else:
        print("0")