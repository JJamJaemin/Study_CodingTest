def solution(slice, n):
    answer = 0
    a = int(n/slice)
    if n % slice == 0:
        answer = a
    else :
        a += 1
        answer = a
    return answer