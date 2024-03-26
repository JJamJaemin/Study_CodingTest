def solution(n):
    answer = 0
    a = int(n /7)
    c = n%7
    
    if a == 0 and c > 0:
        answer =1 
    elif a > 0 and c == 0:
        answer = a
    else :
        answer = a+1
        
    return answer