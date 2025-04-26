s = input()
h = 'hello'
j = pas = 0
for i in s:
    if i == h[j]:
        j += 1
        pas += 1
        if pas == 5:
            break
if pas == 5:
    print('YES')
else:
    print('NO')

