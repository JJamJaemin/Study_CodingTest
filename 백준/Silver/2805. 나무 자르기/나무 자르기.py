import sys
N,M = map(int, sys.stdin.readline().split())
tree = list(map(int, sys.stdin.readline().split()))
tree = sorted(tree)

def find_height():
    start = 0
    end = tree[-1]
    while start <= end:
        tmp = 0
        mid = (start + end) // 2
        for i in range(N):
            if tree[i] - mid > 0:
                tmp += tree[i] - mid
        if tmp >= M:
            answer = mid
            start = mid + 1
        else:
            end = mid - 1
    return answer

print(find_height())
