C, R = map(int, input().split())  # C : 가로 R :세로
K = int(input())


def find_seat(C, R, K):
    if K > C * R:
        return 0

    seats = [[0] * C for _ in range(R)]
    dir_list = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 4방향 설정
    x, y = 0, 0  # 처음 위치
    dir = 0  # 방향 설정

    for i in range(1, K + 1):
        seats[y][x] = i  # 지나간 자리 체크

        if i == K:  # 해당 자리이면 return
            return (x + 1, y + 1)

        nx, ny = x + dir_list[dir][0], y + dir_list[dir][1]  # 다음 자리 탐색

        # 만약 다음 자리가 갈 수 없는 곳일때 조건 처리
        if nx < 0 or nx >= C or ny < 0 or ny >= R or seats[ny][nx] != 0:
            dir = (dir + 1) % 4  # 방향 설정
            nx, ny = x + dir_list[dir][0], y + dir_list[dir][1]  # 다음 자리 재 탐색

        x, y = nx, ny  # 위치 설정


answer = find_seat(C, R, K)

if answer == 0:
    print(0)
else:
    print(answer[0], answer[1])



