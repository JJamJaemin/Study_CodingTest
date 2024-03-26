def solution(order):
    answer = 0
    tmp = 0
    ls = list(map(int,str(order)))
    for i in ls:
        if i!=0 and i%3 ==0:
            tmp += 1
    answer = tmp
    return answer