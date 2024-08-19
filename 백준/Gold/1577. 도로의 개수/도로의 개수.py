n,m = map(int,input().split())
k = int(input())
blocked = []
for i in range(k):
  a,b,c,d = map(int,input().split())
  blocked.append([a,b,c,d])
  blocked.append([c,d,a,b])

dp = [[0 for i in range(m+1)] for j in range(n+1)]
dp[0][0] = 1


for i in range(0,n+1):
  for j in range(0,m+1):
    if i == 0 and j == 0:
      continue
    if [i,j-1,i,j] in blocked and [i-1,j,i,j] in blocked:
      dp[i][j] = 0
    elif [i,j-1,i,j] in blocked:
      dp[i][j] = dp[i-1][j]
    elif [i-1,j,i,j] in blocked:
      dp[i][j] = dp[i][j-1]
    else:
      dp[i][j] = dp[i][j-1] + dp[i-1][j]
print(dp[n][m])