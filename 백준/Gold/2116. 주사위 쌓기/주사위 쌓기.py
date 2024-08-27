n = int(input())
cube = [list(map(int, input().split())) for i in range(n)]

dict = {    # 마주 보고 있는 주사위의 인덱스 값
    0 : 5,
    1 : 3,
    2 : 4,
    3 : 1,
    4 : 2,
    5 : 0
}

def side_max(top):
    result = 0

    for i in range(n):
        for j in range(6):
            if cube[i][j] == top: #현재 주사위에서 top 이 적힌 값을 찾기
                bottom = cube[i][dict[j]] #적힌값의 반대편
                if 6 in [top,bottom]: # 윗면과 아랫면에 6이 들어갔을때
                    if 5 in [top,bottom]: # 5가 들어갔을때
                        result += 4
                    else:
                        result += 5
                else: # 6이 들어가지 않았을때
                    result += 6
                top = bottom #반대편 값을 업데이트하여 다음 주사위 면 결정
                break
    return result

answer = 0
for i in range(1,7):
    answer = max(answer, side_max(i))

print(answer)
