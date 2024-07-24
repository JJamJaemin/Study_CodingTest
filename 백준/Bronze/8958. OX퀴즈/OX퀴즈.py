N = int(input())
for i in range(N):
    S = input()
    score = 0
    answer = 0
    for j in range(len(S)):
        if S[j] == 'O':
            score += 1
        else:
            score = 0
        answer += score
    print(answer)
