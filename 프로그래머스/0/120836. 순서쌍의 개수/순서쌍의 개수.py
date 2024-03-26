def solution(n):
    answer = 0
    for i in range(1, int(n ** (1/2)+1)):
        if i*i == n:
            answer += 1
        elif n % i == 0:
            answer += 2
        else:
            continue
    return answer