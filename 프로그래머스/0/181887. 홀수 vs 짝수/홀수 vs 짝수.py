def solution(num_list):
    answer = 0
    tmp = 0
    tmp2 = 0
    cnt = 1
    for i in num_list:
        if cnt % 2 == 0:
            tmp += i
        else:
            tmp2 += i
        cnt += 1
    if tmp > tmp2:
        answer = tmp
    else:
        answer = tmp2
    return answer