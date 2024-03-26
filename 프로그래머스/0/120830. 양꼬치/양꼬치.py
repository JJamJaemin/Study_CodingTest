def solution(n, k):
    if n>=10 :
        ser=n//10
        k = k-ser
    cal = 12000*n + 2000*k
    answer = cal
    return answer