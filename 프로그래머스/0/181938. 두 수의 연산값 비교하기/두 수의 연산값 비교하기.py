def solution(a, b):
    answer = 0
    #a+b
    plus = str(a) + str(b)
    #2*a+b
    plus2 = 2*a*b
    if int(plus) >plus2:
        answer = int(plus)
    elif int(plus) < plus2:
        answer = plus2
    else:
        answer = int(plus)
    return answer