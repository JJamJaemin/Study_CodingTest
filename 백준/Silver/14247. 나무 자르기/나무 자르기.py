import sys

n = int(sys.stdin.readline()) #나무의 갯수
h = list(map(int, sys.stdin.readline().split())) #나무의 길이
grow = list(map(int, sys.stdin.readline().split())) #나무별 자라는 길이
answer = 0

grow.sort()
answer += sum(h)
for i in range(n):
    answer += grow[i] * i
print(answer)