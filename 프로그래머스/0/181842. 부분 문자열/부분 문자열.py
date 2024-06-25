def solution(str1, str2):
    answer = 0
    for i in range(len(str2)):
        print(str1[i:i+len(str1)])
        if str2[i:i+len(str1)] == str1:
            
            answer = 1
            break

    return answer