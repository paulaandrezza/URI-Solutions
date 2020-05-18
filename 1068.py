while True:
    try:
        L = []
        e = list(input())

        x = 0
        while (x < len(e)):
            if (e[x] == '(' or e[x] == ')'):
                x += 1
            else:
                del e[x]

        x = 0
        while (x < len(e)):
            if (e[x] == '('):
                L.append("(")
            if (e[x] == ')'):
                if (len(L) > 0):
                    del L[-1]
                else:
                    L.append(")")
            x += 1

        if (len(L) == 0):
            print("correct")
        else:
            print("incorrect")

    except EOFError:
        break