while True:
    try:

        n = int(input())

        century = n // 100
        if n % 100 > 0:
            century += 1

        print(century)

    except EOFError:
        break