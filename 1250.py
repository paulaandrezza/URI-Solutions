n = int(input())

for i in range(n):
    t = int(input())
    a = input().split()
    s = input()

    c = 0

    for j in range(t):
        if (int(a[j]) <= 2):
            if (s[j] == 'S'):
                c +=1
        else:
            if (s[j] == 'J'):
                c += 1
    print(c)