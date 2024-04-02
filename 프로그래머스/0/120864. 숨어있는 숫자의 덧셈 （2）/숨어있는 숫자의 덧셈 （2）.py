def solution(my_string):
    answer = 0
    length = len(my_string)
    ls = []
    str_ls = []
    tmp = 0
    tmp2 = ''
    for i in my_string:
        str_ls.append(i)
    for j in range(0,length):
        if str_ls[j].isdigit():
            if tmp == 0 and str_ls[j] == 0:
                print('첫숫자 0', str_ls[j])
            else:
                tmp2 += str_ls[j]
                tmp = 1
        else:
            if tmp2 != '':
                answer += int(tmp2)
                print('tmp2', tmp2)
            tmp2 = ''
            tmp = 0
        print(answer)
    if tmp2 != '':
        answer += int(tmp2)
        print('tmp2',tmp2)
    return answer