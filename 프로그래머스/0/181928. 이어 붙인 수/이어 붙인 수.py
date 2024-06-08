def solution(num_list):
    answer = 0
    tmp = ''
    tmp2 = ''
    for i in num_list:
        if i % 2 == 0:
            tmp = tmp + str(i)
        else:
            tmp2 = tmp2 + str(i)
    answer = int(tmp) + int(tmp2)
    return answer