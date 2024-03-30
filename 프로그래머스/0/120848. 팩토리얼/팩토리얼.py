def solution(n):
    answer = 0
    result = 1
    for i in range(1,3628800):
        result = result * i
        if result > n:
            answer = i -1
            break
    return answer
