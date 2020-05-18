from operator import itemgetter

n = int(input())
dic = {}

for i in range(n):
    x = int(input())

    if x in dic:
        dic[x] += 1
    else:
        dic[x] = 1

dic_sorted = sorted(dic.items(), key=itemgetter(0))
for i in dic_sorted:
    print("%d aparece %d vez(es)" %(i[0], i[1]))