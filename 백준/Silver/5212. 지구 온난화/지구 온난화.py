r, c = map(int, input().split())
map = [list(input()) for i in range(r)]
answer = [arr[:] for arr in map] #map 깊은 복사

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 잠기는 섬 찾아내기
for i in range(r):
    for j in range(c):
        if map[i][j] == 'X':
            cnt = 0
            for k in range(4): #4방향으로 바다가 몇개인지 찾기
                nx = i + dx[k]
                ny = j + dy[k]
                if 0 <= nx < r and 0 <= ny < c:
                    if map[nx][ny] == '.':
                        cnt += 1
                else:
                    cnt += 1
            if cnt >= 3: #바다가 3개 이상이면 잠기는 섬
                answer[i][j] = '.'

#지도 줄이기
min_i = r
min_j = c
max_i = 0
max_j = 0
for i in range(r):
    for j in range(c):
        if answer[i][j] == 'X':
            min_i = min(min_i, i)
            min_j = min(min_j, j)
            max_i = max(max_i, i)
            max_j = max(max_j, j)

for i in range(min_i, max_i + 1):
    print("".join(answer[i][min_j:max_j + 1]))

