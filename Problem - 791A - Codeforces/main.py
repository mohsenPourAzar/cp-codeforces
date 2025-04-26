a, b = map(int,input().split())
i = 1
while(True):
    a *= 3*i
    b *= 2*i
    if a>b:
        break
    i +=1
print(i)