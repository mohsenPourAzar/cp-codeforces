x = int(input())
if x <= 5 :
    print(1)
else:
    i = 5
    if x % i == 0:
        print(int(x / i))
    else:
        print(int(x/i) + 1)