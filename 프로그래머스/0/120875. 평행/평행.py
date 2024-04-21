def solution(dots):
    answer = 0
    cnt = 0
    t = 0
    a = dots.copy()  # dots 리스트의 복사본을 만듦
    k = []
    k_tmp = []
    for i in dots:
        tmp = i
        print(tmp)
        a.remove(tmp)
        k_tmp = []
        for j in a:
            if tmp != j:
                if (tmp[0] - j[0]) != 0 and tmp[1]-j[1] != 0: #기울기 계산
                    k.append((tmp[0]-j[0])/(tmp[1]-j[1])) #기울기들의 집합
                    k_tmp.append((tmp[0]-j[0])/(tmp[1]-j[1])) #선 연결이 안되는 부분의 집합을 위한 리스트
                    b = k_tmp.copy()
                    print(k)
                else:
                    k.append(0)
                    k_tmp.append(0)
                if len(set(k_tmp)) != len(k_tmp):
                    print("초기화")
                    k_tmp = []
                    t += 1
                    print(t)
                    break
                    
            else:
                cnt += 1
                print(cnt)
        if len(k) == len(set(k)) and cnt == 0 or t == 1:
            answer = 0
        else: 
            answer = 1
        
    return answer
