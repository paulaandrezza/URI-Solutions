c = int(input())

rpm = input().split()

for i in range(1, c):
    if (int(rpm[i]) < int(rpm[i-1])):
        print("%d" %(i+1))
        break
else:
    print('0')