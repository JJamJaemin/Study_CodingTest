def solution(n):
    count = n//2
    num = 2
    answer = 0
    for i in range(count):
        answer += num
        num += 2
    return answer