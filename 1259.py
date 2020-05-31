def print_(array):
    for e in array:
        print(e)


n = int(input())
lp = []
li = []

for e in range(n):
    i = int(input())
    if i % 2:
        li.append(i)
    else:
        lp.append(i)


lp = sorted(lp)
li = sorted(li, reverse=True)

print_(lp)
print_(li)