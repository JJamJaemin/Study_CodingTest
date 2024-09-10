from collections import deque

n = int(input()) #컴퓨터의 수
pair = int(input()) #연결된 쌍의 수
computer = list()
graph = [[] for _ in range(n+1)] #그래프 초기화
visited = [0] * (n+1)

for i in range(pair):
    a,b = map(int,input().split())
    graph[a] += [b] #a에 b연결
    graph[b] += [a] #b에 a연결

visited[1] = 1
queue = deque([1])
while queue:
    now = queue.popleft()
    for i in graph[now]:
        if visited[i] == 0:
            queue.append(i)
            visited[i] = 1
print(sum(visited) -1) #1번 컴퓨터를 제외한 개수
