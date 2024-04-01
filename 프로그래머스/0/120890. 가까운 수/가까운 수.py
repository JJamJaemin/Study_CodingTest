def solution(array, n):
    answer = 0
    min = 100000 
    for i in array:
        tmp = abs(n - i)
        if min > tmp:
            min = tmp
            answer = i
        if min == tmp:
            if answer > i:
                answer = i
    return answer