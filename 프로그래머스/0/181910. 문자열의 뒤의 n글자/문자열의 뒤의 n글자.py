def solution(my_string, n):
    answer = ''
    length = len(my_string)
    answer = my_string[length - n:]
    return answer