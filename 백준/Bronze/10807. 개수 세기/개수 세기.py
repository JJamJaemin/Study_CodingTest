N = input()
N = int(N)
if N >= 1 and N <= 100:
  ls = [0] * N
  ls = list(map(int, input().split()))
v = input()
v = int(v)
print(ls.count(v))