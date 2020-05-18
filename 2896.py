n = int(input())

for i in range(n):
    n, k = input().split()

    g = int(int(n) / int(k)) + int(int(n) % int(k))

    print(g)