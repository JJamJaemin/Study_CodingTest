def solution(n, k):
    answer = []
    i = 1
    t = k
    while t <= n:
        t = k*i
        if t <= n:
            answer.append(t)
        i += 1
    return answer