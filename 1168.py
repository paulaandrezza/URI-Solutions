L = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]

n = int(input())

for i in range(n):
    l = 0
    e = list(input())

    for j in e:
        l += L[int(j)]

    print("%d leds" %l)