from collections import deque

N = int(input())
grid = list(map(int, input().split()))

queue = deque([(0, 0)]) #위치, 점프횟수
visited = [0]
answer = -1

while queue:
    now, step = queue.popleft()
    if now == N - 1:
        answer = step
        break

    #현재칸에서 갈 수 있는 곳 체크
    for i in range(1, grid[now]+1):
        can_jump =  now + i
        if can_jump < N and can_jump not in visited:
            queue.append((can_jump, step + 1))
            visited.append(can_jump)

print(answer)
