def solution(my_string, is_prefix):
    answer = 0
    length = len(is_prefix)
    if my_string[:length] == is_prefix:
        answer =1
    
            
    return answer