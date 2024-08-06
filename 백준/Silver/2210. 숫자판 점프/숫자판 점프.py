digit = [[],[],[],[],[]]
answer_list = []
answer = ''
def dfs(x,y,answer):
    if len(answer) == 6:
        answer_list.append(answer)
        return

    check_x = [1,-1,0,0]
    check_y = [0,0,1,-1]
    for i in range(4):
        nx = x + check_x[i]
        ny = y + check_y[i]
        if nx >= 0 and nx < 5 and ny >= 0 and ny < 5:
            dfs(nx,ny,answer+digit[nx][ny])

for i in range(5):
    digit[i] = list(map(str, input().split()))


for i in range(5):
    for j in range(5):
        dfs(i,j,digit[i][j])
print(len(set(answer_list)))




