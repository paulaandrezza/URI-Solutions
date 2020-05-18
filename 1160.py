t = int(input())

for i in range(t):
    anos = 0
    pa, pb, ga, gb = input().split()
    pa, pb, ga, gb = int(pa), int(pb), float(ga), float(gb)

    while True:
        pa = int(pa * (1 + ga/100))
        pb = int(pb * (1 + gb/100))
        anos += 1

        if pa > pb:
            break
        elif anos > 100:
            break

    if anos <= 100:
        print(anos, "anos.")
    else:
        print("Mais de 1 seculo.")