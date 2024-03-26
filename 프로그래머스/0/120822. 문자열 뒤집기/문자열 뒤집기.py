def solution(my_string):
    
    new_string = ''
    
    for char in my_string:
        new_string = char + new_string
    
    answer = new_string
    return answer