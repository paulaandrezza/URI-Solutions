def number(e):
    c = 0
    p = "one"
    if len(e) == 5:
        return 3
    else:
        for j in range(3):
            if e[j] == p[j]:
                c += 1
        if c >= 2:
            return 1
        else:
            return 2

n = int(input())

for i in range(n):
    e = input()

    print(number(e))