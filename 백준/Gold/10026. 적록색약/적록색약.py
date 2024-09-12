from collections import deque
import copy

n = int(input())
grid = [list(input()) for _ in range(n)]
grid2 = copy.deepcopy(grid)
m = len(grid[0])
cnt_R, cnt_G, cnt_B = 0, 0, 0
cnt_R2, cnt_G2, cnt_B2 = 0, 0, 0
answer = 0

def BFS(x,y, RGB): #정상인
    queue = deque([(x,y)])
    grid[y][x] = 'A'
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx,ny = x+dx[i], y+dy[i]
            if 0<=nx<n and 0<=ny<n and grid[ny][nx]== RGB:
                queue.append((nx,ny))
                grid[ny][nx] = 'A'

def BFS_rg(x,y,RGB): #적녹 색맹
    queue = deque([(x,y)])
    grid2[y][x] = 'A'
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    while queue:
        x,y = queue.popleft()
        for i in range(4):
            nx,ny = x+dx[i], y+dy[i]
            if (RGB == 'R' or RGB == 'G') and 0<=nx<n and 0<=ny<n and (grid2[ny][nx]=='G' or grid2[ny][nx]=='R'):
                queue.append((nx,ny))
                grid2[ny][nx] = 'A'
            elif 0<=nx<n and 0<=ny<n and grid2[ny][nx] == RGB:
                queue.append((nx,ny))
                grid2[ny][nx] = 'A'

for i in range(n): #세로 y
    for j in range(m): #가로 x
        if grid[i][j] == 'R':
            RGB = 'R'
            cnt_R += 1
            BFS(j,i,RGB)
        elif grid[i][j] == 'G':
            RGB = 'G'
            cnt_G += 1
            BFS(j,i,RGB)
        elif grid[i][j] == 'B':
            RGB = 'B'
            cnt_B += 1
            BFS(j,i,RGB)

        if grid2[i][j] == 'R':
            RGB = 'R'
            cnt_R2 += 1
            BFS_rg(j,i,RGB)
        elif grid2[i][j] == 'G':
            RGB = 'G'
            cnt_G2 += 1
            BFS_rg(j,i,RGB)
        elif grid2[i][j] == 'B':
            RGB = 'B'
            cnt_B2 += 1
            BFS_rg(j,i,RGB)

answer = cnt_R + cnt_G + cnt_B
answer2 = cnt_R2 + cnt_G2 + cnt_B2
print(answer, answer2)


