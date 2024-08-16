N = int(input())
list = [int(input()) for i in range(N)]

A = [0] * (N+1) #한칸 전에서 올라오는 것
B = [0] * (N+1) #두칸 전에서 올라오는 것

if N == 1:
    print(list[0])
elif N == 2:
    print(list[0] + list[1])
else:
    A[1] = list[0]  # 첫번째 계단
    B[2] = list[1]  # 두번째 계단
    A[2] = list[0] + list[1]  # 두번째 계단
    for i in range(3,N+1):
        A[i] = B[i-1] + list[i-1]
        B[i] = max(A[i-2],B[i-2]) + list[i-1]
    print(max(A[-1],B[-1]))

