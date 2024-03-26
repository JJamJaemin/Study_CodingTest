def solution(array):
    answer = 0
    cnt = 0
    array.sort()
    length = len(array)
    index =int(length/2)
    answer = array[index]
    return answer