while True:
    try:

        e = list(input())
        s = ""
        case = True

        for i in e:
            if i.isalpha():
                if case:
                    s += i.upper()
                    case= False
                else:
                    s += i.lower()
                    case= True
            else:
                s += i

        print(s)

    except EOFError:
        break