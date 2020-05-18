n = int(input())

for i in range(n):
    a = input().split()
    L = []

    for e in a:
        L.append(e[0])

    print(''.join(L))
