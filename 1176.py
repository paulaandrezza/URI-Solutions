t = int(input())

for i in range(t):
    a = int(input())
    p = [0, 1]
    q = p[:]

    for i in range(2, (a+1)):
        n = q[i-2] + q[i-1]
        q.append(n)
    print("Fib(%d) = %d" %(a, q[a]))