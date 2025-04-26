n = int(input())
B = 0
for i in range(n):
    bit = input()
    if bit == "++X" or bit == "X++":
        B += 1
    if bit == "--X" or bit == "X--":
        B -= 1
print(B)
    