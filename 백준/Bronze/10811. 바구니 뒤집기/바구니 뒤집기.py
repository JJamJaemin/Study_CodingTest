#N 바구니 갯수 
N,M = input().split()
N = int(N)
M = int(M)
ls = [0] * N
for a in range(N):
    ls[a] = a+1
for b in range(M):
    i,j = input().split()
    i = int(i)-1
    j = int(j)
    
    nls = ls[i:j]
    nls.reverse()
    ls[i:j] = nls
answer = map(str,ls)
print(' '.join(answer))