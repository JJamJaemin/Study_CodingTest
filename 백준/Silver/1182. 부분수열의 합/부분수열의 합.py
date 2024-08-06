from itertools import combinations

N, S = map(int, input().split())
n_list = list(map(int, input().split()))
select_list = []
answer = 0

for i in range(1,N+1):
    select_list += list(combinations(n_list, i))

for i in range(len(select_list)):
    if sum(select_list[i]) == S:
        answer += 1
print(answer)