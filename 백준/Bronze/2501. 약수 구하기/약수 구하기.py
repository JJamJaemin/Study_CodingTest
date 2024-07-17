N,K = map(int,input().split())
A = []
cnt = 1
while(cnt <= N):
    if N % cnt == 0:
        A.append(cnt)
    cnt += 1
if K > len(A):
    print(0)
else:
    print(A[K-1])
