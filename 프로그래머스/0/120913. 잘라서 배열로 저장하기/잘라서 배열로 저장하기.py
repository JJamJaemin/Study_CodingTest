def solution(my_str, n):
    answer = []
    length = len(my_str)
    tmp = ''
    cnt = 0
    l = 0
    while l < length:
        for i in range(0,n):
            if cnt == 0:
                tmp += my_str[i]
                
            elif cnt > 0 and l < length:
                tmp += my_str[cnt+i]
            l += 1
            
            
        cnt += n
        answer.append(tmp)
        tmp = ''
        
    return answer