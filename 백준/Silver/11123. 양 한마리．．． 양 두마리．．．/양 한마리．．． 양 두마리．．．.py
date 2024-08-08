import sys
sys.setrecursionlimit(100000)
T = int(input())

def dfs(x, y):
    check_x = [1, -1, 0, 0]
    check_y = [0, 0, 1, -1]
    for i in range(4):
        nx = x + check_x[i]
        ny = y + check_y[i]
        if 0 <= nx < H and 0 <= ny < W:
            if grid[nx][ny] == '#':
                grid[nx][ny] = '1'
                dfs(nx, ny)
            elif i == 3:
                return

for t in range(T):
    H, W = map(int, input().split())
    grid = [list(input()) for _ in range(H)]
    count = 0
    for i in range(H):
        for j in range(W):
            if grid[i][j] == '#':
                dfs(i, j)
                count += 1
    print(count)