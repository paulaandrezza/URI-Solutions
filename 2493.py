while True:
    try:

        t = int(input())
        f = []
        s = []

        for i in range(t):
            entrada = input().replace("=", " ")
            f.append(entrada.split())

        for i in range(t):
            r = input().split()

            e = f[int(r[1]) - 1]
            e[0] = int(e[0])
            e[1] = int(e[1])
            e[2] = int(e[2])

            if r[2] == "+":
                if e[0] + e[1] != e[2]:
                    s.append(r[0])
            elif r[2] == "-":
                if e[0] - e[1] != e[2]:
                    s.append(r[0])
            elif r[2] == "*":
                if e[0] * e[1] != e[2]:
                    s.append(r[0])
            elif r[2] == "I":
                if (e[0] + e[1] == e[2]) or (e[0] - e[1] == e[2]) or (e[0] * e[1] == e[2]):
                    s.append(r[0])

        if len(s) == 0:
            print("You Shall All Pass!")
        elif len(s) == t:
            print("None Shall Pass!")
        else:
            so = sorted(s)
            print(" ".join(so))

    except EOFError:
        break