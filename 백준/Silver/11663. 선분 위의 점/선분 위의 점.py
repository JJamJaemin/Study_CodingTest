import sys
n,m = map(int, sys.stdin.readline().split()) #n:점 m:선분 개수
grid = list(map(int, sys.stdin.readline().split()))
grid = sorted(grid)

def find_start(a):
    start = 0
    end = n - 1
    while start <= end:
        mid = (start + end) // 2
        if grid[mid] < a:
            start = mid + 1
        else:
            end = mid - 1
    return end + 1

def find_end(b):
    start = 0
    end = n - 1
    while start <= end:
        mid = (start + end) // 2
        if grid[mid] > b:
            end = mid - 1
        else:
            start = mid + 1
    return end

for i in range(m):
    a,b = map(int, sys.stdin.readline().split())
    print(find_end(b)-find_start(a) + 1)
