def solution(numbers):
    answer = 0
    max_1 = numbers[0]
    max_2 = 0
    length = len(numbers)
    
    for i in range(1, length):
        if max_1 > numbers[i]:
            if max_2 <= numbers[i]:
                max_2 = numbers[i]
        if max_1 <= numbers[i]:
            if numbers[i] > max_2:
                tmp = max_1
                max_1 = numbers[i]
                max_2 = tmp
          
    answer = max_1 * max_2
    print(max_1 , max_2)
    return answer