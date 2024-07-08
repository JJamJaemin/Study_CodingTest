S = input()
answer = 0
while(True):
    if S.find('c=') != -1:
        answer += 1
        S = S.replace('c=','.',1)
    elif S.find('c-') != -1:
        answer += 1
        S = S.replace('c-','.',1)
    elif S.find('dz=') != -1:
        answer += 1
        S = S.replace('dz=','.',1)
    elif S.find('d-') != -1:
        answer += 1
        S = S.replace('d-','.',1)
    elif S.find('lj') != -1:
        answer += 1
        S = S.replace('lj','.',1)
    elif S.find('nj') != -1:
        answer += 1
        S = S.replace('nj','.',1)
    elif S.find('s=') != -1:
        answer += 1
        S = S.replace('s=','.',1)
    elif S.find('z=') != -1:
        answer += 1
        S = S.replace('z=','.',1)
    else:
        break
S = S.replace('.','')
answer += len(S)
print(answer)