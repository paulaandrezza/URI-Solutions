def maior(array):
    m = array[0]

    for i in range(1, len(array)):
        if array[i] > m:
            m = array[i]

    return m

while True:
    n = int(input())

    if n == 0:
        break

    e = [int(i) for i in input().split()]
    f = e[:]

    p = maior(f)
    del(f[f.index(p)])
    p = maior(f)
    p = e.index(p)

    print(p + 1)
