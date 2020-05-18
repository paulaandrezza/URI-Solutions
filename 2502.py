while True:
    try:
        c, n = [int(i) for i in input().split()]
        a = input()
        b = input()

        for i in range(n):
            d = ""
            frase = input()

            for e in frase:
                if e.upper() in b:
                    pos = b.find(e.upper())
                    if e.isupper():
                        d += a[pos]
                    else:
                        d += a[pos].lower()

                elif e.upper() in a:
                    pos = a.find(e.upper())
                    if e.isupper():
                        d += b[pos]
                    else:
                        d += b[pos].lower()

                else:
                    d += e

            print(d)
        print("")

    except EOFError:
        break