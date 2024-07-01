def solution(lines):
    answer = 0
    tmp = []
    load = []
    for i in lines:
        length = i[1] - i[0]
        tmp = []
        for j in range(length):
            tmp.append(i[0]+j)
        load.append(tmp)
    s1 = set(load[0])
    s2 = set(load[1])
    s3 = set(load[2])
    print((s1 & s2) | (s2 & s3) | (s1 & s3))
    answer = len((s1 & s2) | (s2 & s3) | (s1 & s3))
    return answer