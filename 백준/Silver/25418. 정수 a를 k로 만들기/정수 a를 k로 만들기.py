from collections import deque

a,k = map(int,input().split())

queue = deque([(a,0)]) #a값, 연산횟수
visited = set([a])
answer = 0
while queue:
    now, answer = queue.popleft()

    if now == k:
        break
    if (now + 1) <= k and (now + 1) not in visited:
        visited.add(now + 1)
        queue.append((now+1, answer+1))
    if (now * 2) <= k and (now * 2) not in visited:
        visited.add(now * 2)
        queue.append((now*2 , answer + 1))


print(answer)



