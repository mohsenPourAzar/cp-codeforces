n = int(input())
j = 0
for i in range(n):
    num = input().split()
    if num.count('1') >= 2:
        j +=1
print(j)

