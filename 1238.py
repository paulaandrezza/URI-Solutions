n = int(input())

for i in range(n):
    a, b = input().split()
    s = ""

    for e in range(max(len(a), len(b))):
        if e < len(a):
            s += a[e]
        if e < len(b):
            s += b[e]

    print(s)