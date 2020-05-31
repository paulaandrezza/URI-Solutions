a = input().replace(" ", "")
a = int(a, 2)
b = input().replace(" ", "")
b = int(b, 2)

if ((a ^ b) == 0b11111):
    print("Y")
else:
    print("N")