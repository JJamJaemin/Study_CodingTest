def solution(chicken):
    answer = 0
    tmp = 0
    ticket = chicken
    while ticket // 10 > 0:
        tmp = ticket // 10 
        answer += ticket//10
        ticket = (ticket - (10*tmp)) + tmp
        tmp = 0
    return answer