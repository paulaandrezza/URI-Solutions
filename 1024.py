n = int(input())

for i in range(n):
    e = input()
    f = ""

    for j in list(e):
        if j.isalpha():
            f += chr(ord(j) + 3)
        else:
            f += j

    f = f[::-1]
    f = list(f)
    m = len(f) // 2

    for j, k in enumerate(f):
        if j >= m:
            f[j] = chr(ord(k) - 1)

    print(''.join(f))