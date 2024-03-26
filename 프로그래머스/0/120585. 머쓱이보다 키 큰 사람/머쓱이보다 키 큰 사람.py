def solution(array, height):
    length = len(array)
    answer = 0
    for i in range(length):
        if height < array[i]:
            answer += 1
    
    return answer