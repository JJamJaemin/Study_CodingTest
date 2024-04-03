def solution(s):
    answer = ''
    tmp = 0
    ls = []
    a = ''
    for i in range(97, 123):
        a = chr(i)
        tmp = s.count(a)
        print(tmp)
        if tmp == 1:
            ls.append(a)
            print(ls)
    length = len(ls)
    for i in range(length):
        answer += ls[i]
    return answer