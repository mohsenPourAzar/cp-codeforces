n = int(input())

while True:
    n += 1
    a = int(n/1000)
    b = int(n/100 % 10)
    c = int(n/10 % 10)
    d = int(n%10)
    if a != b and a != c and a != d and b != c and b != d and c != d:
        break
print(n)