def solution(num, total):
    answer = []
    if num % 2 == 0:#num이 짝수 일때
        median = 0
        count = 0
        median = int(total/num)
        median_index = int(num/2)
        for i in range(0,median_index-1):
            answer.append(median+1 - (median_index-i))
            count += 1
        answer.append(median)
        for i in range(1,count+2):
            answer.append(median+i)
    else:
        #num이 홀수 일때
        median = 0
        count = 0
        median = int(total/num)
        median_index = int(num/2) +1 
        
        for i in range(0,int(median_index)-1):
            answer.append(median+1 - (median_index-i))
            count += 1
        answer.append(median)
        for i in range(1,count+1):
            answer.append(median+i)
        
    return answer