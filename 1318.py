while True:
    n, m = [int(i) for i in input().split()]

    if n == m == 0:
        break

    dic = {}
    cont = 0

    bilhetes = input().split()

    for e in bilhetes:
        if e not in dic:
            dic[e] = 1
        else:
            dic[e] += 1

    for e in dic.values():
        if e > 1:
            cont += 1

    print(cont)