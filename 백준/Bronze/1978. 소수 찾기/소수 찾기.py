N = int(input())
A = list(map(int, input().split()))
answer = 0
for i in range(N):
    if A[i] == 2:
        answer += 1
    if A[i] != 1 and A[i] % 2 != 0:
        cnt = 0
        for j in range(2, A[i]):
            if A[i] % j == 0 :
                cnt = 1
                break
        if cnt != 1:
            answer += 1

print(answer)