def solution(numbers):
    i = 0
    sum = 0
    for i in range(len(numbers)):
        sum += numbers[i]
    answer = sum/len(numbers)
    return answer