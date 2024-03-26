def solution(hp):
    answer = 0
    #장군개미 5 병장개미 3 일개미 1
    a = hp//5
    hp = hp%5
    b = hp//3
    hp = hp%3
    c = hp
    answer = a+b+c
    return answer