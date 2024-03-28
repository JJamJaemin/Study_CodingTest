def solution(my_string):
    answer = ''
    ls = list(my_string)
    ls_index = []
    new_str = ''
    length = len(my_string)
    for i in range(0,length):
        tmp = ls[i]
        if new_str.find(tmp) == -1:
            new_str += tmp
                
        
    answer = new_str    
        
    return answer