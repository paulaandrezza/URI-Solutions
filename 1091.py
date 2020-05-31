def regiao(n, m, x, y):
    if x == n or y == m:
        return "divisa"

    elif x < n and y > m:
        return "NO"

    elif x > n and y > m:
        return "NE"

    elif x < n and y < m:
        return "SO"

    else:
        return "SE"


while True:
    k = int(input())
    if k == 0:
        break

    n, m = [int(i) for i in input().split()]

    for e in range(k):
        x, y = [int(i) for i in input().split()]
        print(regiao(n, m, x, y))