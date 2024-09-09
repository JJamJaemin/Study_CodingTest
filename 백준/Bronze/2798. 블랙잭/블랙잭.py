from itertools import combinations

N, M = map(int, input().split())
card = list(map(int, input().split()))
card.sort()

combs = list(combinations(card, 3))
max = 0
for i in combs:
    if sum(i) <= M and sum(i) > max:
        max = sum(i)
print(max)
