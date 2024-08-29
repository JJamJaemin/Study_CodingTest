import sys
sys.setrecursionlimit(1000000)

n = int(sys.stdin.readline())
tree = [[] for i in range(0,n+1)]

for i in range(n-1):
    a, b = map(int, sys.stdin.readline().split())
    tree[a].append(b) #a번 노드와 인접한 노드
    tree[b].append(a) #b번 노드와 인접한 노드

visited = [0] * (n+1) #방문 노드 즉 부모노드

def dfs(node):
    for i in tree[node]:
        if visited[i] == 0:
            visited[i] = node
            dfs(i)

dfs(1) #첫번째 노드부터 dfs

for a in range(2,n+1): # 두번째 노드 부터 출력
    print(visited[a])
