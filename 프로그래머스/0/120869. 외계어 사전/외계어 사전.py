def solution(spell, dic):
    answer = 0
    cnt = 0
    tmp = 0
    spell_length = 0
    for i in dic:
        for j in spell:
            spell_length = len(spell)
            if i.find(j) != -1:
                cnt += 1
                print(i,j,cnt)
        if spell_length == cnt:
            tmp += 1
            print(i)
        cnt = 0
        spell_length = 0
    if tmp > 0:
        answer = 1
    else:
        answer = 2
    return answer