def solution(numbers, k):
    answer = 0
    length = len(numbers)
    cnt = 0
    c = 0
    while cnt < k:
        if length % 2 == 0: 
            for i in range(0,length,2):
                print(numbers[i])
                answer = numbers[i]
                cnt +=1
                if cnt == k:
                    break
        else:
            for j in range(c,length,2):
                if numbers[j] == numbers[length-1]:
                    c = 1
                else:
                    c = 0
                print(numbers[j])
                answer = numbers[j]
                cnt += 1
                if cnt == k:
                    break
    return answer