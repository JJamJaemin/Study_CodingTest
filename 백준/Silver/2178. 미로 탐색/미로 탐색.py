from collections import deque

n,m = map(int ,input().split())
grid = list()
for i in range(n):
    grid.append(list(map(int, str(input()))))



def BFS(x,y):
    # 4방향
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    queue = deque()
    queue.append([x,y])
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            if 0 <= x+dx[i] < n and 0 <= y+dy[i] < m and grid[x+dx[i]][y+dy[i]] == 1:
                queue.append([x+dx[i], y+dy[i]])
                grid[x+dx[i]][y+dy[i]] = grid[x][y] + 1
    return grid[n-1][m-1]


print(BFS(0,0))

