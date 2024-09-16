m,n = map(int,input().split()) # m : gird 크기 n: 명령 개수

direction = 0 # 0 오른쪽 1 위 2 왼쪽 3 아래
answer = 0
answer_x, answer_y = 0, 0
y,x = 0,0

for i in range(n):
    command, cnt = map(str, input().split())
    cnt = int(cnt)

    if command == 'MOVE':
        if direction == 0: #우측
            if x + cnt <= m:
                y, x = y, x + cnt
            else:
                answer = -1
                break
        elif direction == 1:
            if y + cnt <= m:
                y, x = y + cnt, x
            else:
                answer = -1
                break
        elif direction == 2:
            if x - cnt >= 0:
                y, x = y, x - cnt
            else:
                answer = -1
                break
        elif direction == 3:
            if y - cnt >= 0:
                y, x = y - cnt, x
            else:
                answer = -1
                break
    elif command == 'TURN':
        if cnt == 0: #왼쪽 90 도
            if direction == 3 :
                direction = 0
            else:
                direction += 1
        elif cnt == 1: #오른쪽 90도
            if direction == 0 :
                direction = 3
            else:
                direction -= 1
if answer != -1:
    answer_x, answer_y = x, y
    print(answer_x, answer_y)
else:
    print(answer)