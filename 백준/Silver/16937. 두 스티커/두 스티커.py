H, W = map(int, input().split()) #모눈종이 크기
N = int(input()) #스티커의 갯수

sticker = []
for i in range(N):
    x,y = map(int, input().split())
    sticker.append([x,y])
    #스티커 크기들 저장
answer = []
for i in range(N): #첫 번째 스티커 선택
    r1 = sticker[i][0] #가로
    c1 = sticker[i][1] #세로
    for j in range(i+1,N): #두번째 스티커 선택
        r2 = sticker[j][0]
        c2 = sticker[j][1]
        #가로로 나란히 붙일때
        if (r1+r2 <= W and max(c1,c2) <= H) or (c1+r2 <= W and max(r1,c2) <= H) or (r1+c2 <= W and max(c1,r2) <= H) or (c1+c2 <= W and max(r1,r2) <= H):
            answer.append(r1*c1 + c2*r2)
        #세로로 나란히 붙일때
        if (r1+r2 <= H and max(c1,c2) <= W) or (c1+r2 <= H and max(r1,c2) <= W) or (r1+c2 <= H and max(c1,r2) <= W) or (c1+c2 <= H and max(r1,r2) <= W):
            answer.append(r1*c1 + c2*r2)

#넓이 최대값 구하기
sorted_answer = sorted(answer)
if len(sorted_answer) != 0:
    print(sorted_answer[-1])
else:
    print(0)

