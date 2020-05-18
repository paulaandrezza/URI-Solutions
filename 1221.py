n = int(input())
c = 0

while c < n:
    c2 = 3
    c3 = 0

    a = int(input())

    if a == 2:
        print("Prime")
    elif a % 2 == 0:
        print("Not Prime")
    else:
        while c2 < a**(1/2) + 1:
            if a % c2 == 0:
                c3 += 1
                break
            c2 += 2

        if c3 == 1:
            print("Not Prime")
        else:
            print("Prime")

    c += 1