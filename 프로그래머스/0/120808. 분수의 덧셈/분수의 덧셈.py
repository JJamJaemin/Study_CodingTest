def solution(numer1, denom1, numer2, denom2):
    answer = []
    tmp_1 = numer1 * denom2 #분자1
    tmp_2 = numer2 * denom1 #분자2
    tmp = denom1 * denom2 # 분모
    sub = [tmp_1+tmp_2, tmp]
    for i in range(1,1000):
        if sub[0] % i == 0 and sub[1] % i == 0:
            sub[0] = int(sub[0]/i)
            sub[1] = int(sub[1]/i)
        elif tmp == tmp_1 and tmp == tmp_2:
            sub[0] = 2
            sub[1] = 1
        elif sub[1] % sub[0] ==0:
            sub[1] = sub[1]/sub[0]
            sub[0] = 1
            
    answer = sub
    return answer