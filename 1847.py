a = input().split()
a[0] = int(a[0])
a[1] = int(a[1])
a[2] = int(a[2])

if (a[0] > a[1]):       # Desceu do 1° para o 2°
    if (a[1] <= a[2]):  # Subiu ou permaneceu constante do 2º para o 3º
        n = True
    elif (a[1] > a[2]): # Desceu do 2° para o 3°
        if (a[1] - a[2] < a[0] - a[1]): #desceu do 2º para o 3º menos do que descera do 1º para o 2º
            n = True
        else:
            n = False

elif (a[0] < a[1]):     # Subiu do 1° para o 2°
    if (a[1] >= a[2]):  # Desceu ou permaneceu constante do 2º para o 3º
        n = False
    elif (a[1] < a[2]): # Subiu do do 2º para o 3º
        if (a[2] - a[1] < a[1] - a[0]): # subiu do 2º para o 3º menos do que subira do 1º para o 2º
            n = False
        else:
            n = True

else:                   # Permaneceu constante
    if (a[2] > a[1]):
        n = True
    else:
        n = False

if (n):
    print(":)")
else:
    print(":(")