num , Max = map(int,input().split())
L = [int(x) for x in input().split()]
b = 0
for i in L:
    if i >= L[Max-1] and i > 0 :
        b += 1
print(b)