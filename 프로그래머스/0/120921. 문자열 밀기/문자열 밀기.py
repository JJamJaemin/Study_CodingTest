def solution(A, B):
    answer = 0
    if A == B:
        answer = 0
    else:
        length = len(A)
        for i in range(1,length):
            A = A[-1]+A[0:-1]
            print(A)
            if A == B:
                return i
            else:
                answer = -1
    return answer