#N 바구니 갯수 , M 몇번 넣는지(줄)
N,M = input().split()
N = int(N)
M = int(M)
ls = [0] * N
for c in range(M):
  i,j,k = input().split()
  i = int(i)
  j = int(j)
  k = int(k)
  for a in range(i-1,j):
    cnt = 1
    for b in range(k):
      ls[a] = cnt
      cnt += 1
answer = map(str,ls)
print(" ".join(answer))