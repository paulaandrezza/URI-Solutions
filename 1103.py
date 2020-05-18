while True:
    a = input().split()
    if a[0] == '0' and a[1] == '0' and a[2] == '0' and a[3] == '0': break

    m1 = int(a[0])*60+int(a[1])
    m2 = int(a[2])*60+int(a[3])

    if m1 > m2:
        m = m2 + 24*60 - m1
    else:
        m = m2 - m1

    print("%d" %m)