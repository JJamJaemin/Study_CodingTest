def solution(array):
    answer = 0
    ls =[]
    m = 0
    cnt=[]
    for i in array:
        if i in ls :
            print("있는 숫자",i)
        else:
            ls.append(i)
    print(ls)
    for j in ls:
        cnt.append(array.count(j)) 
        if array.count(j) > m:
            m = array.count(j)
            tmp = j
    if cnt.count(m) > 1:
        tmp = -1
    if len(ls) == 1:
        tmp = ls[0]
    answer = tmp
    return answer