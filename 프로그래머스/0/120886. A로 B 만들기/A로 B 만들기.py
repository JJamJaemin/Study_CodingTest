def solution(before, after):
    answer = 0
    cnt = 0
    ls_b = list(before)
    ls_a = list(after)
    length = len(ls_b)
    for i in range(0,length):
        tmp = ls_b[i]
        if ls_a.count(tmp) == ls_b.count(tmp):
            cnt += 1
            print(tmp, ls_b.count(tmp))
    if cnt == length:
        answer = 1
    return answer