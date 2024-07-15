N = int(input())
List = [[0 for j in range(100)] for i in range(100)]
answer = 0
for i in range(N):
    A, B = input().split()
    A = int(A)
    B = int(B)
    for i in range(10):
        for j in range(10):
            List[A+i][B+j] += 1
for i in range(100):
    for j in range(100):
        if int(List[i][j]) > 0:
            answer += 1
print(answer)
