import sys
sys.stdout = open(sys.stdout.buffer.fileno(), 'w', encoding='utf8')

while True:
    try:
        m = int(input())
        v = []
        soma = int(0)
        primo = True
        for i in range(m):
            v.append(int(input()))
        s = int(input())

        i = m - 1
        while i >= 0:
            soma += v[i]
            i -= s

        if (soma == 1 or soma % 2 == 0 and soma != 2):
            primo = False
        else:
            raiz = int(soma*1/2) + 1
            for i in range(3, raiz, 2):
                if (soma % i == 0):
                    primo = False
                    break

        if primo:
            print("You’re a coastal aircraft, Robbie, a large silver aircraft.")
        else:
            print("Bad boy! I’ll hit you.")
    except EOFError:
        break