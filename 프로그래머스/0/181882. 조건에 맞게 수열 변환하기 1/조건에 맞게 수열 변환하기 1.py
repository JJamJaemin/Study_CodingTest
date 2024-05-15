def solution(arr):
    answer = []
    index = 0
    for i in arr:
        if i >= 50 and i % 2 == 0:
            i = int(i / 2)
            arr[index] = i
            index += 1
        elif i < 50 and i % 2 != 0:
            i = int(i * 2)
            arr[index] = i
            index += 1
        else:
            index += 1
    answer = arr
    return answer