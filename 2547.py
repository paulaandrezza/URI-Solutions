while True:
    try:
        e = input().split()
        c = 0
        for i in range(int(e[0])):
            n = int(input())
            if (n >= int(e[1]) and n <= int(e[2])):
                c += 1

        print(c)

    except EOFError:
        break