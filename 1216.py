s = 0
n = 0

while True:
    try:

        nome = input()
        dist = int(input())

        n += 1
        s += dist

    except EOFError:
        break

print("%.1f" %(s/n))