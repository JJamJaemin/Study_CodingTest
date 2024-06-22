def solution(str_list, ex):
    answer = ''
    for i in str_list:
        if ex in i:
            print("있음")
        else:
            answer = answer + i
    if answer != '':
        return answer
    else:
        return ''