n = int(input())
map = []
for i in range(n):
    map.append(list(input()))
answer = []
def dfs(x,y):
    global count
    check_x = [1,-1,0,0]
    check_y = [0,0,1,-1]
    for i in range(4):
        nx = x+check_x[i]
        ny = y+check_y[i]
        if nx >= 0 and nx < n and ny >= 0 and ny < n:
            if map[nx][ny] == '1':
                count += 1
                map[nx][ny] = '2'
                dfs(nx,ny)

for i in range(n):
    for j in range(n):
        if map[i][j] == '1':
            map[i][j] = '2'
            count = 1
            dfs(i,j)
            answer.append(count)
print(len(answer))
sorted_answer = sorted(answer)
for i in sorted_answer:
    print(i)