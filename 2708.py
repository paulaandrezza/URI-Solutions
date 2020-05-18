p = 0
j = 0

while True:
    entrada = input().split()

    if entrada[0] == "ABEND":
        break
    elif entrada[0] == "SALIDA":
        j += 1
        p += int(entrada[1])
    else:
        j -= 1
        p -= int(entrada[1])

print(p)
print(j)