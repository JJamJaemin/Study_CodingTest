def solution(my_string, num1, num2):
    answer = ''
    l = list(my_string)
    a = l[num1] 
    b = l[num2]
    l[num1] = b
    l[num2] = a
    
    answer = ''.join(l)
    return answer