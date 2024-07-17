while(True):
    N = int(input())
    if N == -1:
        break
    A = []
    answer = 0
    cnt = 1
    while(cnt <= N):
        if N % cnt == 0:
            A.append(cnt)
        cnt += 1
    for i in A:
        answer += i
    if answer-N == N:
        print(N, end= " = ")
        for i in range(len(A)-1):
            if i != 0:
                print("+",A[i], end = " ")
            else:
                print(A[i], end= " ")
    else:
        print(N , end = " is NOT perfect.")
    print("")