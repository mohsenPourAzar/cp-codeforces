num = int(input())
string = input()
d = ""
s = 0
for i in string:
    if i == d:
        s += 1
    d = i
print(s)