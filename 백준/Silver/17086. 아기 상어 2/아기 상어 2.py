import queue
import sys
from collections import deque
sys.setrecursionlimit(1000000)


N, M = map(int, input().split())
space = [list(map(int, input().split())) for _ in range(N)]
shark = []
check_x = [1, -1, 0, 0, 1, 1, -1, -1]
check_y = [0, 0, 1, -1, 1, -1, 1, -1]
# print(space)
def bfs(shark):
    q = deque()

    for i in range(len(shark)):
        x,y = shark[i][0], shark[i][1]
        q.append((x,y))
        # print(q)
    while q:
        x, y = q.popleft()
        for i in range(8):
            nx, ny = x + check_x[i], y + check_y[i]
            if 0 <= nx < N and 0 <= ny < M:
                if space[nx][ny] == 0:
                    q.append((nx, ny))
                    space[nx][ny] = space[x][y] + 1
                    # print(space)

for i in range(N):
    for j in range(M):
        if space[i][j] == 1:
            shark.append((i, j))
bfs(shark)
max_dis = max(map(max, space))
print(max_dis-1)