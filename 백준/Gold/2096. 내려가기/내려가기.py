n = int(input())

grid = list(map(int, input().split()))
dp_max = grid
dp_min = grid

for i in range(n-1):
    grid = list(map(int,input().split()))
    dp_max = [grid[0] + max(dp_max[0],dp_max[1]), grid[1] + max(dp_max[0], dp_max[1], dp_max[2]), grid[2] + max(dp_max[1], dp_max[2])]
    dp_min = [grid[0] + min(dp_min[0],dp_min[1]), grid[1] + min(dp_min[0], dp_min[1], dp_min[2]), grid[2] + min(dp_min[1], dp_min[2])]

print(max(dp_max), min(dp_min))