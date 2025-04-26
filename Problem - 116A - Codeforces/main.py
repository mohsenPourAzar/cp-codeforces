num = int(input())
Max = res = 0
for i in range(num):
    a,b = map(int,input().split())
    res -= a
    res += b
    if res > Max:
        Max = res
print(Max)
