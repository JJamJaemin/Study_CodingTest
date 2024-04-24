def solution(dots):
    answer = 0
    tmp1 = dots[0]
    a = []
    for i in dots:
        t = i
        a.append((((tmp1[1] - t[1])**2) + ((tmp1[0] - t[0])**2))**(1/2))
    a.sort()
    answer = a[1] * a[2]
    return answer