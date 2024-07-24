import sys
N = int(sys.stdin.readline())
list = []
for i in range(N):
    n = int(sys.stdin.readline())
    list.append(n)
sorted_list = sorted(list)
for i in range(N):
    print(sorted_list[i])
