def solution(score):
    answer = []
    answer_tmp =[]
    for i in score:
        avg = (i[0]+i[1])/2
        print(i)
        answer_tmp.append(avg)
        print(answer_tmp)
        
    s_avg = sorted(answer_tmp,reverse=True)
    for j in answer_tmp:
        score = s_avg.index(j)
        answer.append(score+1)
    print(s_avg)
    return answer