n = int(input())
c = 0

while c < n:
    d = 0
    r = 0

    a = int(input())

    while d < a:

        r = r + 2**d

        d += 1

    print(r)

    c += 1