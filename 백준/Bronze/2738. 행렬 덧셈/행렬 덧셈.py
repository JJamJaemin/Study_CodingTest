n,m = input().split()
n = int(n)
m = int(m)
arr = [[0] * m for _ in range(n)]
arr2 = [[0] * m for _ in range(n)]
answer = [[0] * m for _ in range(n)]

for i in range(n):
    arr[i] = input().split()
for j in range(n):
    arr2[j] = input().split()

for i in range(n):
    for j in range(m):
        answer[i][j] = int(arr[i][j]) + int(arr2[i][j])
    a = ' '.join(map(str, answer[i]))
    print(a)