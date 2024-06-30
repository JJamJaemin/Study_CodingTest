X = input()
N = input()
X = int(X)
N = int(N)
tmp = 0
for i in range(N):
    a, b = input().split()
    a = int(a)
    b = int(b)
    tmp += a * b
if X == tmp:
    print("Yes")
else:
    print("No")