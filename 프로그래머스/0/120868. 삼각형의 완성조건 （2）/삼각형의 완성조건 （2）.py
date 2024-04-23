def solution(sides):
    answer = 0
    cnt = 0
    tmp_answer = 0
    set_side = sorted(sides)
    #sides[1] 이 가장 긴변일 경우
    for i in range (1,set_side[1]+1):
        if (set_side[0] + i) > set_side[1]:
            tmp_answer += 1
            print(i)
            
    #새로운 변이 가장 긴변일 경우
    a = set_side[1] + 1
    while set_side[0] + set_side[1] > a:
        cnt += 1
        a += 1
        
    answer = tmp_answer + cnt
    # print(set_side)
    return answer