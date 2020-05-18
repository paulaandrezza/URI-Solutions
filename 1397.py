while True:
    a = 0
    b = 0

    n = int(input())
    if n == 0: break

    for i in range(n):
        a1, b1 = input().split()
        if int(a1) > int(b1): a += 1
        elif int(b1) > int(a1): b += 1

    print(a, b)