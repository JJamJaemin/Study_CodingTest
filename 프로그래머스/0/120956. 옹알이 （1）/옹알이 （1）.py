def solution(babbling):
    answer = 0
    cnt = -1
    word = ['aya','ye','woo','ma','aya','ye','woo','ma','aya','ye','woo','ma','aya','ye','woo','ma']
    for i in babbling:
        cnt += 1
        for j in word:
            #print(i.find(j))
            if i.find(j) == 0:
                i = i.replace(j,'')
            if len(i) == 0:
                print(i,j)
                answer += 1
                break
        
    return answer