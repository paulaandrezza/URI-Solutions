while True:
    try:
        n = int(input())
        dic = {}
        qtd = 0

        for e in range(n):
            m, l = input().split()

            p = 0 if l == "D" else 1

            if m not in dic:
                dic[m] = [0, 0]
                dic[m][p] = 1
            else:
                dic[m][p] += 1

        for value in dic.values():
            qtd += min(value[0], value[1])

        print(qtd)

    except EOFError:
        break