#검증수 : 5자리 제곱 + 합 /10의 나머지
A = list(map(int, input().split()))
answer = 0
for i in range(5):
    answer += A[i]**2
answer = answer % 10
print(answer)

