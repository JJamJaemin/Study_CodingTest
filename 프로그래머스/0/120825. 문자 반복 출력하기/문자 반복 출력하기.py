def solution(my_string, n):
    answer = ''
    length = len(my_string)
    for i in range(0,length):
        answer += my_string[i] * n
    return answer