def solution(array, n):
    count =0
    answer = 0
    length = len(array)
    for i in range(length):
        if array[i] == n:
            count += 1
    answer = count
    return answer