def solution(my_string, is_suffix):
    answer = 0
    length = len(is_suffix)
    if my_string[len(my_string)-length:] == is_suffix or my_string == is_suffix:
        answer = 1
    else:
        answer = 0
    
    return answer