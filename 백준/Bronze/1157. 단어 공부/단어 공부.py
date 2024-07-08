S = input()
S = S.upper()
S = sorted(S)
S = ''.join(S)
max = 0
max2 = 0
answer = ''
subanswer = ''
cnt = 1
for i in range(len(S)):
    if i != 0 and S[i] == S[i-1]:
        cnt += 1
        if max <= cnt:
            max2 = max
            max = cnt
            subanswer = answer
            answer = S[i]
    elif i != 0 and S[i] != S[i-1]:
        if cnt > len(S)/2+1:
            break
        if cnt == 1 :
            if max <= cnt:
                max2 = max
                max = cnt
                subanswer = answer
                answer = S[i]
        cnt = 1
    elif len(S) == 1:
        answer = S[0]
        break

if len(S) != 1 and S.replace(answer,'') != '':
    S = S.replace(answer,'')
    if subanswer == '':
        subanswer = S[-1]
elif len(S) != 1 and S.replace(subanswer,'') == '':
    max = 0
if (S.count(subanswer)) == max:
    print('?')
else:
    print(answer)