q = int(input())
e = input().split()

a = e.count("0")
b = e.count("1")

if a > b:
    print("Y")
else:
    print("N")
