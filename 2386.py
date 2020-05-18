a = int(input())
n = int(input())

c = 0
d = 0

while c<n:

    b = int(input())

    if b*a >= 40000000:
        d +=1

    c += 1

print(d)