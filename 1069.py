n = int(input())

for e in range(n):
    sinal = 0
    total = 0
    i = input()

    for f in i:
        if f == "<":
            sinal += 1
        elif f == ">" and sinal > 0 :
            total += 1
            sinal -= 1

    print(total)
