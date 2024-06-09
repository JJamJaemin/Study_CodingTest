def solution(num_list):
    answer = 0
    tmp = 1
    tmp2 = 0
    for i in num_list:
        tmp *= i
        tmp2 += i
    tmp2 = tmp2 * tmp2
    if tmp < tmp2:
        answer = 1
    else:
        answer = 0
    
    return answer