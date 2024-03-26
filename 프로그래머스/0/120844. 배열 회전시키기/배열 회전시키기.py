def solution(numbers, direction):
    answer = []
    tmp = 0
    length = len(numbers)
    if direction == 'left':
        tmp = numbers[0]
        for i in range(0,length-1):
            numbers[i] = numbers[i+1]
        numbers[-1] = tmp
    else:
        tmp = numbers[-1]
        for i in range(1,length):
            numbers[-i] = numbers[-i-1]
        numbers[0] = tmp
    answer = numbers
    return answer