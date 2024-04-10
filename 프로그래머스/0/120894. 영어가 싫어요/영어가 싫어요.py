def solution(numbers):
    answer = 0
    a = {"zero":0,"one":1, "two":2, "three":3,"four":4,"five":5,"six":6,"seven":7,"eight":8,"nine":9}
    tmp = ''
    tmp2 = ''
    for i in numbers:
        tmp += i
        if tmp == 'zero':
            tmp2 += str(a[tmp])
            tmp =''
        if tmp == 'one':
            tmp2 += str(a[tmp])
            tmp =''
        if tmp == 'two':
            tmp2 += str(a[tmp])
            tmp =''
        if tmp == 'three':
            tmp2 += str(a[tmp])
            tmp =''
        if tmp == 'four':
            tmp2 += str(a[tmp])
            tmp =''
        if tmp == 'five':
            tmp2 += str(a[tmp])
            tmp =''
        if tmp == 'six':
            tmp2 += str(a[tmp])
            tmp =''
        if tmp == 'seven':
            tmp2 += str(a[tmp])
            tmp =''
        if tmp == 'eight':
            tmp2 += str(a[tmp])
            tmp =''
        if tmp == 'nine':
            tmp2 += str(a[tmp])
            tmp =''
        
        
    answer = int(tmp2)
    return answer