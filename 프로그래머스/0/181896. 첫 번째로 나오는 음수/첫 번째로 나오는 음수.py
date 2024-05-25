def solution(num_list):
    answer = 0
    cnt = 0
    for i in num_list:
        if i < 0:
            if cnt == 0:
                answer = 0
                break
            else:  
                answer = cnt
                break
        else:
            cnt += 1
    if cnt != 0 and answer == 0:
        answer = -1
    return answer