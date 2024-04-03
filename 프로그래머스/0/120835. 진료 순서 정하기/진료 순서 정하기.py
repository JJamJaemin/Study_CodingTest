def solution(emergency):
    answer = []
    ls = sorted(emergency, reverse = True)
    length = len(emergency)
    tmp = 0
    for i in emergency:
        tmp = ls.index(i)
        answer.append(tmp+1)
    return answer