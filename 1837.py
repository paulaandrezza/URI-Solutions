a, b = input().split()

r = int(a) % abs(int(b))
q = (int(a) - r) / int(b)

print("%d %d" % (q, r))