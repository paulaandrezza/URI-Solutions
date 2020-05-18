abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

n = int(input())

for i in range(n):
    dec = ""
    s = input()
    d = int(input())

    for j in s:
        pos = abc.find(j)
        if pos < d:
            pos += 26
        dec += abc[pos - d]

    print(dec)
