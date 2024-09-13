n = int(input())

arr = [0] * 11
arr[1] = 1 # 1을 만들 수 있는 경우의 수
arr[2] = 2 # 2를 만들 수 있는 경우의 수
arr[3] = 4 # 3을 만들 수 있는 경우의 수

for i in range(4, 11):
    arr[i] = arr[i - 1] + arr[i - 2] + arr[i - 3]

for i in range(0,n):
    a = int(input())
    print(arr[a])