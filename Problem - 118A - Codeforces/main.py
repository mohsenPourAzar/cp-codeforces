str0= input().lower()
for i in str0:
    if i == 'a' or i == 'o' or i == 'y' or i == 'e' or i == 'u' or i == 'i':
        str0 = str0.replace(i, '')
d = ""
for i in str0:
    d = d + '.' + i
print(d)
