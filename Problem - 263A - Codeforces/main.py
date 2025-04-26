I = J = 0
for i in range(5):
    one = list(map(int, input().split()))
    for j in one:
        if j == 1:
            J = one.index(j) + 1
            I = i + 1
            break
print(abs(3-J)+abs(3-I))