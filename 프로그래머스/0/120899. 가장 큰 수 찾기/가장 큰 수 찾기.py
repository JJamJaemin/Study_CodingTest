def solution(array):
    answer = []
    tmp = 0
    tmp2 =0
    for i in array:
        if i > tmp:
            tmp = i
            answer = [tmp,tmp2]
        tmp2 +=1
    return answer