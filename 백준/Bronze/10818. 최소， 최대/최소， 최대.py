N = input()
N = int(N)
if N >= 1 and N <= 1000000:
  ls = [0] * N
  ls = list(map(int, input().split()))
Max = max(ls)
Min = min(ls)
print(Min, Max)