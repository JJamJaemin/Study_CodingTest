n,m = map(int,input().split())
grid = [list(map(int,input().split())) for i in range(n)]
dp = [[0 for i in range(m+1)]for j in range(n+1)]


for i in range(1, n+1):
    for j in range(1, m+1):
        dp[i][j] = grid[i-1][j-1] + max(dp[i-1][j], dp[i][j-1])

print(dp[-1][-1])