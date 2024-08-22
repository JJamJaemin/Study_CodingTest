import sys

n,a,b = map(int,sys.stdin.readline().split())
tile_A = list(map(int,sys.stdin.readline().split())) # 2*1 타일
tile_B = list(map(int,sys.stdin.readline().split())) # 2*2 타일
tile_A.sort()
tile_B.sort()

#n이 홀수 일때 -> A 타일을 무조건 사용
#n이 짝수 일때 -> A 타일을 사용하지 않을 수 잇음
answer = 0
if n % 2 == 1: #n이 홀수이면 A타일 무조건 사용
    if len(tile_A) >= 1:
        answer += tile_A[-1]
        tile_A.pop()
        n -= 1
for i in range(0,n,2):
    if len(tile_A) >= 2 and len(tile_B) < 1: #A타일이 2개 이상
        answer += tile_A[-1] + tile_A[-2]
        tile_A.pop()
        tile_A.pop()
    elif len(tile_A) >= 2 and len(tile_B) >= 1:
        if tile_A[-1] + tile_A[-2] >= tile_B[-1]:
            answer += tile_A[-1] + tile_A[-2]
            tile_A.pop()
            tile_A.pop()
        else:
            answer += tile_B[-1]
            tile_B.pop()
    elif len(tile_B) >= 1 and len(tile_A) < 2: # A타일을 2개를 사용하지 못할때
        answer += tile_B[-1]
        tile_B.pop()
print(answer)






