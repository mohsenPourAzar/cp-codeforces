n = int(input())
for i in range(n):
    num = input()
    if len(num) > 10:
        print(num[0]+str(len(num)-2)+str(num[-1]))
    else:
        print(num)