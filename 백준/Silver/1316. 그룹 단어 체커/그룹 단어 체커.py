N = int(input())
a = 0
for i in range(N):
    S = input()
    answer = []
    group = True
    for j in range(len(S)):
        if S[j] in answer:
            if j != 0 and S[j-1] == S[j]:
                group = True
            else:
                group = False
                break
        else:
            answer.append(S[j])
    if group == True:
        a += 1
print(a)