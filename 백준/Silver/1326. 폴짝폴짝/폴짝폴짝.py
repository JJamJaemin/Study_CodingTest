from collections import deque

N = int(input())
bridge = list(map(int, input().split()))
bridge.insert(0,0)
a,b = map(int, input().split())

def BFS(start, end):
    queue = deque([start]) #시작 위치 설정
    visited = [-1] * (N+1) # 방문 노드 표시 (방문하지 않은곳 -1)
    visited[start] = 0
    while queue:
        now = queue.popleft() #현재 노드 탐색
        # 오른쪽 방향 탐색
        for i in range(now, N + 1 , bridge[now]):
            if visited[i] == -1 :
                queue.append(i)
                visited[i] = visited[now] + 1 #i까지 도달하는데 필요한 점프 횟수 추가
                if i == end:
                    return visited[i]
        # 왼쪽 방향 탐색
        for i in range(now, 0, -bridge[now]):
            if visited[i] == -1:
                queue.append(i)
                visited[i] = visited[now] + 1
                if i == end:
                    return visited[i]
    return -1

print(BFS(a, b))





