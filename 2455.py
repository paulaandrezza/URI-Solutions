a = input().split()

if int(a[0]) * int(a[1]) == int(a[2]) * int(a[3]):
    print("0")
elif int(a[0]) * int(a[1]) > int(a[2]) * int(a[3]):
    print("-1")
else:
    print("1")