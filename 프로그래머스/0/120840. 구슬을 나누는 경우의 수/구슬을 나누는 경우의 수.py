def solution(balls, share):
    answer = 0
    a = balls - share
    fact_a = 1
    fact_b = 1
    fact_c = 1
    while a != 0:
        fact_a *= a
        a -= 1
    while share != 0:
        fact_b *= share
        share -= 1
    fact = 1
    while balls != 0:
        fact_c *= balls
        balls -= 1
    answer = fact_c / (fact_a*fact_b)
    return answer