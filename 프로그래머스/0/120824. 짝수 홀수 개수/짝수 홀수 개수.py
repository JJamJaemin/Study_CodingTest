def solution(num_list):
    length = len(num_list)
    answer = [0] *2
    for i in range(length):
        if num_list[i] %2 == 0:
            answer[0] += 1
        else:
            answer[1] += 1
    return answer