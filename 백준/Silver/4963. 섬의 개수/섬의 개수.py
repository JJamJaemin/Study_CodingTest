from collections import deque
import sys
#8방향
dx = [1,1,1,0,0,-1,-1,-1]
dy = [1,0,-1,1,-1,1,0,-1]

def BFS(x, y):
    queue = deque()
    queue.append([x,y])
    grid[y][x] = 0
    while queue:
        x,y = queue.popleft()
        for i in range(8):
            if (x + dx[i]) >= 0 and (x + dx[i]) < w and (y + dy[i]) >= 0 and (y + dy[i]) < h:
                if grid[y+dy[i]][x+dx[i]] == 1:
                    queue.append([x+dx[i],y+dy[i]])
                    grid[y+dy[i]][x+dx[i]] = 0

while True: # 0 0이 들어올때까지 무한 반복
    w,h = map(int,input().split())
    if w == 0 and h == 0:
        break
    grid = list()
    answer = 0
    for i in range(h):
        grid.append(list(map(int,sys.stdin.readline().split()))) #지도 만들기

    for i in range(h): #y
        for j in range(w): # x
            if grid[i][j] == 1: # [y][x]
                answer += 1
                BFS(j,i)
    print(answer) #섬의 개수 출력



