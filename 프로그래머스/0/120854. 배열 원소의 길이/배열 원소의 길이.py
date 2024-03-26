def solution(strlist):
    length = len(strlist)
    answer = [0] * length
    for i in range(length):
        c_length = len(strlist[i])
        answer[i] = c_length
        
    return answer