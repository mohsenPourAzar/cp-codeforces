n = int(input())
s = input()
A = s.count('A')
D = s.count('D')
if A>D :
    print("Anton")
elif D>A :
    print("Danik")
else:
    print("Friendship")