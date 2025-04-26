num = list(map(int,input().split('+')))
num.sort()
d = ""
for i in num:
    d = d + str(i) + '+'
d = d[:-1]
print(d)
