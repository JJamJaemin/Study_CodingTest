N = [[]*9]*9
max = 0
for i in range(9):
    N[i]=list(map(int,input().split()))
    for j in range(9):
        if N[i][j]>=max:
            max=N[i][j]
            a = i+1
            b = j+1
print(max)
print(a,b)