while True:
    a = input()

    if a == '0': break
    m = 0
    j = 0
    i = 0

    b = input().split()

    while i < int(a):
        if int(b[i]) == 0: m += 1
        else: j += 1
        i += 1
    print("Mary won %d times and John won %d times" %(m,j))
