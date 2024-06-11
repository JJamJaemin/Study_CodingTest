def solution(n):
    answer = 0
    if n % 2 == 0:
        i = 0
        while i <= n:
            if i % 2 == 0:
                answer += i*i
            i += 1
    else:
        i = 0
        while i <= n:
            if i % 2 != 0:
                answer += i
            i += 1
    return answer