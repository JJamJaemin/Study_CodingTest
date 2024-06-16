def solution(a, b):
    answer = 0
    #a+b
    ab = str(a) + str(b)
    #ba
    ba = str(b) + str(a)
    if int(ab) >= int(ba):
        answer = int(ab)
    elif int(ba) > int(ab):
        answer = int(ba)

    return answer