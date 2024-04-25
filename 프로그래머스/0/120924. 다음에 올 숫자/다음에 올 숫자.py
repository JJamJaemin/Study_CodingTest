def solution(common):
    answer = 0
    #등차수열
    if common[1] - common[0] == common[2] - common[1]:
        # a + dx
        answer = common[0] + (len(common))*(common[1]-common[0])
    #등비수열
    elif common[1] / common[0] == common[2] / common[1]:
        answer = common[0]*(common[2] / common[1])**(len(common))
    
    return answer