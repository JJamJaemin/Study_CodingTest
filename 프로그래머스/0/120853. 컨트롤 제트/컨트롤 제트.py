def solution(s):
    answer = 0
    ls = []
    length = 0
    length = len(s)
    tmp = ''
    for i in s:
        if i != ' ':
            tmp+= i
        if i == ' ' :
            ls.append(tmp)
            tmp =''
    ls.append(tmp)    
    print(ls)
    tmp2 = 0
    index = 0
    for i in ls:
        if i != 'Z':
            tmp2 += int(i)
            print(tmp2)
        else:
            tmp2 -= int(ls[index-1])
        index += 1
    answer = tmp2
    return answer