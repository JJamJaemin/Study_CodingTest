def solution(num_list):
    answer = 0
    length = len(num_list)
    if length > 10:
        for i in num_list:
            answer += i
    else:
        answer = 1
        for i in num_list:
            answer *= i
            
    return answer