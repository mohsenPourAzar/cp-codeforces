k , n , w = map(int,input().split())
t = 0
for i in range(1,w+1):
    t = t + (i * k)
if n >= t:
    print(0)
else:
    print(t-n)