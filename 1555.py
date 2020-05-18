n = int(input())
cont = 0

while cont < n:

    x,y = input().split()

    r = (3*int(x))**2 + int(y)**2
    b = 2*int(x)**2 + (5*int(y))**2
    c = -100*int(x) + int(y)**3

    if r > b and r > c:
        print("Rafael ganhou")
    elif b > c and b > r:
        print("Beto ganhou")
    else:
        print("Carlos ganhou")

    cont += 1
