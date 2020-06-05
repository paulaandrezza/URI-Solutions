pos = [1, 3, 5, 10, 25, 50, 100]

n = int(input())

for e in pos:
    if n <= e:
        print("Top %d" %e)
        break