def solution(my_string, target):
    answer = 0
    length = len(target)
    for i in range(len(my_string)):
        print(my_string[i:i+length])
        if my_string[i:i+length] == target:
            answer = 1
    return answer