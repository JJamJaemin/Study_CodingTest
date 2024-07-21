N = int(input())
M = int(input())
stat = 0
answer = []
for i in range(N,M+1):
    stat = 0
    if i == 2:
        answer.append(i)
    if i != 1 and i % 2 != 0:
        for j in range(2,i):
            if i % j == 0:
                stat = 1
        if stat == 0:
            answer.append(i)
if len(answer) == 0:
    print(-1)
else:
    print(sum(answer))
    print(min(answer))




