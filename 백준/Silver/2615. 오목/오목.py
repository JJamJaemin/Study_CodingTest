grid = []

for i in range(19):
    grid.append(list(map(int, input().split())))

dx = [1, 1, 1, 0]  # 오른쪽, 오른쪽 아래, 아래, 왼쪽 아래
dy = [0, 1, -1, 1]  # 방향에 따른 y 변화

omok = False

for i in range(19):  # i는 y좌표
    if omok:
        break
    for j in range(19):  # j는 x좌표
        if omok:
            break
        if grid[i][j] != 0:  # 바둑알이 있는 경우
            player = grid[i][j]
            for m in range(4):  # 4방향 탐색 (반대방향은 하지 않음)
                cnt = 1  # 현재 위치에서 시작
                nx, ny = j, i  # 현재 위치

                # 5개의 돌이 연속적으로 있는지 확인
                for k in range(4):  # 최대 4칸 더 탐색 (총 5칸)
                    nx += dx[m]
                    ny += dy[m]
                    if 0 <= nx < 19 and 0 <= ny < 19 and grid[ny][nx] == player:
                        cnt += 1
                    else:
                        break

                # 5개의 돌이 연속되는 경우
                if cnt == 5:
                    # 6목인지 확인 (앞쪽 돌이 같은지)
                    prev_x = j - dx[m]
                    prev_y = i - dy[m]
                    if not (0 <= prev_x < 19 and 0 <= prev_y < 19 and grid[prev_y][prev_x] == player):
                        # 6목인지 확인 (뒤쪽 돌이 같은지)
                        next_x = nx + dx[m]
                        next_y = ny + dy[m]
                        if not (0 <= next_x < 19 and 0 <= next_y < 19 and grid[next_y][next_x] == player):
                            print(player)  # 승리한 돌 색 출력
                            print(i + 1, j + 1)  # 시작 좌표 출력 (가장 왼쪽/위쪽 돌 좌표)
                            omok = True
                            break
if omok == False:
    print(0)