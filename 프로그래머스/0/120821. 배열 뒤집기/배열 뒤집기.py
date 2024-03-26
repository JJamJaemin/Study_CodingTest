def solution(num_list):
    length = len(num_list)
    answer = [0] * length
    for i in range(length):
        answer[i] = num_list[length-1-i]
    return answer