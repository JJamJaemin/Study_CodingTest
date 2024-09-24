n = int(input())
list = list(map(int, input().split()))

answer = abs(list[0]+list[-1])
answer_index_start = 0
answer_index_end = n-1

start = 0
end = n-1
while start < end:
    tmp = list[start]+list[end]
    if abs(tmp) < answer:
        answer = abs(tmp)
        answer_index_start = start
        answer_index_end = end

    if tmp < 0 : #음수일 경우 시작점 index+1
        start = start + 1
    elif tmp > 0: #양수일 경우 끝점 index-1
        end = end - 1
    else: #0일 경우 종료
        break
print(list[answer_index_start], list[answer_index_end])
