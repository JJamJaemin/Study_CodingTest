def solution(numbers):
    answer = 0
    m_max =0
    m2_max =0
    length = len(numbers)
    sorted_numbers = sorted(numbers)
    m_max = sorted_numbers[0] * sorted_numbers[1]
    m2_max = sorted_numbers[-1] * sorted_numbers[-2]
        
    
    if m_max > m2_max:
        answer = m_max
    else:
        answer = m2_max
    
    
    return answer