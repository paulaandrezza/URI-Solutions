n = int(input())

for i in range(n):
    a, b = input().split()

    if (b == a[-len(b):]):
        print("encaixa")
    else:
        print("nao encaixa")