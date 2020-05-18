n = int(input())
c = 0

while c < n:

    a = input()

    if a[0] == a[2]:
        r = int(a[0]) * int(a[2])
    elif a[1].isupper():
        r = int(a[2]) - int(a[0])
    elif a[1].islower():
        r = int(a[0]) + int(a[2])

    print(r)

    c += 1