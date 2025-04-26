num = input()
one = zero = z = 0
for i in num:
    if i == '1':
        one += 1
        zero = 0
    if i == '0':
        zero += 1
        one = 0
    if zero == 7 or one == 7:
        z = 1
if z == 1:
    print("YES")
else:
    print("NO")