def yn(e):
    letra = e[0][0].lower()

    for i in e:
        if i[0].lower() != letra:
            return "N"
            break
    else:
        return "Y"


while True:
    e = input().split()
    if e[0] == "*":
        break

    print(yn(e))