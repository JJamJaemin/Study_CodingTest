ls = [0] * 9
for i in range(9):
    A = input()
    ls[i] = int(A)
Max = max(ls)
print(Max)
index = ls.index(Max)
print(index + 1)