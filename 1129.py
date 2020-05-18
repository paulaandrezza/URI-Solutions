L = ['A', 'B', 'C', 'D', 'E']

while True:
    n = int(input())
    if (n == 0):
        break

    for i in range(n):
        c = 0
        a = input().split()

        for j in range(5):
            if (int(a[j]) <= 127 ):
                letra = L[j]
                c += 1

        if (c == 1):
            print(letra)
        else:
            print('*')