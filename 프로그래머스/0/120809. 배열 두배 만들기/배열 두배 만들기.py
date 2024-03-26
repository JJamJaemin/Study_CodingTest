def solution(numbers):
    length = len(numbers)
    answer = numbers
    
    for i in range(length):
        t = numbers[i] * 2
        answer[i] = t
    
    return answer