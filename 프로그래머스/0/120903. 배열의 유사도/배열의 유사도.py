def solution(s1, s2):
    answer = 0
    count =0
    s1_length = len(s1)
    s2_length = len(s2)
    
    for i in  range(0, s1_length):
        for j in range(0,s2_length):
            if s1[i] == s2[j]:
                count += 1
    answer = count
    return answer