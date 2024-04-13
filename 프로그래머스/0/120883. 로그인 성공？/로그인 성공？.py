def solution(id_pw, db):
    answer = ''
    tmp = 0
    p_tmp = 0
    for i in db:
        if id_pw[0] == i[0]:
            tmp = 1
            if id_pw[1] == i[1]:
                p_tmp = 1
        
    if tmp == 1 and p_tmp == 0:
        answer = 'wrong pw'
    elif tmp == 1 and p_tmp == 1:
        answer = 'login'
    else:
        answer = 'fail'
    return answer