def solution(my_string):
    answer = ''
    new_string = ''
    length = len(my_string)
    
    for i in range(0,length):
        if my_string[i] == 'a':
            tmp = my_string[i]
            
        elif my_string[i] == 'e':
            tmp = my_string[i]
            
        elif my_string[i] == 'i':
            tmp = my_string[i]
            
        elif my_string[i] == 'o':
            tmp = my_string[i]
            
        elif my_string[i] == 'u':
            tmp = my_string[i]
            
        else:
            new_string += my_string[i]
    answer = new_string
    return answer