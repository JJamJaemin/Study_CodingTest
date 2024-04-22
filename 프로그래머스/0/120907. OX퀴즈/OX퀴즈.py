def solution(quiz):
    answer = []
    for i in quiz:
        a = i.find('=')
        sol = i[:a]
        result = int(i[a+2:])
        if eval(sol) == result:
            answer.append('O')
        else:
            answer.append('X')
    return answer