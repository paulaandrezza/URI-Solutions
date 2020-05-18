c = int(input())
p = 0

while p < c:
    q = 1
    media = 0
    cont = 0

    n = input().split()

    while q <= int(n[0]):
        media += int(n[q])
        q += 1

    media /= int(n[0])

    q = 1
    while q <= int(n[0]):
        if int(n[q]) > media:
            cont += 1
        q += 1

    print("%.3f%%" %(cont*100.0/float(n[0])))


    p += 1