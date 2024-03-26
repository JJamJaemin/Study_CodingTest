def solution(my_string):
    answer = []
    a=0
    for i in my_string:
        if i.isdigit():
            a = int(i)
            answer.append(a)
    answer.sort()
    answer = list(answer)
    return answer