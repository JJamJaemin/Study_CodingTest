#N 바구니 갯수 M 공 바꾸는 횟수
N,M = input().split()
N = int(N)
M = int(M)
arr = []
for a in range(N):
    arr.append(a+1)
for b in range(M):
    tmp = 0
    i,j = input().split()
    i = int(i)
    j = int(j)
    tmp = arr[j-1]
    arr[j-1] = arr[i-1]
    arr[i-1] = tmp
answer = map(str,arr)
print(' '.join(answer))
    