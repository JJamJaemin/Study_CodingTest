def solution(i, j, k):
    answer = 0
    cnt = 0
    a = []
    for t in range(i,j+1):
        for m in str(t):
            a.append(m)
        if str(k) in a:
            cnt += a.count(str(k))
        a= []
    answer = cnt
    return answer