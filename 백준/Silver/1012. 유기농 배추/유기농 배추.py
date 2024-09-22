from collections import deque
t = int(input())
for _ in range(t):
    m,n,k=map(int,input().split()) #m가로 n 세로 k배추 위치
    grid = [[0 for i in range(m)]for j in range(n)]

    for i in range(k):
        a,b=map(int,input().split())
        grid[b][a] = 1

    def bfs(x,y):
        q = deque([(x,y)])
        grid[y][x] = 2
        answer = 0
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        while q:
            x,y = q.popleft()
            for i in range(4):
                nx,ny = x+dx[i], y+dy[i]
                if 0 <= nx < m and 0 <= ny < n and grid[ny][nx] == 1:
                    q.append((nx,ny))
                    grid[ny][nx] = 2
                    answer += 1
        return answer

    answer = 0
    for i in range(m):
        for j in range(n):
            if grid[j][i] == 1:
                bfs(i,j)
                answer += 1
    print(answer)