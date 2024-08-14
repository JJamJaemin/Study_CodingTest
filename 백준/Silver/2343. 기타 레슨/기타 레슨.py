N, M = map(int, input().split())
time = list(map(int, input().split()))

start = max(time) #가장 작을 수 있는 블루레이의 크기
end = sum(time) # 가장 클 수 있는 블루레이의 크기

while start <= end:
    mid = (start + end) // 2 # 가능한 블루레이 크기

    total = 0 # 블루레이 크기를 구할 임시 변수
    count = 1 # 블루레이 갯수를 구할 임시 변수
    for i in time:
        if total + i > mid: #설정된 블루레이 크기보다 크다면 임시 블루레이 크기를 초기화 블루레이 갯수 +1
            count += 1
            total = 0
        total += i

    if count <= M: #블루레이 갯수가 M 보다 작을경우 answer에 저장
        answer = mid
        end = mid -1
    else:
        start = mid + 1
print(answer)