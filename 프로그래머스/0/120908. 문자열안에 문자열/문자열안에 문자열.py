def solution(str1, str2):
    find = str1.find(str2)
    if find != -1:
        answer = 1
    else:
        answer = 2

    return answer