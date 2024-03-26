def solution(n):
    answer = 0
    tmp = int(n**(1/2))
    if tmp *tmp == n:
        answer = 1
    else:
        answer = 2
    return answer