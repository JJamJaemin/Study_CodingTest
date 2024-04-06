def solution(bin1, bin2):
    answer = ''
    b_1 = '0b'+bin1
    b_2 = '0b'+bin2
    b_1 = int(b_1,2)
    b_2 = int(b_2,2)
    sum = b_1 + b_2
    tmp = bin(sum)
    
    answer = tmp[2:]
    return answer