abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

n = int(input())

for i in range(n):
    l = int(input())
    s = 0
    for j in range(l):
        e = input()
        for k, l in enumerate(e):
            s += abc.index(l) + j + k
    print(s)