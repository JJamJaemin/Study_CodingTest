def solution(array):
    answer = 0
    ls =[]
    m = 0
    cnt=[]
    for i in array: #중복값 제거한 리스트 만들기
        if i in ls :
            print("존재하는 숫자",i)
        else:
            ls.append(i)
    for j in ls: #최빈값 구하기
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