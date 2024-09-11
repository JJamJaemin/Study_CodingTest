from collections import deque

n,m,k = map(int,input().split())
grid = [list(map(int,input().split())) for _ in range(n)]
answer = 0
needed_mursh = 0
def BFS(x, y):
    queue = deque([(x,y)])
    grid[x][y] = 1
    mursh = 1
    dx = [1,-1 ,0 ,0]
    dy = [0, 0, 1, -1]
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<n and 0<=ny<n and grid[nx][ny]==0:
                queue.append((nx,ny))
                grid[nx][ny] = 1
                mursh += 1
    return mursh

for i in range(n):
    for j in range(n):
        if grid[i][j]==0:
            mursh = BFS(i,j)
            needed_mursh = (mursh+ k -1) // k
            answer += needed_mursh

if answer <= m and needed_mursh > 0:
    print("POSSIBLE")
    print(m-answer)
else:
    print("IMPOSSIBLE")