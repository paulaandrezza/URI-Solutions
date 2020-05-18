flag = 0

while True:
    n = int(input())

    if n == 0:
        break
    if flag == 1:
        print()

    L = []
    len_L = []

    for e in range(n):
        L.append(input())
        len_L.append(len(L[e]))

    s = max(int(number) for number in len_L)

    for e in L:
        print(e.rjust(s))
    flag = 1