N = input()
N = int(N)
ls = [0]*N
ls = list(map(int, input().split()))
answer = 0
if len(ls) == N:
    M = max(ls)
    idx = 0
    for i in ls:
        ls[idx] = ls[idx]/M*100
        answer += ls[idx]
        idx += 1
        
print(answer/N)



