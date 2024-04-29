def solution(polynomial):
    answer = ''
    a = polynomial.split()
    x = 0
    c = 0
    length = len(a)
    for i in range(0,length) :
        if a[i].find('x') != -1: #x인 수 찾기
            print('다항식')
            print(a[i])
            if a[i].strip('x') == '':
                x += 1
            else:
                x += int(a[i].strip('x'))
        elif a[i] != '+' and a[i].find('x') == -1:
            c += int(a[i])
    if c == 0:
        if x == 1:
            answer = 'x'
        else:
            answer = str(x)+'x'
    else:
        if x == 1:
            answer = 'x'+' + '+str(c)
        elif x == 0:
            answer = str(c)
        else:
            answer = str(x)+'x'+' + '+str(c)
                
    return answer