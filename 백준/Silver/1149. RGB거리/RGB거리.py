n = int(input())
grid = [list(map(int,input().split())) for i in range(n)]

dp = [[0]* 3 for _ in range(n)]

# dp[i][0] R
# dp[i][1] G
# dp[i][2] B
dp[0][0] = grid[0][0]
dp[0][1] = grid[0][1]
dp[0][2] = grid[0][2]

for i in range(1,n):
    dp[i][0] = min(dp[i-1][1] + grid[i][0], dp[i-1][2] + grid[i][0]) #빨강을 칠할때
    dp[i][1] = min(dp[i-1][0] + grid[i][1], dp[i-1][2] + grid[i][1]) #초록을 칠할때
    dp[i][2] = min(dp[i-1][0] + grid[i][2], dp[i-1][1] + grid[i][2]) #파랑을 칠할때

print(min(dp[n-1][0], dp[n-1][1], dp[n-1][2]))