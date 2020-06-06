while True:

    e = input().split()
    if e[0] == "0":
        break

    q, d, p = [int(i) for i in e]

    paginas = int(q*(p*d)/(p-q))

    if paginas == 1:
        print("%d pagina" %paginas)
    else:
        print("%d paginas" %paginas)