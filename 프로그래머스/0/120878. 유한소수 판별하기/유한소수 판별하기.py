def solution(a, b):
    answer = 0
    #a의 약수
    aa = []
    #b의 약수
    bb = []
    #공통 약수
    c = []
    tmp = 0
    #a의 약수 찾기
    for i in range(1, a + 1):
        if (a % i == 0) :
            aa.append(i)
    #b의 약수 찾기
    for i in range(1, b + 1):
        if (b % i == 0) :
            bb.append(i)
    #a와 b 공통된 약수 찾기
    for i in aa:
        if i in bb:
            c.append(i)
    #약분
    a = int(a / c[-1])
    b = int(b / c[-1])
    print(a,b,"기약분수")
    c = []
    #분모의 약수
    for i in range(1,b+1):
        if b % i == 0:
            c.append(i)
    a = []
    cnt = 0
    for i in c:
        for j in range(1,i):
            if i % j == 0:
                cnt += 1 
        if cnt == 1:
            a.append(i)
        cnt = 0
    str(a)
    if 2 in a:
        a.remove(2)
    if 5 in a:
        a.remove(5)
    print(a)
    print(len(a))
    if len(a) >= 1:
        answer = 2
    else:
        answer = 1
    return answer